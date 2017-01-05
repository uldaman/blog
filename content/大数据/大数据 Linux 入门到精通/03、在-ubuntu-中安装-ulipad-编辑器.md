author: Martin
date: 2015-03-26 17:04
title: 03. 在 Ubuntu 中安装 Ulipad 编辑器

Ulipad 是一个国人编写的专业 Python 编辑器, 它基于 wxpython 开发的GUI(图形化界面).
好吧, 有人说 vim, 我承认它确实是神器, 但上手实在是有点蛋疼…以后有机会使用的时候再学吧…

# 安装

在安装之前, 有必要确认下我们 Ubuntu 上的 Python 是否正常.
打开终端, 输入 python –V (注意大小写, 是大写的 V).

![](http://i61.tinypic.com/1zovrsl.jpg)

如果正常输出了 Python 版本号, 就可以开始安装 Ulipad 了.

1. 用 goolge 搜索 ulipad 或者 直接进入 [http://code.google.com/p/ulipad/](http://code.google.com/p/ulipad/)
点击 Downloads, 下载最新的 zip 压缩包(为了访问 google, 你可能需要做点什么…总之, 你懂的).

![](http://i57.tinypic.com/1z36t93.jpg)

↓↓↓↓

![](http://i58.tinypic.com/mm7lg7.jpg)

2. 右键选择复制链接地址.

![](http://i58.tinypic.com/wrxkrs.jpg)

3. 打开终端, 输入 wget 链接地址, 回车开始下载文件.

![](http://i62.tinypic.com/1zdomyc.jpg)

4. 下载好后, 输入 ls 命令查看下当前文件夹下的文件, 可以看到多了 ulipad.4.1.zip, 接着输入 unzip ulipad.4.1.zip 解压文件.

![](http://i58.tinypic.com/6895d0.jpg)

5. 用 cd 命令进入刚解压出来的文件夹, 接着用 ls 命令查看文件.

![](http://i60.tinypic.com/im8g42.jpg)

6. 我们要执行的是 Ulipad.py 文件(注意大小写), 输入命令 python Ulipad.py .
此时它会报错, 说没有导入 wx 模块, 前面说过: Ulipad 是基于 wxpython 开发的GUI(图形化界面). 所以我们要给 Ubuntu 安装 wxpython 库. 只需要一句命令:
sudo apt-get install python-wxgtk2.8
等它安装会后, 再输入 python Ulipad.py 就能打开 Ulipad 编辑器了.

![](http://i62.tinypic.com/5yvrk9.jpg)

7. 现在开始对 Ulipad 进行一下配置, 打开参数设置.

![](http://i61.tinypic.com/f0u6qf.jpg)

Linux 下只要注意制表符设置就可以了, 其它默认即可.

![](http://i57.tinypic.com/23h0zkl.jpg)

![](http://i62.tinypic.com/2nvaxc5.jpg)

8. 接下来打开目录浏览.

![](http://i58.tinypic.com/sobqkn.jpg)

添加新的目录

![](http://i57.tinypic.com/2nsq1wg.jpg)

定位到用户目录下, 点击右上角创建文件夹, 命名为 workspace, 最后点击右下角打开, 在弹出的对话框里勾上 Python 再点击确定.

![](http://i60.tinypic.com/xola8i.jpg)

![](http://i62.tinypic.com/28mjr6t.jpg)

9. 现在来测试下设置好的环境.
在目录浏览窗口右键--新建文件, 命名为 hello.py.

![](http://i59.tinypic.com/wld9ur.jpg)

![](http://i58.tinypic.com/21kxxlg.jpg)

输入 print “123”后, ctrl + s 保存, 如果代码写错了, 例如写成少打一个引号, 这时下面会弹出语法检查窗口.
可以去掉下面 在_Python程序运行进入PEP8风格检查_ 的勾.

![](http://i61.tinypic.com/2q88tud.jpg)

当我们写好代码后, 点击右上角的运行按钮或者按F5键就能运行脚本了.

![](http://i61.tinypic.com/729kya.jpg)

10. 最后为了方便以后打开 Ulipad, 将快捷方式添加到 '应用程序'

```
sudo gedit /usr/share/applications/Ulipad.desktop
```
<br>
然后在里面添加如下内容:

```
[Desktop Entry]
Name=Ulipad
Comment=a Python IDE
Exec=python /home/zgf/py/ulipad/UliPad.py
#图标
Icon=/home/zgf/py/ulipad/ulipad.ico
Terminal=false
Type=Application
Categories=Application;Development;
```
<br>
保存后, Ulipad 就会出现在'应用程序'里面:

![](http://i64.tinypic.com/15i0osn.jpg)

然后把它锁在侧边栏:

![](http://i59.tinypic.com/vq5vf7.jpg)
