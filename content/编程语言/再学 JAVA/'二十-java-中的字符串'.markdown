author: Martin
date: 2015-06-13 12:13
title: (二十) Java 中的字符串

在之前的笔记就已经使用了字符串, Java 中, 字符串被作为 String 类型的对象处理, 该类位于 java.lang 包中, 默认情况下这个包被自动导入所有的程序.

创建 String 对象的方法：


    String si = "xxx"<span style="color: #000000">;
    String s2 </span>= <span style="color: #0000ff">new</span><span style="color: #000000"> String();
    String s3 </span>= <span style="color: #0000ff">new</span> String("xxx");







String 对象具有不变性, 即对象创建后则不能被修改(如果需要一个可以改变的字符串, 我们可以使用 StringBuffer 或者 StringBuilder);
而平常见到的 Java 代码中, 对 String 对象的修改其实是创建了新的对象.




一些 String 必须了解的细节:
*、通过 String s1="字符串" 声明了一个字符串对象, s1 存放的是字符串对象的引用, 然后通过 s1="新的字符串", 其实质是创建了新的字符串对象, 变量 s1 指向了新创建的字符串对象.
*、每次 new 一个字符串就是产生一个新的对象, 即便两个字符串的内容相同, 使用 "==" 比较时也为 "false", 如果只需比较内容是否相同, 应使用 "equals()" 方法.
*、多次出现的字符常量, 只会创建一个, 如 String s1="字符串", String s2="字符串", 那么 s1、s2 指向的是同一个对象, 即 s1 == s2.




String 类提供了许多用来处理字符串的方法, 例如, 获取字符串长度、对字符串进行截取、将字符串转换为大写或小写、字符串分割等.
![](http://i59.tinypic.com/w1624g.jpg)




小细节:
*. 字符串 str 中字符的索引从0开始, 范围为 0 到 str.length()-1
*. 使用 indexOf 进行字符或字符串查找时, 如果匹配返回位置索引, 如果没有匹配结果, 返回 -1
*. 使用 substring(beginIndex , endIndex) 进行字符串截取时, 包括 beginIndex 位置的字符, 不包括 endIndex 位置的字符
??
