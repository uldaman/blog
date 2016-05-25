author: Martin
date: 2015-05-26 08:25
title: 17、通用对话框之 QFileDialog

> 说明: 这些文章都是本人学习"devbean QT 学习之路2"的笔记, 部分内容摘自原文, 部分是自己的领悟.

QFileDialog 即文件对话框, 常见的就是打开文件和保存文件对话框:

![](http://i60.tinypic.com/2bwhzb.jpg)

![](http://i57.tinypic.com/2j27qu0.jpg)

实现代码如下:

```cpp
void Qt_Notepad::OpenFile() {
    QString fileName = QFileDialog::getOpenFileName(this, "Open File", NULL, "file (*.*)");

    if (!fileName.isEmpty()) {
        QFile file;
        file.setFileName(fileName);
        if (file.open(QIODevice::ReadWrite)) {
            QTextStream in(&file);
            ui.textEdit->setText(in.readAll());
            file.close();
        }
    }
}

void Qt_Notepad::SaveFile() {
    QString fileName = QFileDialog::getSaveFileName(this, "Save File", "Untitled.txt");

    if (!fileName.isEmpty()) {
        QFile file;
        file.setFileName(fileName);
        if (file.open(QIODevice::ReadWrite)) {
            QTextStream out(&file);
            out << ui.textEdit->toPlainText(); //取纯文本
            file.close();
        }
    }
}
```
<br>
这两个函数中分别使用了 QFileDialog 的两个静态函数: getOpenFileName() 和 getSaveFileName();

先来看下 getOpenFileName() , 这个函数获取需要打开的文件的全路径.

```cpp
QString getOpenFileName(QWidget * parent = 0,
                        const QString & caption = QString(),
                        const QString & dir = QString(),
                        const QString & filter = QString(),
                        QString * selectedFilter = 0,
                        Options options = 0)
```
<br>

- parent: 父窗口.
- caption: 对话框标题;
- dir: 对话框打开时的默认目录, "." 代表程序运行目录, "/" 代表当前盘符的根目录(特指 Windows 平台; Linux 平台当然就是根目录), 这个参数也可以是平台相关的, 比如"C:\\"等;
- filter: 过滤器. 我们使用文件对话框可以浏览很多类型的文件, 但是, 很多时候我们仅希望打开特定类型的文件. 比如, 文本编辑器希望打开文本文件, 图片浏览器希望打开图片文件. 过滤器就是用于过滤特定的后缀名. 如果我们使用"Image Files(*.jpg *.png)", 则只能显示后缀名是 jpg 或者 png 的文件. 如果需要多个过滤器, 使用";;"分割, 比如"JPEG Files(*.jpg);;PNG Files(*.png)";
- selectedFilter: 默认选择的过滤器;
- options: 对话框的一些参数设定, 比如只显示文件夹等等, 它的取值是enum QFileDialog::Option, 每个选项可以使用 | 运算组合起来.
- Qt_Notepad::OpenFile() 函数中我们先获取了文件的全路径, 然后判断下是否获取到了, 如果成功获取了文件路径, 就创建一个 QFile 对象,  然后将用户选择的文件路径传递给这个对象, 接下来使用 QFile::open() 打开文件, 参数是以何种方式打开. 打开成功则返回 true, 由此继续进行下面的操作, 使用 QTextStream::readAll() 读取文件所有内容, 然后将其赋值给 QTextEdit 显示出来. 最后不要忘记关闭文件.
- Qt_Notepad::SaveFile() 函数也类似, 只不过最后一步, 我们使用 << 重定向, 将 QTextEdit 的内容输出到一个文件中. 关于文件操作, 我们会在后面的学习.

完整源码: [http://yunpan.cn/cwdG4VIJd8c5V](http://yunpan.cn/cwdG4VIJd8c5V)  访问密码 13dc
