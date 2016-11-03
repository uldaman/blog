author: Martin
date: 2015-05-25 18:05
title: 16、通用对话框之 QMessageBox

> 说明: 这些文章都是本人学习”devbean QT 学习之路2”的笔记, 部分内容摘自原文, 部分是自己的领悟.

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

看到 QMessageBox 很自然的也就想到 Windows Api MessageBox, 实际这两者也的确差不多, 都是用于显示消息提示的.

![](http://i60.tinypic.com/2h5i93o.jpg)

QMessageBox 中有几个 static func 我们会经常使用:

`void about(QWidget * parent, const QString & title, const QString & text)`:<br>
显示关于对话框. 这是一个最简单的对话框, 其标题是 title, 内容是 text, 父窗口是 parent. 对话框只有一个 OK 按钮.

`void aboutQt(QWidget * parent, const QString & title = QString())`:<br>
显示关于 Qt 对话框. 该对话框用于显示有关 Qt 的信息.

`StandardButton critical(QWidget * parent, const QString & title, const QString & text, StandardButtons buttons = Ok, StandardButton defaultButton = NoButton)`:<br>
显示严重错误对话框. 这个对话框将显示一个红色的错误符号. 我们可以通过 buttons 参数指明其显示的按钮. 默认情况下只有一个 Ok 按钮, 我们可以使用 StandardButtons 类型指定多种按钮.

`StandardButton information(QWidget * parent, const QString & title, const QString & text, StandardButtons buttons = Ok, StandardButton defaultButton = NoButton)`:<br>
QMessageBox::information() 函数与 QMessageBox::critical() 类似, 不同之处在于这个对话框提供一个普通信息图标.

`StandardButton question(QWidget * parent, const QString & title, const QString & text, StandardButtons buttons = StandardButtons( Yes | No ), StandardButton defaultButton = NoButton)`:<br>
QMessageBox::question() 函数与 QMessageBox::critical() 类似, 不同之处在于这个对话框提供一个问号图标, 并且其显示的按钮是“是”和“否”两个.

`StandardButton warning(QWidget * parent, const QString & title, const QString & text, StandardButtons buttons = Ok, StandardButton defaultButton = NoButton)`:<br>
QMessageBox::warning() 函数与 QMessageBox::critical() 类似, 不同之处在于这个对话框提供一个黄色叹号图标.

我们可以看到大部分 static func 函数有个 StandardButton 返回值, 我们可以根据这个返回值来判断用户点击了 QMessageBox 的哪个按钮, 一般是 QMessageBox::Ok、QMessageBox::Cancel、QMessageBox::Yes、QMessageBox::No 等.

```cpp
if (QMessageBox::Yes == QMessageBox::question(this,
                                              "Question",
                                              "Are you OK?",
                                              QMessageBox::Yes | QMessageBox::No,
                                              QMessageBox::Yes)) {
    QMessageBox::information(this, "Hmmm...", "I'm glad to hear that!");
} else {
    QMessageBox::information(this, "Hmmm...", "I'm sorry!");
}
```
<br>
当然这些 static func 可以满足我们大部分的项目需求, 然而, 有时, 我们需要显示一个特殊的 QMessageBox, 此时, 我们就要使用 QMessageBox 的属性设置 API 来达到目的, 例如我们想弹出下面这种 QMessageBox.

![](http://i58.tinypic.com/1zydo2o.jpg)

实现这个 QMessageBox 的代码如下:

```cpp
QMessageBox msgBox;
msgBox.setText(tr("The document has been modified."));
msgBox.setInformativeText(tr("Do you want to save your changes?"));
msgBox.setDetailedText(tr("Differences here..."));
msgBox.setStandardButtons(QMessageBox::Save
                          | QMessageBox::Discard
                          | QMessageBox::Cancel);
msgBox.setDefaultButton(QMessageBox::Save);
int ret = msgBox.exec();
switch (ret) {
case QMessageBox::Save:
    qDebug() << "Save document!";
    break;
case QMessageBox::Discard:
    qDebug() << "Discard changes!";
    break;
case QMessageBox::Cancel:
    qDebug() << "Close document!";
    break;
}
```
<br>

- setText() 设置对话框的主要文本信息;
- setIformativeText() 设置对话框的简单说明文本;
- setDetailedText() 设置对话框的详细信息, 当我们使用了这个条 API 后, 弹出的对话框就会多出一个 Show Details , 点击就能显示我们设置的详细信息;
- setStandardButtons() 主动设置了对话框上显示的按钮, 这里我们设置了三个;
- exec() 弹出模态对话框, 最后根据其返回值进行相应的操作.

更多的 QMessageBox 用法就需要使用时查阅帮助文档了.
