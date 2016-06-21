author: Martin
date: 2015-03-15 17:53
title: (五) C/C++ 调用 Lua 函数 与 Lua 栈平衡

Lua 提供了一些 Lua API 用来在 C/C++ 代码中直接调用 Lua 函数.
但是这种方法有个前提: 不管是调用 LuaGlue 函数还是原生的 Lua 函数, 我们必须知道被调用函数的函数名,.

最简单的 Lua API 就是 **int luaL_dostring (lua_State *L, const char *str);**

现在新建一个 Lua 脚本, 脚本代码如下 :





    <span style="color: #0000ff;">function</span><span style="color: #000000;"> Add(x, y)
       </span><span style="color: #0000ff;">return</span> x +<span style="color: #000000;"> y;
    </span><span style="color: #0000ff;">end</span>







我们在 C/C++ 中可以这样调用 Add 函数:





    luaL_dostring(m_pState, <span style="color: #800000;">"</span><span style="color: #800000;">Add(11, 12)</span><span style="color: #800000;">"</span>);







但是现在有个问题, Add 函数返回一个整型值, 但是使用 LuaL_dostring 方法不能获取到这个返回值.
我们通过 **lua_gettop()** (返回目前栈里元素的个数) 这个 Lua API 来证明这点, 编写代码如下:





    luaL_dofile(m_pState, <span style="color: #800000;">"</span><span style="color: #800000;">C:/Users/Administrator/Desktop/test.lua</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    luaL_dostring(m_pState, </span><span style="color: #800000;">"</span><span style="color: #800000;">Add(11, 12)</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #0000ff;">int</span> nOut =<span style="color: #000000;"> lua_gettop(m_pState);
    printf(</span><span style="color: #800000;">"</span><span style="color: #800000;">当前栈元素数量 = %d.\n</span><span style="color: #800000;">"</span>, nOut);







输入结果为: **"当前栈元素数量 = 0".**
可以看到返回值并没有被保存在 Lua 栈上, 因为 Lua 虚拟机有垃圾回收功能, 它负责 Lua 脚本中的内存管理, 定期释放脚本中无引用数据.
luaL_dostring(m_pState, "Add(11, 12)"); 这句代码的功能就是用 Lua 虚拟机来执行这句 Add(11, 12) 脚本代码, 当它执行完毕后, 其所占用的栈内存就被 Lua 虚拟机回收了.

那怎么才能在 C/C++ 中获取到 Lua 函数的返回值呢? 看下面的代码:





    lua_State* m_pState =<span style="color: #000000;"> luaL_newstate();
    luaL_openlibs(m_pState);

    luaL_dofile(m_pState, </span><span style="color: #800000;">"</span><span style="color: #800000;">C:/Users/Administrator/Desktop/test.lua</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    lua_getglobal(m_pState, </span><span style="color: #800000;">"</span><span style="color: #800000;">Add</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    lua_pushnumber(m_pState, </span><span style="color: #800080;">11</span><span style="color: #000000;">);
    lua_pushnumber(m_pState, </span><span style="color: #800080;">12</span><span style="color: #000000;">);
    lua_pcall(m_pState, </span><span style="color: #800080;">2</span>, <span style="color: #800080;">1</span>, <span style="color: #800080;">0</span><span style="color: #000000;">);

    </span><span style="color: #0000ff;">int</span> nOut =<span style="color: #000000;"> lua_gettop(m_pState);
    printf(</span><span style="color: #800000;">"</span><span style="color: #800000;">当前栈元素数量 = %d.\n</span><span style="color: #800000;">"</span><span style="color: #000000;">, nOut);

    </span><span style="color: #0000ff;">int</span> nSum = luaL_optinteger(m_pState, -<span style="color: #800080;">1</span>, <span style="color: #800080;">0</span><span style="color: #000000;">);
    printf(</span><span style="color: #800000;">"</span><span style="color: #800000;">计算结果为 = %d.\n</span><span style="color: #800000;">"</span><span style="color: #000000;">, nSum);

    lua_close(m_pState);</span>







也就是手动模拟上一篇笔记中提到的执行 Lua 函数过程: **先将函数名压栈, 再压入两个参数, 最后通过 lua_pcall() 来执行函数**. 输出结果为:

![](http://i57.tinypic.com/2z3ucdv.jpg)

为什么这样调用 Lua 函数就能获取到返回值呢?
因为 Lua 虚拟机**只处理 Lua 脚本中的无引用数据, 而不会去处理 C/C++ 端的数据, 管理 C/C++ 端的 Lua 栈是需要自己动手的**.

这种调用方式和之前用 LuaL_dostring 的区别在于, LuaL_dostring 是告诉 Lua 虚拟机去执行 Add(11, 12) 这句代码.
而上面代码中是手动通过 lua_pcall() 来直接进入函数主体的, 进入函数主体后, 程序再将控制权交给 Lua 虚拟机, 之后 Lua 虚拟机取出两个参数进行运算并将结果压回栈顶, 接下来函数开始返回, Lua 虚拟机清空参数栈保留返回值栈后就将程序的控制权还给 C/C++ 端了.
换句话说, LuaL_dostring 方式中是通过 Lua 虚拟机进入的函数主体, 因此函数返回时 Lua 虚拟机会进行“扫尾”操作, 而 lua_pcall 方式是通过 C/C++ 代码进入函数主体的, 那么栈顶的返回值如果不进行特殊处理会一直被保存.

那么问题又来了, 如果这个返回值会被一直保存, 那多次通过这种方式调用 Lua 函数后, Lua 栈不是会爆掉? 答案是肯定的, 看下面代码:





    <span style="color: #0000ff;">for</span> (<span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span>; i < <span style="color: #800080;">10</span>; i++<span style="color: #000000;">) {
        lua_getglobal(m_pState, </span><span style="color: #800000;">"</span><span style="color: #800000;">Add</span><span style="color: #800000;">"</span><span style="color: #000000;">);
        lua_pushnumber(m_pState, </span><span style="color: #800080;">11</span><span style="color: #000000;">);
        lua_pushnumber(m_pState, </span><span style="color: #800080;">12</span><span style="color: #000000;">);
        lua_pcall(m_pState, </span><span style="color: #800080;">2</span>, <span style="color: #800080;">1</span>, <span style="color: #800080;">0</span><span style="color: #000000;">);

        </span><span style="color: #0000ff;">int</span> nOut =<span style="color: #000000;"> lua_gettop(m_pState);
        printf(</span><span style="color: #800000;">"</span><span style="color: #800000;">当前栈元素数量 = %d.\n</span><span style="color: #800000;">"</span><span style="color: #000000;">, nOut);
    }</span>





![](http://i61.tinypic.com/22cfv4.jpg)

可以看到 Lua 栈在不断的增大, 那怎么办呢?
别担心, Lua 提供了** lua_Pushxxx** 及** lua_Popxxx** 系列 Lua API 供 C/C++ 端来管理 Lua 栈(在上一篇笔记中已经接触到了一部分 lua_Pushxxx 系列的 Lua API).
再看下面的代码:





    <span style="color: #0000ff;">for</span> (<span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span>; i < <span style="color: #800080;">10</span>; i++<span style="color: #000000;">) {
        lua_getglobal(m_pState, </span><span style="color: #800000;">"</span><span style="color: #800000;">Add</span><span style="color: #800000;">"</span><span style="color: #000000;">);
        lua_pushnumber(m_pState, </span><span style="color: #800080;">11</span><span style="color: #000000;">);
        lua_pushnumber(m_pState, </span><span style="color: #800080;">12</span><span style="color: #000000;">);
        lua_pcall(m_pState, </span><span style="color: #800080;">2</span>, <span style="color: #800080;">1</span>, <span style="color: #800080;">0</span><span style="color: #000000;">);
    }
    </span><span style="color: #0000ff;">int</span> nOut =<span style="color: #000000;"> lua_gettop(m_pState);
    lua_pop(m_pState, nOut);
    nOut </span>=<span style="color: #000000;"> lua_gettop(m_pState);
    printf(</span><span style="color: #800000;">"</span><span style="color: #800000;">当前栈元素数量 = %d.\n</span><span style="color: #800000;">"</span>, nOut);





![](http://i59.tinypic.com/f1f50k.jpg)

可以看到, 函数被调用了 10 次, 但是因为我们调用了 lua_pop() 来平衡 Lua 栈, 最终的 Lua 栈元素个数为 0.

最后要提醒大家, **lua_tonumber() 和 lua_tostring() 等系列 Lua API 只是简单得获取 Lua 栈上的内容但并不对栈进行操作.
**另外要注意的是: **一定要将数据取出后保存到别的变量中去再进行 Lua 栈平衡操作, 否则会因为清栈操作导致程序异常, 切记！**
 ba
