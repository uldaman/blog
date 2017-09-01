author: Martin
date: 2015-06-12 07:51
title: (十) Java 中的数组

Java 中的数组和 C 中数组在使用上可能看不出什么区别, 实际上也的确差不多;
但是它们在内存中还是有很大区别的, Java 中的数组不像 C 语言中那样是连续的内存块, 它是一个对象;

Java 通过 数据类型标示符 + 数组符号[] 来声明一个数组对象的引用. 如 int[] n = null, String[] str = null 等等;
Java 通过 new 关键字生成具体的数组对象, 如 int[] n = new int[30]; 这就生成一个可存 30 个 int 型数据的数组对象, n 是这个数组对象的引用.
Java 中还提供了另外一种直接创建数组的方式, 它将声明数组、分配空间和赋值合并完成, 如 int[] n = { 10, 11, 12, 13 }, 或者可以这么写 int[] n = new int[]{ 10, 11, 12, 13 }.

在 Java 中, 数组的访问和 C 中一致, 但是 Java 中的数组还提供了一些有用的属性和方法(因为它是一个对象), 这在 C 中就是不可能的了, 数组长度: length, 拷贝当前数组: clone().
在 C 语言中, 要遍历一个数组需要提供两个数据, 数组名和数组长度, 在 Java 中就不需要提供长度了, 直接使用数组的 length 属性就可以了.



* * *



二维数组

所谓二维数组, 可以简单的理解为是一种“特殊”的一维数组, 它的每个数组空间中保存的是一个一维数组.

二维数组定义方式: int[][] nn = null 或者 int nn[][] = null.

不规则二维数组: 在定义二维数组时也可以只指定行的个数, 然后再为每一行分别指定列的个数, 如果每行的列数不同, 则创建的是不规则的二维数组, 如:





    <span style="color: #0000ff;">int</span>[][] nn = <span style="color: #0000ff;">new</span> <span style="color: #0000ff;">int</span>[3<span style="color: #000000;">][];
    nn[</span>0] = <span style="color: #0000ff;">new</span> <span style="color: #0000ff;">int</span>[5<span style="color: #000000;">];
    nn[</span>1] = <span style="color: #0000ff;">new</span> <span style="color: #0000ff;">int</span>[6<span style="color: #000000;">];
    nn[</span>2] = <span style="color: #0000ff;">new</span> <span style="color: #0000ff;">int</span>[7];








* * *



Arrays 工具类

Arrays 类是 Java 中提供的一个工具类, 在 java.util 包中, 该类中包含了一些方法用来直接操作数组, 比如可直接实现数组的排序、搜索等.

Arrays 中常用的方法, 如:
使用前要先导入包: import java.util.Arrays;

1. 排序: Arrays.sort(数组名), 升序排列.

2. 将数组转换为字符串: Arrays.toString(数组名), 该方法按顺序把多个数组元素连接在一起, 多个元素之间使用逗号和空格隔开.

3. 填充数组: Arrays.fill(数组名, 元素), 用指定元素填充数组.

4. 比较两数组元素是否相等: Arrays.equals(array1, array2).

5. 查找数组元素: Arrays.binarySearch(数组名, 元素), 必须先对数组排序, 否则结果不正确, 如果不存在就返回负数.

具体的用法可以再参数网上资料.



* * *



foreach

在遍历数组、集合时, foreach 更简单便捷, 这种语法类似 C++11 中的 <[基于范围的 for 循环](http://www.smallcpp.cn/small_349.php)>.

语法:

for (元素类型 元素变量 : 遍历对象) {

}
???
