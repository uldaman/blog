author: Martin
date: 2015-06-13 12:29
title: (二十一) StringBuilder 类

在 Java 中, 除了可以使用 String 类来存储字符串, 还可以使用 StringBuilder 类或 StringBuffer 类存储字符串.

因为对 String 的修改会生成新的 String 对象, 所以当频繁操作 String 时, 就会额外产生很多消耗, 使用 StringBuilder 或 StringBuffer 就可以避免这个问题, 它们是可变类, 任何对它指向的字符串的操作都不会产生新的对象.
至于 StringBuilder 和StringBuffer, 它们基本相似, 不同之处, StringBuffer 是线程安全的, 而 StringBuilder 则没有实现线程安全功能, 所以性能略高.

StringBuilder str1 = new StringBuilder();

StringBuilder str2 = new StringBuilder(“xxx”);

StringBuilder 类也提供了一些方法来操作字符串:
![](http://i59.tinypic.com/2mzb78k.jpg)
