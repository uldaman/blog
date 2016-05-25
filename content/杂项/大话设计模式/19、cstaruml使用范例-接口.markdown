author: Martin
date: 2015-03-11 15:50
title: 19、[C++]StarUML使用范例 — 接口

C++在设计时, 接口这种概念还没有提出来, 所以C++中没有直接支持接口的语法, 但是可以使用抽像类来实现接口.

接口（interface）是抽像类的变体, 抽象类里面可以有非虚函数, 但接口里只能有虚函数.

从toolbox中, 选择“Interface”, 并点击图表的某处, 将其改名为 Strategy.

![](http://i59.tinypic.com/30mtlhh.jpg)

在顶部工具栏选择 “Stereotype Display” 下拉按钮, 将值改变为“None”, 这将改变默认的圆形形状, 使其变为和普通类一样的长方形.

![](http://i58.tinypic.com/257dllg.jpg)

还是在顶部工具栏, 取消选中 "Suppress Operations" , 这将使我们能够看到接口的方法栏.
并且选中 "Suppress Attributes" , 这将隐藏使接口的属性栏, 因为接口里只能有虚函数, 不能包含数据成员.
最后在 "Properties" 面板勾上 IsAbstract 属性.

![](http://i62.tinypic.com/121eatf.jpg)
