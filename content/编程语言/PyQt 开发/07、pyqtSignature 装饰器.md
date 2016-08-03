Title: 07、pyqtSignature 装饰器
Author: Martin
Date: 2016-05-14 18:03
Summary: 在前面笔记的例子中, 我们发现槽函数有个装饰器 @pyqtSignature(""), 这个装饰器有什么作用呢?

在前面笔记的例子中, 我们发现槽函数有个装饰器 @pyqtSignature(""), 这个装饰器有什么作用呢?

这货往简单了说就是一个 "标识", 标识这个槽函数是和哪个信号函数绑定的...那么, 为什么要有这个标识呢? 记得以前在用 C++ 开发 Qt 时, 并没有要标识...

> 官方说该装饰器在新的 pyqt 中已被 [pyqtSlot](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#PyQt4.QtCore.pyqtSlot) 替代

参考官方文档:<br>
[http://pyqt.sourceforge.net/Docs/PyQt4/old_style_signals_slots.html#the-qtcore-pyqtsignature-decorator](http://pyqt.sourceforge.net/Docs/PyQt4/old_style_signals_slots.html#the-qtcore-pyqtsignature-decorator)<br>
[http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#PyQt4.QtCore.pyqtSlot](http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html#PyQt4.QtCore.pyqtSlot)

举个例子:

```python
QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self, QtCore.SLOT(_fromUtf8("on_pushButton(bool)")))

@pyqtSignature("")
def on_pushButton(self, checked):
    """
    Slot documentation goes here.
    """
    print "111"
```
<br>
我这里手动关联了一个信号槽, 按以前对 C++ 开发 Qt 的理解, 当产生 `clicked(bool)` 信号时, 会找到 `on_pushButton(self, checked)` 槽函数...

然而, 遗憾的是, pyqt 不具备这样的功能, 如果你不在 `@pyqtSignature("")` 声明, pyqt 是找不到这个槽函数的...所以你必须改成 `@pyqtSignature("bool")`.

个人理解是, 因为 Python 函数的灵活性 (PyQt4 allows any Python callable to be used as a slot, not just Qt slots), 太灵活了, 所以要被限制 ? ?

以及 Python 不支持函数重载, 加上个标识, 同名的函数就可以被 Qt 认为是两个不同的函数了 ? ?

这个标识可以是一个 python 的基本类型, 如 int、bool 等等.
