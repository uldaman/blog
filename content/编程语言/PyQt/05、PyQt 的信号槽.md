Title: 05、PyQt 的信号槽
Author: Martin
Date: 2016-05-12 00:29
Summary: 学习使用 Eric 来创建一个信号槽.

关于 Qt 信号槽的基础知识参考我另一个系列笔记: [零基础QT入门](http://www.smallcpp.cn/category/ling-ji-chu-qtru-men2.html)

[TOC]

# 使用 Qt 设计师生成信号槽
首先, 在 `Qt 设计师` 上的信号槽是可以被 Eric 转换的, 也就是说, 以前那种直接在 `Qt 设计师` 上拖拽来编辑信号槽的方式是被兼容的.

![](http://i67.tinypic.com/2f06h69.jpg)

保存好后, 到 eric 中编译窗体, 就会发现 `Ui_first_window.py` 文件被修改了, 添加了一行信号槽关联代码:

![](http://i68.tinypic.com/264qjw0.jpg)

# 使用 Eric 生成信号槽
然后, eric 强大的地方在于, 它能够快捷的从 `Ui_first_window.py` 生成信号槽, 而不需要事先在 `Qt 设计师` 中拖放, 我们先在刚才的窗体上添加一个新按钮, 记住它的 **objectName** 为 pushButton_2, 然后回到 eric 中, 在 `first_window.ui` 上右键, 选择 "生成对话框代码", 我们可以看到 "窗体代码产生器" 上已经发生了一些变化:

![](http://i64.tinypic.com/2gvr5o4.jpg)

红框部分就是 pushButton_2 按钮的信号, 我们勾选 `on_pushButton_2_clicked()` 后点击保存, 发现 `first_window.py` 文件已被更改, 多了一个槽处理函数:

```python
@pyqtSignature("")
def on_pushButton_2_clicked(self):
    """
    Slot documentation goes here.
    """
    # TODO: not implemented yet
    raise NotImplementedError
```
<br>
这个槽函数会被关联到 pushButton_2 按钮的 clicked 信号, 我们翻阅代码发现并没有找到 Qt 的信号槽关联函数 (connect), 其实它是通过下面这句代码来实现的:

![](http://i66.tinypic.com/2v8pmc0.jpg)

这可以说是 eric 给我们定义好的 "轮子" 了.

> 这里仅补充一下**信号槽编程**与**事件编程**的差异, 对于从 MFC 转到 Qt 来的我而言, on\_pushButton\_2\_clicked() 函数类似 MFC 中的按钮点击事件, 其实并不然, 底层实现先抛开不说, 就使用上而言, MFC 按钮点击事件需要先定义一个事件 (一串数字), 而信号槽则不需要, 只要两个函数符合条件, 就能通过 Qt 的 connect 函数把它们关联起来.

# 自定义信号槽
记得以前在学 Qt 时, 连接信号槽的那个函数难记死了...而在 PyQt 中, 连接一个信号槽, 简直简单到爆...并且 PyQt4 allows any Python callable to be used as a slot, not just Qt slots.

参考官方文档: [new_style_signals_slots](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#PyQt4.QtCore.pyqtSlot)

你可以通过 `PyQt4.QtCore.pyqtSignal` 来定义一个信号, 调用新信号的 `connect` 方法连接一个槽, 然后在合适的时候调用 新信号的 `emit` 方法:

```python
from PyQt4.QtCore import pyqtSignal

def on_new_solt():
    print u'接收到新信号'

sin_new = pyqtSignal()  # 定义新信号
sin_new.connect(on_new_solt)  # 连接信号槽
sin_new.emit()  # 发出信号
```
# 记一次调错
在开始一个项目的过程中, 遇到一个问题:

假设存在两个 table widget, 我希望为这两个 table widget 自定一个信号槽, 一开始我是这么写的:

```python
from PyQt4.QtCore import pyqtSignal

class ClassName(Ui_Xxx):

    def __init__(self, arg):
        self.table_widget_one.sin_update = pyqtSignal()
        self.table_widget_one.sin_update.connect(self.update_one)

        self.table_widget_two.sin_update = pyqtSignal()
        self.table_widget_two.sin_update.connect(self.update_two)

    def update_one(self):
        print u'更新第一个 table widget'

    def update_two(self):
        print u'更新第二个 table widget'
```
<br>
发现脚本直接跑不起来.... 经探索发现, 信号必须被定义成`类成员`, 像下面这样:

```python
from PyQt4.QtCore import pyqtSignal

class ClassName(Ui_Xxx):
   table_widget_one.sin_update = pyqtSignal()  # 类成员
   table_widget_two.sin_update = pyqtSignal()  # 类成员

    def __init__(self, arg):
        self.table_widget_one.sin_update.connect(self.update_one)
        self.table_widget_two.sin_update.connect(self.update_two)

    def update_one(self):
        print u'更新第一个 table widget'

    def update_two(self):
        print u'更新第二个 table widget'
```
<br>
改过后, 脚本可以跑起来了, 但是发现信号槽关联失败, 再探索发现信号要定义成类的一级成员, 于是我只能再定义个类继承 QTableWedgit:

```python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSignal

class My_Table_Widget(QtGui.QTableWidget):
    sin_update = pyqtSignal(dict)
```
<br>
然后在 Qt 设计师中让 `table_widget_one` 和 `table_widget_two` 提升为 `My_Table_Widget`, 最后改主脚本为:

```python
from PyQt4.QtCore import pyqtSignal

class ClassName(Ui_Xxx):

    def __init__(self, arg):
        self.table_widget_one.sin_update.connect(self.update_one)
        self.table_widget_two.sin_update.connect(self.update_two)

    def update_one(self):
        print u'更新第一个 table widget'

    def update_two(self):
        print u'更新第二个 table widget'

```
