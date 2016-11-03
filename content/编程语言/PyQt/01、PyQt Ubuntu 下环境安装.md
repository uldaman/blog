Title: 01、PyQt Ubuntu 下环境安装
Author: Martin
Date: 2016-04-26 19:04
Summary: Qt 4.8.7 + Python 2.7 + PyQt 4.11 + Eric6 安装简介

注意, 我在 Ubuntu 低版本下安装这个环境有点问题, 在最新版本下正常... 所以安装前还是请大家升级自己的 Ubuntu 系统吧.

[TOC]

# 说明
PyQt 是 Riverbank Computing 公司开发的, 到 [Riverbank Computing](https://www.riverbankcomputing.com/news) 的官网上就能下载 PyQt 了.

![](http://i63.tinypic.com/2lo6k5t.jpg)

不过这里要注意下版本, 因为我们是用的 Python 2 系列, 而 Python 2 系列只支持到 PyQt 4, 而 PyQt 4 又只支持的是 QT 4.8, 所以我们的环境就成了:<br>
__Python 2.7 + PyQt 4.11 + Qt 4.8.7__

# Qt 4.8.7
下载: [qt-everywhere-opensource-src-4.8.7.tar.gz](http://share.weiyun.com/97b8d2b831fec5c13cccb2880490b050)

这个版本的 Qt 貌似从官网上下不到了, 官网上的是 qt-everywhere-enterprise-src-4.8.7.tar.gz, 这个版本安装时需要一个 Licenses ... 我试了下还是有点问题, 所以网上找了个开源版本共享在我的云盘上.

下载下来后, 解压并在 Shell 中进入该文件夹, 依次执行下面的命令:

```shell
~/Downloads/qt-everywhere-opensource-src-4.8.7$ sudo ./configure
~/Downloads/qt-everywhere-opensource-src-4.8.7$ sudo make
~/Downloads/qt-everywhere-opensource-src-4.8.7$ sudo make install
```
<br>
安装好后, Qt 的默认路径是 `/usr/local/Trolltech/Qt-4.8.7/`, 可以在执行第一条命令时指定安装目录 `./configure --prefix=/usr/local`

过程是漫长的, 耐心等待...

接下来配置__环境变量__:

```shell
sudo vi ~/.bashrc
```
<br>
打开文件后, 在结尾处添加以下内容:

```
export QTDIR=/usr/local/Trolltech/Qt-4.8.7
export LD_LIBRARY_PATH=${QTDIR}/lib:${LD_LIBRARY_PATH}
export PATH=${QTDIR}/bin:${PATH}
```
<br>
然后刷新下 bashrc:

```shell
source ~/.bashrc
```
<br>
测试是否安装成功:

```shell
qmake -v
QMake version 2.01a
Using Qt version 4.8.7 in /usr/local/Trolltech/Qt-4.8.7/lib
```
<br>
输入 `qmake -v` 后如果出现上面的内容就表示 Qt 安装好了...

# SIP
SIP 是python 调用 C/C++ 库的必备模块, 是 PyQt 的依赖工具, 所以安装 PyQt 之前必须先安装 SIP.

PyQt 编译时使用的 SIP 版本__必须__与 python 默认调用的 SIP 保持一致!<br>
否则 python 中是无法调用 PyQt 的, 测试方法如下:

分别在终端输入:

```shell
sip -V
```
<br>
在python3环境输入：

```python
import sip
print(sip.SIP_VERSION_STR)
```
<br>
查看二者显示的版本是否一致, 如不一致, 删除 python 的 dist-packages 目录下 sip 的相关文件:

```shell
sudo rm -rf /usr/lib/python2.7/dist-packages/sip*
```
<br>
然后再开始开安装.

首先去 [Riverbank Computing](https://www.riverbankcomputing.com/software/sip/download) 下载 SIP 安装包.

下载下来后, 解压并在 Shell 中进入该文件夹, 依次执行下面的命令:

```shell
sudo python configure.py
sudo make
sudo make install
```
<br>
安装结束后, 再用之前的方法测试下.

# PyQt 4.11
先去下载安装包 [Riverbank Computing](https://www.riverbankcomputing.com/software/pyqt/download)

下载下来后, 解压并在 Shell 中进入该文件夹, 依次执行下面的命令:

```shell
sudo python configure.py
sudo make
sudo make install
```
<br>
如果 `sudo python configure.py` 时提示找不到 qmake 编译器, 可以用面这条命令来指定 qmake:

```shell
sudo python configure.py -q /usr/local/Trolltech/Qt-4.8.7/bin/qmake
```
<br>
安装完后测试下:

```
import PyQt4
```
<br>
如果不报错就说明安装好了...

# QScintilla
QScintilla 是连接编译器和 Python 的接口, 是 __Eric__ 的必需前置组件.

先去下载安装包 [Riverbank Computing](https://www.riverbankcomputing.com/software/qscintilla/download)

下载下来后, 解压并在 Shell 中进入该文件夹, 依次执行下面的命令:

```
cd QScintilla-gpl-2.9.2

cd Qt4Qt5
qmake qscintilla.pro
sudo make
sudo make install

cd ../designer-Qt4Qt5
qmake designer.pro
sudo make
sudo make install

cd ../Python
python configure.py
sudo make
sudo make install
```
<br>
# Eric6
去官网下载 [Eric6](http://eric-ide.python-projects.org/eric-download.html) 安装包:

- ic6\-6.1.4.tar.gz
- eric6\-i18n\-zh_CN\-6.1.4.tar.gz

下载好后都解压下, 依次执行:

```shell
cd ic6-6.1.4
sudo python install.py

cd ../eric6-i18n-zh_CN-6.1.4
sudo python3 install-i18n.py
```
<br>
安装好后, 运行 eric6:

```
sudo eric6
```
<br>
__注意:__ 为避免 Eric6 写入配置文件时权限不足, 要用 `sudo` 来运行 eric6.

也可以将当前用户的 eric6 目录权限设置为可读写:

```
sudo chmod a+w -R ~/.eric6
sudo chmod a+w -R ～/.config/Eric6
```
<br>
然后就可以不用 `sudo` 来运行 eric6 了.
