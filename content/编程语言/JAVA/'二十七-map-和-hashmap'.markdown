author: Martin
date: 2015-06-14 14:53
title: (二十七) Map 和 HashMap

上一篇笔记学习了 Java 容器中的 Collection 家庭, 接下来学一学 Map 家庭.

Map 接口提供了一种映射关系, 其中的元素以键值对(key – value)的形式存储, 能够实现根据 key 快速查找 value(和 C++ 中的 stl::map 差不多).

Map 中的键值对以 Entry 类型的对象实例形式存在(stl::map 中是 value_type).

Map 中的键值对中的 key 值是不可重复的, value 值则可以, 这一点 stl::map 也是一样的, 同样的, stl 提供了 multimap 来实现 key 值可重复的 map, Java 也提供了 key 值可以重复的 map, 就是IdentityHashMap.

Map 插入键值对的方法不同于上一篇中学过的 add 方法, 它使用的是 put 方法, 参数为 key 值 和 value 值.

Map 中常用的方法:
keySet(): 返回 Map 中包含的键的 Set.
values(): 返回 Map 中包含的值的 Connection.
entrySet(): 返回 Map 中包含的映射关系的 Set.

HashMap 类是 Map 接口的一个重要实现类, 也是最常用的, 基于哈希表实现.
HashMap 中的 Entry 对象是无序排列的.
Key 和 Value 都可以为 null, 但是一个 HashMap 只能有一个 key 为 null 的映射(因为 key 不能重复).



* * *



实例:

上一篇笔记中做过一个学生选课的案例, 我们已经可以通过 List、Set 来管理备选课程, 现在继续为其添加功能, 通过 Map<String, Student> 进行学生信息管理, Key 为学生 ID, value 为学生对象.

[http://yunpan.cn/cQAGwDcYmtdDP](http://yunpan.cn/cQAGwDcYmtdDP)  访问密码 ce09

增



刪



改


查
