author: Martin
date: 2015-03-11 13:09
title: 16、[C++] StarUML使用范例 -- 虚类

启动StarUML，弹“New Project By Approach”对话框, 选择“Empty Project”新建项目.

![](http://i57.tinypic.com/wqvy2x.jpg)

在右边的“Model Explorer”面板中可以看到新建的“Untitled”工程, 工程的属性可以在下方的Properties面板中修改（工程名、作者等）.

![](http://i58.tinypic.com/dncz6s.jpg)

通过“Model”主菜单, 或者在 Model Explorer 面板的工程上右击, 依次 Add — Model 来添加一个模型.

![](http://i61.tinypic.com/f36w54.jpg)

通过“Model”主菜单, 或者在刚新建的模型 Model1 上右击，依次 Add Diagram — Class Diagram.

![](http://i57.tinypic.com/2cr3mn8.jpg)

点击主菜单“Model” — “Profile…”菜单去设置工程所需的 profile, **这决定了工程所使用的规则和约定**. 这里我们包含”C++ Porfile”这一配置.



![](http://i61.tinypic.com/34yv9d3.jpg)

现在，开始真正绘制类图, 从左边的“Toolbox”面板选择“类”图标, 然后左键单击绘制窗口的某处, 这样就使用通用名字创造了一个新的类, 双击, 将类改名为 Strategy.

![](http://i59.tinypic.com/ao9lwm.jpg)

点击“Attribute”(蓝色方块), 为类添加一个属性(或者在刚添加的类图上右击, “Add”—“Attribute”), 填入期望的名字, 如:“m_radius”.

![](http://i57.tinypic.com/289egsi.jpg) --> ![](http://i58.tinypic.com/kohmu.jpg)

点击右边“Model Explorer”中的“m_radius”, 在右下边的 "Properties" 面板中的 Visibility 下拉框中选择“PRIVATE”(私有的), 再在“Type”中打开浏览, 在 “Data Type”下拉框中选择 double 作为 m_radius 属性的类型,

![](http://i59.tinypic.com/2873hox.jpg)

![](http://i60.tinypic.com/2qtfp7t.jpg)

![](http://i59.tinypic.com/30tsx9e.jpg)



点击“Operation”(红色方块), 为类添加一个方法(或者在刚添加的类图上右击, “Add”—“Operation”), 填入期望的名字, 如:“Algorithm()”.

![](http://i60.tinypic.com/5mzszm.jpg) --> ![](http://i60.tinypic.com/21j1xfo.jpg)

现在为这个方法设置 void 返回值 和 int 参数.

在“Model Explorer”中右击 "Algorithm" 选择“Add Parameter”.

在“Properties”框中, 将参数的名子变为空, 将“DirectionKind”选为“RETURN”, 将“Type”选为 double.

![](http://i61.tinypic.com/n15u7n.jpg)

再次右击 "Algorithm" 选择“Add Parameter”.

在“Properties”框中, 将参数的名子改为 arg1, 将“Type”选为 int.

![](http://i59.tinypic.com/2ewzlp5.jpg)

最后, 将 Strategy 和 Algorithm 的 IsAbstract 属性框打上勾, 他们在图标上的名字将变为斜体, 表明这是一个虚类.

![](http://i62.tinypic.com/iegv0m.jpg)
卙
