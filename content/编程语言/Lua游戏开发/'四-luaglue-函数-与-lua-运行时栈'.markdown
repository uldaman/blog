author: Martin
date: 2015-03-15 16:17
title: (四) LuaGlue 函数 与 Lua 运行时栈

在之前, 我们写了一个很简单的 LuaGlue 函数, 然而这个函数不接收参数和也没有返回值, 但是不可否认的是, LuaGlue 函数具有传递参数和返回值的能力.
这种功能通过 Lua 运行时栈来完实现.

要搞明白 Lua 栈, 首先要搞清楚栈的索引是如何定义的.

![](http://i57.tinypic.com/219xv1h.jpg)

当初始化一个栈的时候, 它的栈底索引是 1, 而栈顶相对索引是 -1.
Lua 栈的结构和 C/C++ 的栈具有异曲同工之处, 即先进后出, 最选压栈的元素被保存在栈底.

假设存在一个 LuaGlue 函数 Add(int i, intj), 它接收两个整型参数并返回相加的结果;
现在, 我们在 Lua 脚本中使用它: local nRet = Add(11, 12);
我们来看看 Lua 栈的变化过程.
当执行到这段代码的时候, 首先把函数名(Add)压栈, 然后将第一个参数(11)压栈, 再将第二个参数(12)压栈, 此时栈变成这样:

![](http://i60.tinypic.com/2ch9b4h.jpg).

然后 Lua 解释器取出栈底的函数名, 通过函数名找到函数的入口, 进入函数主体, 此时栈是这样的:

![](http://i57.tinypic.com/2el9yy8.jpg)

此时已经进入 C/C++ 写的 LuaGlue 函数底层代码.
C/C++ 从 Lua 栈中取出里面的两个参数进行加法计算, 然后将结果压栈, 现在栈变成了这样:

![](http://i61.tinypic.com/5zdtzk.jpg)

函数调用成功返回之后, Lua 解释器释放掉参数栈保留返回值栈, 此时栈是这样的:

![](http://i61.tinypic.com/2ev6h3k.jpg)

最后, Lua 解释器将这个返回值取出并赋值给 nRet, 此时 Lua 栈为空.

那么问题来了!
在 C/C++ 写的 LuaGlue 函数底层代码中, 怎么取出这些参数, 然后又怎么将计算结果压回栈, 最后又是怎么设置栈底指针的呢?
cLua 类中的 GetIntArgument 方法能够从 Lua 栈中返回一个整型数据.

    <span style="color: #0000ff">int</span> cLua::GetIntArgument(<span style="color: #0000ff">int</span> num, <span style="color: #0000ff">int</span> nDefault <span style="color: #008000">/*</span><span style="color: #008000">= 0</span><span style="color: #008000">*/</span><span style="color: #000000">) {
        </span><span style="color: #0000ff">return</span><span style="color: #000000"> luaL_optinteger(m_pScriptContext, num, nDefault);
    }</span>







而cLua 类中的 PushInt 方法能够向 Lua 栈中压入一个整型数据.




    <span style="color: #0000ff">void</span> cLua::PushInt(<span style="color: #0000ff">int</span><span style="color: #000000"> value) {
        lua_pushinteger(m_pScriptContext, value);
    }</span>







这两个方法都要求传入参数在 Lua 栈中的位置.





好了, 现在我们大概可以写出这个 LuaGlue 的底层代码了:




    LuaGlue LuaGlue_Add(lua_State*<span style="color: #000000"> L) {
        </span><span style="color: #0000ff">int</span> argNum = <span style="color: #800080">1</span><span style="color: #000000">;
        </span><span style="color: #0000ff">int</span> nSum1 = luaL_optinteger(L, argNum++, <span style="color: #800080">0</span>);   <span style="color: #008000">//</span><span style="color: #008000"> 取出参数一</span>
        <span style="color: #0000ff">int</span> nSum2 = luaL_optinteger(L, argNum++, <span style="color: #800080">0</span>);   <span style="color: #008000">//</span><span style="color: #008000"> 取出参数二</span>
        lua_pushinteger(L, nSum1 + nSum2);      <span style="color: #008000">//</span><span style="color: #008000"> 压入结果</span>
        <span style="color: #0000ff">return</span> <span style="color: #800080">1</span>;   <span style="color: #008000">//</span><span style="color: #008000"> 表示此 LuaGlue 函数有一个返回值</span>
    }







最后, 需要说明的是 LuaGlue 函数的返回值个数, Lua 函数可以返回多个值, LuaGlue 函数也支持这个特性.
它通过最后一句代码 return x; 来指定到底返回了几个值, 当然这个数值必须要和 Lua 栈中实际 Push 进的返回值数量一致.
另外, 这个函数中还用到一个小技巧, 在函数开始定义了一个局部变量并初始为 1, 每当从 Lua 栈中读取了一个参数就递加 1.
lo
