Title: 01、UML 架构及 StarUML
Author: Martin
Date: 2016-03-31 21:28
Summary: UML 图形分三大类, 对象图、交互图和状态图, 细分又有八种图形, 用例图、时序图、协作图、状态图、活动图、类图、组件图 及 部署图.

[TOC]

# UML 架构
UML 图形分类:

- 对象图
    + 类图
    + 组件图
    + 部署图
- 交互图
    + 用例图
    + 时序图
    + 协作图
    + 活动图
- 状态图
    + 状态图

[参考文档](http://www.ibm.com/developerworks/cn/rational/r-uml/)

这里重点学习 __用例图、时序图 和 类图__ 三张图.

# StarUML
StarUML 5.0 貌似是最后一个免费版本...

安装好后运行, 会让选一个 approach (入口), 直接点 Cancel 就好, 会以默认的视图打开 StarUML.

![](http://i66.tinypic.com/dde2rr.jpg)

也可以选择 Rational, 这种 approach 用的也比较多.

![](http://i65.tinypic.com/260psvn.jpg)

![](http://i64.tinypic.com/14t6iyh.jpg)

- __用例视图__(Use Case View), 包含系统中所有的参与者、用例和用例图, Use Case View 在系统中可以看成是一个独立的实现, 它侧重用高级别的视图表明系统做什么, 而不用考虑具体的实现

- __逻辑视图__(Logical View), 重点描述在系统中如何实现用例, 它提供系统各模块的详细视图, 并描述这些模块之间的关系, Logical View 包含对一些类图、时序图和状态图, 通过这些具体的元素, 开发者可以对系统构建具体的设计

- __组件视图__(Component View), 包含的信息有代码库、可执行文件、运行时库，还有在模型中的其他组件, 一个组件就是一个物理的编码模块

- __发布视图__(Deployment View), 关于系统的物理发布, 它不同于系统的逻辑架构
