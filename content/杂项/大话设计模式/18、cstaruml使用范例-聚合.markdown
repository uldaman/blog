author: Martin
date: 2015-03-11 15:30
title: 18、[C++]StarUML使用范例 — 聚合

聚合表示一种弱拥有关系, 即被聚合的类能单独存在.

用上一篇的方法快速添加一个 Context 类.

![](http://i62.tinypic.com/k4a4j7.jpg)

从toolbox中选择表示“Aggregation”的箭头, 并从 Strategy拖拽向 Context, 此时连线是没有箭头指向的, 选中连接线, 在右边的“Properties”框上, 将 "End1.IsNavigable" 勾选上,箭头就出来了.

![](http://i62.tinypic.com/sz7ww1.jpg)

将“End2.Name”一栏改为 Strategy，将“End2.Visibility”改为 "PRIVATE", 这样就自动为 Context 添加一个 Strategy 类型的私有成员, 表示 Context 维护一个 Strategy 对象的引用.

![](http://i62.tinypic.com/2urmbv4.jpg)
ols
