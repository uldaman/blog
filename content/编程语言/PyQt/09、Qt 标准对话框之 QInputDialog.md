Title: 09、Qt 标准对话框之 QInputDialog
Author: Martin
Date: 2016-05-14 21:26
Summary: 所谓标准对话框, 就是 Qt 内置的一些对话框, 比如文件选择、颜色选择等等.

Qt 的内置对话框大致分为以下几类;

- `QColorDialog`: 选择颜色;
- `QFileDialog`: 选择文件或者目录;
- `QFontDialog`: 选择字体;
- `QInputDialog`: 允许用户输入一个值, 并将其值返回;
- `QMessageBox`: 模态对话框, 用于显示信息、询问问题等;
- `QPageSetupDialog`: 为打印机提供纸张相关的选项;
- `QPrintDialog`: 打印机配置;
- `QPrintPreviewDialog`: 打印预览;
- `QProgressDialog`: 显示操作过程.

在学习 Qt 的时候, 已经接触过 [QMessageBox](http://blog.smallcpp.cn/16-tong-yong-dui-hua-kuang-zhi-qmessagebox.html) 和 [QFileDialog](http://blog.smallcpp.cn/17-tong-yong-dui-hua-kuang-zhi-qfiledialog.html) 了, 这节笔记学习下 QInputDialog.

QInputDialog 提供了一些简单的 `static` 函数，用于快速的建立一个对话框:

- getText (文本)
- getInteger (整数)
- getDouble (小数)
- getItem (下拉)

首先来看看 getText 函数：

```python
from PyQt4 import QtGui
QtGui.QInputDialog.getText(self, u'提示', u'输入信息:', QtGui.QLineEdit.Normal, u"请输入你的信息...")
```
<br>
代码比较简单，使用 getText 函数就可以弹出一个可供用户输入的对话框:

![](http://i63.tinypic.com/w1qixt.jpg)

另外, 该函数接收两个返回值:

- QString 用户输入的信息 (如果用户点击 cancel , 则该值为空)
- bool 用户点击 ok 还是 cancel

其它静态方法使用类似, 参考文档: [http://pyqt.sourceforge.net/Docs/PyQt4/qinputdialog.html#getText](http://pyqt.sourceforge.net/Docs/PyQt4/qinputdialog.html#getText)
