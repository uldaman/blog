author: Martin
date: 2015-03-16 10:41
title: (六) 5.2+ Lua 中的可变参数

在 5.2 之前, 你也许像下面这样来使用 Lua 中的变参功能:





    <span style="color: #0000ff;">function</span><span style="color: #000000;"> text( ... )
        </span><span style="color: #0000ff;">for</span> i = <span style="color: #800080;">1</span>, arg.n <span style="color: #0000ff;">do</span>
            <span style="color: #ff00ff;">print</span><span style="color: #000000;">(arg[i])
        </span><span style="color: #0000ff;">end</span>
    <span style="color: #0000ff;">end</span><span style="color: #000000;">

    text(</span><span style="color: #800080;">10</span>, <span style="color: #800080;">20</span>)







这完全没有问题, 在 5.2 之前, Lua 将函数的可变参数存放在一个叫 arg 的表中, 除了参数以外, arg 表中还有一个域 n 表示参数的个数.

但是, 到了 5.2 中, 定义函数的时候,  如果使用了 "..." 表达式, 那么语言后台将不会再帮忙打包 "arg" 对象了, 它将直接使用** {...} — — **用可变参数中的所有值创建一个列表.
需要注意的是, 这个表没有 n 域, 它只含参数, 我们可以用下面这种遍历表的方法来遍历它:





    <span style="color: #0000ff;">for</span> i,v <span style="color: #0000ff;">in</span> <span style="color: #ff00ff;">ipairs</span>{...} <span style="color: #0000ff;">do</span>
        <span style="color: #ff00ff;">print</span><span style="color: #000000;">(v)
    </span><span style="color: #0000ff;">end</span>







或者我们可以自己手动构建 arg 表: local arg = table.pack(...)
table.pack(...) 将返回用所有参数以键 1,2, 等填充的新表,  并将 "`n`" 这个域设为参数的总数(就像 5.2 之前 Lua 后台帮我们打包的一样).
接下来就可以像 5.2 之前那使用变参功能了.





    <span style="color: #0000ff;">function</span><span style="color: #000000;"> text( ... )
        </span><span style="color: #0000ff;">local</span> arg =<span style="color: #000000;"> table.pack(...)
        </span><span style="color: #0000ff;">for</span> i = <span style="color: #800080;">1</span>, arg.n <span style="color: #0000ff;">do</span>
            <span style="color: #ff00ff;">print</span><span style="color: #000000;">(arg[i])
        </span><span style="color: #0000ff;">end</span>
    <span style="color: #0000ff;">end</span><span style="color: #000000;">

    text(</span><span style="color: #800080;">10</span>, <span style="color: #800080;">20</span>)



nar
