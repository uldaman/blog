author: Martin
date: 2015-03-09 05:35
title: 13、资源文件及 Action

[TOC]

# 添加资源
Qt 资源系统是一个跨平台的资源机制, 用于将程序运行时所需要的资源以二进制的形式存储于可执行文件内部. 如果你的程序需要加载特定的资源(图标、文本翻译等), 那么, 将其放置在资源文件中, 就再也不需要担心这些文件的丢失. 也就是说, 如果你将资源以资源文件形式存储, 它是会编译到可执行文件内部.

双击打VS项目文件中的.qrc文件打开资源编辑器.

![](http://i61.tinypic.com/20uphmc.jpg)

![](http://i62.tinypic.com/15f20s1.jpg)

Add Prefix 添加前缀, 即上图的 /Demo .

Add File 添加资源文件.

![](http://i60.tinypic.com/29vat06.jpg)

返回 Qt 编辑器中, 可以发现资源文件已经添加好了.

![](http://i60.tinypic.com/24b0qc8.jpg)

接下来为这个新添加的资源文件关联动作.

# 添加 Action
Action 可以显示在**菜单栏**, 作为一个菜单项, 当用户点击该菜单项, 对用户的点击做出响应;<br>
也可以在**工具栏**, 作为一个工具栏按钮, 用户点击这个按钮就可以执行相应的操作, Qt 使用 QAction 类作为动作.<br>
动作包含了图标、菜单文字、快捷键、状态栏文字、浮动帮助等信息.

默认的, 菜单栏及工具栏只有 **QMainWindow** 上才有, 如果想在 QDialog 或者 QWidget 添加该怎么做呢?<br>
要记得，QToolBar 以及 QStatusBar 都是 QWidget 的子类, 因此我们就可以将其结合布局管理器添加到另外的 QWidget 上面 (QLayout 布局提供了 setMenuBar() 函数，可以方便的添加菜单栏).

下面我们来添加一个动作.

![](http://i60.tinypic.com/kbewix.jpg)

![](http://i61.tinypic.com/vqha4w.jpg)

![](http://i58.tinypic.com/35asu46.jpg)

![](http://i58.tinypic.com/9gc7zc.jpg)

这样一个动作便添加好了.

![](http://i61.tinypic.com/ftpsuv.jpg)

那么怎么使用这个动作?

很简单, 直接拖拽动作编辑器中的icon到工具栏或菜单项里就可以了.

![](http://i62.tinypic.com/dh915h.jpg)

接下来就要为这个 Action 关联操作代码了, 即连接信号和槽.

```cpp
Demo::Demo(QWidget *parent)
    : QMainWindow(parent)
{
    ui.setupUi(this);
    connect(ui.action_New, &QAction::triggered, [](bool) {
        qDebug() << "This is a Demo";
    });
}
```
<br>
triggered() 是 QAction 的信号函数, 当点击 QAction 时被发出.
