author: Martin
date: 2015-06-14 04:53
title: (二十六) Java 中的容器

学过 STL 的都应该知道容器的概念, Java 中也有这样的东西.

Java 中的容器有两大接口: Collection 和 Map;

Collection 又分为三个小接口: List、Queue 和 Set.

![](http://i59.tinypic.com/2w565u0.jpg)

ArrayList、HashSet 和 HashMap 分别是 List、Set 和 Map 的实现类, 这三种也是使用最广泛的三个类.



* * *



Collection 接口是 List、Set 和 Queue 接口的父接口, 它定义了可用于操作 List、Set 和 Queue 的方法(增、删、改、查).

List 是元素有序并且可以重复的集合, List 可以精确控制每个元素的插入位置, 或删除某个位置的元素.

ArrayList 是数组序列, 是 List 接口的一个重要实现类, 它的底层是由数组实现的.


    <span style="font-family: 微软雅黑;">Set 和 List 类似, </span><span style="font-family: 微软雅黑;">最大的不同就是 List 是可以有序并且可重复的, 而 Set 是无序并且不能重复的.
    List 适合经常追加数据, 插入, 删除数据, 但随即取数效率比较低.
    Set 适合经常地随即储存, 插入, 删除, 但是在遍历时效率比较低.</span>




    <span style="font-family: 微软雅黑;">这个其实也没什么好记的了, 有 STL 基础, 学这个太简单, 上一份例子代码(附视频解说):
    <span style="text-decoration: underline;"><span style="color: #3366ff;"><a style="color: #3366ff; text-decoration: underline;" href="http://yunpan.cn/cQsGPx38k4ISg">http://yunpan.cn/cQsGPx38k4ISg</a></span></span>  访问密码 8bf2
    <embed src="http://static.video.qq.com/TPout.swf?vid=d0156knzsv7&auto=0" align="middle" height="400" type="application/x-shockwave-flash" width="480"></embed>
    </span>




    <span style="font-family: 微软雅黑;">需要注意的是 Java 中的泛型不能是基本数据类型, 必须是其包装类, 如, ArrayList<Integer>.</span>
