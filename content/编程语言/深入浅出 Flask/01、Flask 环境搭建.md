Title: 01、Flask 环境搭建
Author: Martin
Date: 2016-03-30 20:17
Summary: 简单介绍下 Flask, 及其环境搭建

[TOC]

# 虚拟环境
## 安装 virtualenv
```
pip install virtualenv
```
<br>

## 创建 venv
```
virtualenv [指定虛擬環境的名稱]
```
<br>
使用该命令创建的环境会依赖系统环境中的 site packages, 就是说系统中已经安装好的第三方 package 也会安装在虚拟环境中, 如果不想依赖这些 package, 那么可以加上参数 --no-site-packages 建立虚拟环境.

```
virtualenv --no-site-packages [指定虛擬環境的名稱]
```
<br>

推荐使用 __--no-site-packages__, 这样就可以得到干净的 python 环境了.

## 启动 venv
```
source ./bin/activate (linux)
Scripts\activate (windows)
```
<br>

如果启动成功, 那么命令行前面就什么多了(__虛擬環境的名稱__)标识, 此时就可以在虚拟环境里进行操作了,
如安装项目依赖包等.

通过下面的命令, 可以查看当前已安装了哪些第三方包

```
pip list
或者
pip freeze
```
<br>

这里我们先安装下 __Flask__:

```
pip install flask
```
<br>

## 退出 venv
```
bin/deactivate (linux)
Scripts\deactivate (windows)
```
<br>

## 移植环境
```
pip freeze > requirements.txt 将当前环境的包依赖信息保存在 requirements.txt 文件
pip install -r requirements.txt 会自动从网上下载并安装所有包
```
<br>

# 安装 Eclipse + PyDev打开Eclipse，Help–>Install new software
## 安装 Eclipse
Eclipse 的安装见 [http://www.smallcpp.com/028-eclipse.html](http://www.smallcpp.com/028-eclipse.html)

## 安装 PyDev
打开 Eclipse, Help –> Install new software

点击 "__Add__", 名字: __PyDev__, 地址: __http://pydev.org/updates__ (这个地上好像不行, 然后我用浏览器直接访问这个地址, 它提示: Nothing to see here (this is just a dummy link to be redirected to https://dl.bintray.com/fabioz/pydev/4.5.5), 于是我把地址改成 __https://dl.bintray.com/fabioz/pydev/4.5.5__ 就可以了.)

接下来, Eclipse 列出了两个插件: __PyDev__ 和 __PyDev Mylyn Integration__(官网上说是一个任务或者应用程序生命周期管理的工具, 没什么用, 不用安装这个)

选中 __PyDev__ 插件后, 一路下一步.

最后重启 Eclipse 后, 验证是否安装成功, 打开 Eclipse–\>File–\>New-\>Project, 若 __PyDev__ 项存在即为可用.

![](http://i66.tinypic.com/a23r4l.jpg)

## 配置 Flask
配置 Python 解释器来到 virtualenv:<br>
Window –\> Preferences –\> PyDev \> Interpreters \> Python Interpreter

New –\> 选择安装目录

![](http://i68.tinypic.com/ws2rnb.jpg)

Eclipse 会自动分析出当前依赖 Libraries.

最后在 __Forced Builtins__ 选项卡中, 新建 __flask.ext__ 项即可.

![](http://i65.tinypic.com/acvgat.jpg)

# Flask 项目框架搭建
## 新建 Python 项目
File \-\> New \-\> PyDev Project

## 新建架构文件夹
![](http://i66.tinypic.com/xbt6o.jpg)

```
app – 根目录
　　static – 静态资源目录，图片，js，css等
　　templates – 模板
　　_init_.py – 初始化脚本
　　views.py – 视图控制器
tmp – 临时文件夹
run.py – 项目启动程序
```
<br>

## 编写 Hello World

__\_init\_.py__ 创建 Flask 实例

```python
from flask import Flask
app = Flask(__name__)
```
<br>

__run.py__ 创建启动脚本

```python
from app import app
from app import views

app.run(debug = True)
```
<br>

__views.py__ 编写视图函数

```
from app import app

@app.route("/")
def index():
    return "hello,world!"
```
<br>
