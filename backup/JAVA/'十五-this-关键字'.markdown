author: Martin
date: 2015-06-12 10:42
title: (十五) this 关键字

和 C++ 一样, 代表的是就是当前对象本身.

不过 Java 中还有特殊的作用: this 调用构造函数.

格式: this();

我们知道一个类, 可以有多个构造函数, 调用哪个构造函数取决于 this() 里的参数个数及类型;

this调用构造函数, 必须是构造函数中第一条语句;

    <span style="color: #000000">Person()  {
       System.out.println(</span>"无参数构造函数"<span style="color: #000000">);
    }
    Person(</span><span style="color: #0000ff">int</span><span style="color: #000000"> i)  {
       </span><span style="color: #0000ff">this</span><span style="color: #000000">();
       System.out.println(</span>"一个参数构造函数"<span style="color: #000000">);
    }</span>
