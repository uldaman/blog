Title: 02、PyQt Win7 64 环境下安装
Author: Martin
Date: 2016-05-11 20:47
Summary: Python 2.7 + PyQt 4.11 + Eric6 安装简介

Windows 下配置环境就简单了, Riverbank Computing 帮你集成好了 Qt 的开发环境, 只需下载一个安装包就可以...

![](http://i65.tinypic.com/2njwmdl.jpg)


所以你总共只需要安装下面三个软件:

- python 2.7 for windows 64
- [PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x64.exe](https://www.riverbankcomputing.com/software/pyqt/download)
- [Eric6](https://sourceforge.net/projects/eric-ide/files/eric6/stable/)

前两个就不说了, 说说 Eric6 的安装, 下载源码解压到任意目录, 执行 `python install.py` 即可以将 eric6 安装到 python 根目录下, 打开 `python 根目录/Scripts`:

![](http://i67.tinypic.com/s4rnk3.jpg)

点击 **eric6.bat** 就能打开 eric6 了, 首次打开时会让你配置 eric6, 如果以后想重新配置可以点击 **eric6-configure.bat**.

> 安装好后, 刚才解压的 Eric6 目录就可以删除了.
