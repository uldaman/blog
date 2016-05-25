author: Martin
date: 2015-03-14 18:14
title: (二) Lua 与 C/C++ 的第一次亲密接触

Lua 引擎本身是由 C 语言撰写, 在 C 或 C++ 中使用 Lua 脚本也相当简单, 因此, Lua 常被用来扩展 C/C++ 程序.

**Lua 环境(Lua_State)
**Lua 脚本运行时的所有数据(变量, 函数, 数据结构等)都被保存在一个称做 Lua_State 的结构中.
对于 C/C++ 与 Lua 交互来说, Lua_State 就是用来发送和接收数据的地方, 它利用栈(Lua Stack)来达到这个目的.
因此, Lua 解释器运行时都会自身维护一个运行时栈(Lua Stack), 专门用来处理 Lua 环境.
关于栈的其它知识以后再补充. 现在我们只要知道: **Lua 的运行时栈就是 Lua 与其它语言数据交互的地方**.

**Lua 访问 C/C++ 接口
**即用 C/C++ 来完成底层功能, 然后暴露自定义的 api 给 Lua，以供其调用.
我们把这种 C/C++ 暴露给 Lua 的接口称做 LuaGlue 函数.
当然, "制作"这种接口需要用到 Lua 提供给 C/C++ 的 API, 通常把它们称之为 Lua API.
Lua 除了提供这种"制作" LuaGlue 函数的 Lua API 外, 还提供了其它诸如能获取 Lua 脚本中变量值、调用 Lua 函数等功能的 Lua API.
**简单来说:** Lua 脚本通过 LuaGlue 来访问和操作 C/C++, 而 C/C++ 通过 Lua API 来访问和操作 Lua 脚本.

在创建 LuaGlue 之前, 首先要在 VS 中初始化 Lua 环境, 基本的初始化步骤如下：
1. 使用 **luaL_newstate()** 创建一个新的 Lua 环境(Lua_State).
2. 使用 **luaL_openlibs(Lua_State*)** 函数加载 Lua 的标准库.
3. 现在可以在 C/C++ 中使用 Lua 了.
4. 在我们不需要的时候,要将 Lua_State 关闭掉:** lua_close(Lua_State*)**;
需要注意的是在 Lua 5.0 之前, 是使用 lua_open() 来创建一个新的 Lua 环境, 而非 luaL_newstate();
而 luaL_openlibs() 也是 Lua 5.1 版本才出现的 Lua API, 它用来打开所有的 Lua 库, 在这之前, 我们需要写一堆代码来初始化 Lua 库:
luaopen_base(L);
luaopen_io(L);
luaopen_math(L);
...

当然在此之前还要按上篇文件的内容搭建好开发环境.

初始化好 Lua 环境后, 就可以开始编写 LuaGule 函数了.
所有的 LuaGule 函数被要求为 int 返回和一个 lua_State* 参数, 并且必须是 C 方式调用, 这意味着, 我们需要用 **extern “C”**来声明函数.
编写好后, 为了让其能被 Lua 访问, 程序需要使用一个 Lua API -- **lua_register(lua_State *L, const char *name, lua_CFunction f)** 来注册 LuaGule 函数.

    #include <windows.h><span style="color: #000000">
    #include </span><tchar.h><span style="color: #000000">
    #include </span><span style="color: #800000">"</span><span style="color: #800000">LuaEx.h</span><span style="color: #800000">"</span>


    <span style="color: #0000ff">extern</span> <span style="color: #800000">"</span><span style="color: #800000">C</span><span style="color: #800000">"</span> <span style="color: #0000ff">int</span> LuaGule_Out(lua_State*<span style="color: #000000"> L) {
        printf(</span><span style="color: #800000">"</span><span style="color: #800000">This is a LuaGule! \r\n</span><span style="color: #800000">"</span><span style="color: #000000">);
        </span><span style="color: #0000ff">return</span> <span style="color: #800080">0</span><span style="color: #000000">;
    }

    </span><span style="color: #0000ff">int</span> _tmain(<span style="color: #0000ff">int</span> argc, _TCHAR*<span style="color: #000000"> argv[]) {
        lua_State</span>* L =<span style="color: #000000"> luaL_newstate();
        luaL_openlibs(L);
        lua_register(L, </span><span style="color: #800000">"</span><span style="color: #800000">新函数</span><span style="color: #800000">"</span>, LuaGule_Out); <span style="color: #008000">//</span><span style="color: #008000"> 注册 LuaGule</span>
    <span style="color: #000000">
        luaL_dofile(L, </span><span style="color: #800000">"</span><span style="color: #800000">C:/Users/Administrator/Desktop/test.lua</span><span style="color: #800000">"</span><span style="color: #000000">);

        lua_close(L);

        system(</span><span style="color: #800000">"</span><span style="color: #800000">PAUSE</span><span style="color: #800000">"</span><span style="color: #000000">);
        </span><span style="color: #0000ff">return</span> <span style="color: #800080">0</span><span style="color: #000000">;
    }</span>







编译生成 exe 可执行文件, 再在桌面新建一个 test.lua 文件, 里面写上一句代码: 新函数()




然后运行刚写生成的 exe 可执行文件:




![](http://i58.tinypic.com/2vc816u.jpg)
 ?
