Title: 2、搭建VS + QT 项目环境
Author: Martin
Date: 2015-02-15 14:10
Summary: 介绍如何在 Windows 下安装 QT, 及用 VS 新建一个 QT 项目.

假设已经安装过 vs2010 或者 更高版本.

首先去官网下载Qt: [http://www.qt.io/download-open-source/](http://www.qt.io/download-open-source/)

![](http://i63.tinypic.com/wkfwy8.jpg)

点击上面的 Downloads, 进入下面的界面, 按流程下载相应的工具.

![](http://i68.tinypic.com/2cna5ns.jpg)

![](http://i63.tinypic.com/25piky8.jpg)

![](http://i64.tinypic.com/2hpp20g.jpg)

在 Windows Host 下根据你的 VS 下载合适的版本(要下载 OpenGL 版本).

最后下载 VS 插件.

![](http://i66.tinypic.com/2mhhfnn.jpg)

全部下载好后, 按顺序安装就行了.

环境设置:

在系统环境变量 Path 中添加QT的Bin目录:C:\Qt4.8.2\bin（安装路径因人而异）可能需要重启.

Qt Creator 设置:

打开Qt Creator,菜单"工具"--》"选项",<br>在打开的对话框里选左边的"构建和运行",<br>右边选"Qt版本", 点击添加, 找到你之前安装的Qt文件夹里的bin子文件夹, 找到qmake.exe, 然后点击确定, 这样就设置好了.

VS 设置:

![](http://i66.tinypic.com/s3lv1z.jpg)

![](http://i67.tinypic.com/dmcieh.jpg)

msvc2010_opengl

D:\Development\Qt5.3.2\5.3\msvc2010_opengl

在vs中新建项目

![](http://i65.tinypic.com/58c9i.jpg)

![](http://i65.tinypic.com/20prls6.jpg)

![](http://i63.tinypic.com/m9putc.jpg)

![](http://i66.tinypic.com/2ppnbc9.jpg)

后面两个复选框, 第一个是给应用程序添加默认图标, 第二个是添加预编译头.

最后需要设置QT工程版本, 这个很重要(一般是默认设置好的, 最好还是检查下), 设置好以后就不用再设置引用库路径等东西.

项目右键设置.

![](http://i68.tinypic.com/313kw9c.jpg)

![](http://i64.tinypic.com/a9r969.jpg)

设置好后, 此时还是提示包含库不对:

![](http://i66.tinypic.com/5aqt6q.jpg)

编译一下, 再关闭 VS 重新打开就正常了.

![](http://i68.tinypic.com/dd1cvo.jpg)
