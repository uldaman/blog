author: Martin
date: 2015-03-11 13:36
title: 17、[C++] StarUML使用范例 -- 子类

上一篇, 我们添加了一个名为 Strategy 的虚类.

现在, 为这个虚类快速添加子类.

在 "Model Explorer" 面板中点选 Strategy, 按 Ctrl + C 或者 右击选择 Copy 菜单进行复制, 再点选 Model1 按 Ctrl + V 或者 右击选择 Paste 菜单进行粘贴.

![](http://i59.tinypic.com/15dry52.jpg) --> ![](http://i60.tinypic.com/2m7dpp3.jpg)



点选粘贴出来的新类 Strategy_, 将它的名字改为 ConcreteA, 并取消勾选 IsAbstract 框.

再按住 ConcreteA 拖动到绘图面板上, 一个新类图就出现了.

![](http://i62.tinypic.com/1z1tik2.jpg)

从toolbox中选择表示“Generalization”的箭头, 并从 ConcreteA 拖拽向 strategy, 使 ConcreteA 继承 strategy, 如果想使连接线表现为直角的方式, 右击连接线, 并选择 "Format — Line Style — Rectilinear" 菜单.

![](http://i61.tinypic.com/2uzp2mr.jpg)
p Q
