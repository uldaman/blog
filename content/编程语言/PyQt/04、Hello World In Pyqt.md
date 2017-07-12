Title: 04、Hello World In Pyqt
Author: Martin
Date: 2016-05-11 23:39
Summary: 学习使用 Eric 开发一个 Qt 程序的基本流程.

新建项目

![](http://i64.tinypic.com/2zpt5b4.jpg)

配置项目属性

![](http://i64.tinypic.com/2nkqpkz.jpg)

新建 UI (切换到下图序号 1 的标签, 在下面空白区右键, 选择新建窗体)

![](http://i68.tinypic.com/3voxt.jpg)

![](http://i67.tinypic.com/91m1jo.jpg)

![](http://i64.tinypic.com/240x5b7.jpg)

点击保存后, eric6 上出现了 `first_window.ui` 文件, 并且自动打开了 `Qt 设计师`.

![](http://i66.tinypic.com/1phydz.jpg)

关于如何使用 `Qt 设计师` 及 Qt 编程的基础知识参考我另一个系列笔记: [零基础QT入门](http://www.smallcpp.cn/category/ling-ji-chu-qtru-men2.html)

这个 `first_window.ui` 文件是 Qt 专用的, python 不认识它, 但是最终我们是通过 python 来运行程序, 所以需要把 `*.ui` 文件转化成 python 识别的格式, 方法很简单, 在 `*.ui` 文件上右键选择 `编译窗体` (编译成功/失败会弹框提示).

![](http://i66.tinypic.com/sm3bte.jpg)

切换回下图序号 1 的标签, 可以看到多了一个 `Ui_first_window.py` 文件 (以 **Ui** 开头, 标明这是从 Qt 的 Ui 文件转换来的)

![](http://i68.tinypic.com/11qr6op.jpg)

这个文件有自测代码, 在 Eric 上按 **F2** 或者 点击下图中的图标, 就能打开刚才新建的窗体了.

```python
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
```
<br>
![](http://i65.tinypic.com/dfitfn.jpg)

![](http://i65.tinypic.com/292v8dy.jpg)

虽然 `Ui_first_window.py` 能够被直接运行, 但它本质还是个 ui 层面的文件 (从它的命名就可以看出), 不应该被直接运行, 而从 OOA/D 的角度说, 它是属于 view 层,  eric 提供了快捷的方法从 `Ui_xxx.py` 文件生成 controller 层的代码, 所有的在界面上的事件处理都在这层完成.

首先切换到下图序号 1 的标签, 在 `first_window.ui` 上右键, 选择 "生成对话框代码"

![](http://i65.tinypic.com/2qs5wmo.jpg)

![](http://i66.tinypic.com/aui5wp.jpg)

切换到下图序号 1 的标签, 可以看到又多了个文件

![](http://i67.tinypic.com/1411mcn.jpg)

这个文件要做些修改.

去掉一个多余的点，将

```python
from .Ui_first_window import Ui_Form
```
<br>
变成

```python
from Ui_first_window import Ui_Form
```
<br>
添加测试代码:

```python
if __name__ == "__main__":
    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
```
<br>
然后就可以按 **F2** 或者 点击工具栏上的图标, 就能打开刚才新建的窗体了.
