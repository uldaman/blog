author: Martin
date: 2015-06-16 12:05
title: 三、Lua 中的閉包

对于习惯了 C/C++ 这种不可嵌套定义函數的语言来说, 理解闭包真不太容易;

要解釋閉包就要先理解幾個小知識點:
Lua 中的函数是带有词法定界（lexical scoping）的第一类值（first-class values）.

**第一类值（first-class values）**是指,** **在 Lua 中函数和其他值（数值、字符串）一样, 函数可以被存放在变量中, 也可以存放在表中, 可以作为函数的参数, 还可以作为函数的返回值;
正因為函數也可以被嵌套定義在另一個函數內部, 假设函数 f2 定义在函数 f1 中, 那么就称 f2 为 f1 的内嵌(inner)函数, f1 为 f2 的外包(enclosing)函数, 外包和内嵌都具有传递性, 即 f2 的内嵌必然是 f1的内嵌, 而 f1 的外包也一定是 f2 的外包, 内嵌函数能访问外包函数已创建的所有局部变量, 这种特性便是所谓的**词法定界（lexical scoping）, **而这些局部变量则称为该内嵌函数的外部局部变量(external local variable)或 **upvalue.**

简单的说闭包是一个函数加上它可以正确访问的 upvalue, 这个函数一般是一个匿名函数, 并且定义在另一个函数内部, 这个函数可以访问定义在外部函数内的成员变量, 参数, 以及全局函数, 如:


    <span style="color: #0000ff">function</span><span style="color: #000000"> f1(n)
       </span><span style="color: #008000">--</span><span style="color: #008000"> 函数参数也是局部变量  </span>
       <span style="color: #0000ff">return</span> <span style="color: #0000ff">function</span><span style="color: #000000"> ()
          </span><span style="color: #ff00ff">print</span>(n) <span style="color: #008000">--</span><span style="color: #008000"> 引用外包函数的局部变量  </span>
       <span style="color: #0000ff">end</span>
    <span style="color: #0000ff">end</span>






對閉包有興趣的可以看看這篇網文: [http://www.cnblogs.com/yyxt/p/3875185.html](http://www.cnblogs.com/yyxt/p/3875185.html)







* * *


**通過閉包來模擬面向對象**



上一篇筆記, 通過 table 模擬了面向對象, 這一次, 通過閉包來模擬.



    <span style="color: #0000ff">local</span> <span style="color: #0000ff">function</span><span style="color: #000000"> People()
        </span><span style="color: #0000ff">local</span> tab =<span style="color: #000000"> {}

        </span><span style="color: #0000ff">function</span><span style="color: #000000"> tab:sayHi()
            </span><span style="color: #ff00ff">print</span>(<span style="color: #800000">"</span><span style="color: #800000">Say Hi!</span><span style="color: #800000">"</span><span style="color: #000000">)
        </span><span style="color: #0000ff">end</span>

        <span style="color: #0000ff">return</span><span style="color: #000000"> tab
    </span><span style="color: #0000ff">end</span>

    <span style="color: #0000ff">local</span> p =<span style="color: #000000"> People()
    p.sayHi()</span>






再來看看怎麼繼承:



    <span style="color: #0000ff">local</span> <span style="color: #0000ff">function</span><span style="color: #000000"> Man()
        </span><span style="color: #0000ff">local</span> tab =<span style="color: #000000"> People()

        </span><span style="color: #0000ff">function</span><span style="color: #000000"> tab:sayHi()
            </span><span style="color: #ff00ff">print</span>(<span style="color: #800000">"</span><span style="color: #800000">Man Say Hi!</span><span style="color: #800000">"</span><span style="color: #000000">)
        </span><span style="color: #0000ff">end</span>

        <span style="color: #0000ff">return</span><span style="color: #000000"> tab
    </span><span style="color: #0000ff">end</span>

    <span style="color: #0000ff">local</span> m =<span style="color: #000000"> Man()
    m.sayHi()</span>
:ry
