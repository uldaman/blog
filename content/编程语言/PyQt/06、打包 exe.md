Title: 06、打包 exe
Author: Martin
Date: 2016-05-12 23:27
Summary: 利用 py2exe / pyinstaller 将开发好的 PyQt 程序打包成 exe 发布.

[TOC]

> 在使用时发现, 64 位的 py2exe 没办法打包成一个 exe 文件, 会生成很碰依赖文件, 而且实战中还发现其他问题, 推荐使用 pyinstaller 去打包 exe, 使用非常简单, 如果不想显示 console, 并且打包成一个单独的 exe 文件, 那就加两个参数:<br>
> pyinstaller app.py --noconsole --onefile

# 使用 py2exe
## 一、简介
py2exe 是一个将 python 脚本打包成 windows 上的可独立执行的可执行程序 (*.exe) 的工具, 这样, 就可以不用装 python 而在 windows 系统上运行这个可执行程序.

## 二、安装
从 [http://prdownloads.sourceforge.net/py2exe](http://prdownloads.sourceforge.net/py2exe) 下载并安装与当前系统匹配的 py2exe 安装程序, 这将安装 py2exe 和相应的例子, 这些例子被安装在 `lib\site-packages\py2exe\samples` 目录下.

## 三、应用
我们将一节笔记中做好的 **first_window** 程序打包成 exe.

在 **first_window** 目录下新建一个 py 文件, 名字随意 (我这里就取名为 `exe.py` 了), 填充以下内容:

```python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

options = {
    'py2exe': {
        'dll_excludes': ['MSVCP90.dll'],  # py2exe 会提示 MSVCP90.dll: No such file or directory, 要么将 windows 目录下的 MSVCP90.dll 拷到 python 安装目录下, 要么就在这里配置下
        'includes': ['sip'],  # py2exe 打包 pyqt 程序时不会带上 sip, 手动指定下
        'bundle_files': 1,  # 打包成一个 exe 程序, 否则会在生成一堆依赖 dll、pyd 文件, 只支持 32 位 python
        'compressed': 1,  # 启用压缩
        'optimize': 2  # 2级优化
    }
}

setup(
    version = '1.0.0',  # exe 版本
    description = 'description for your exe',  # 文件说明 (在 exe 属性里显示的)
    name = 'name for your exe',  # 产品名称 (不是 exe 文件名, 是在 exe 属性里显示的)
    options =  options,
    zipfile = None, # 不生成zip库文件
    windows = ['first_window.py'],  # 如果是窗口程序就用 windows, 控制台程序就用 console
    )
```
<br>
然后控制台进入 **first_window** 目录, 执行命令: `python exe.py py2exe`, 系统就开始打包了, 打包完成后会生成一个 `dist` 目录, 这里存放 exe 文件.

开发 pyqt 程序时, 可能会产生多个 py 文件, 只需要在打包脚本中指定**入口文件**就可以了, py2exe 会自动分析依赖, 但并不是绝对的, 例如 sip 包就不会被自动带上, 所以这里就需要我们在 `includes` 中配置.<br>
另外, 也可以在 options 的 `packages` 参数里配置, 让 py2exe 在打包时把 package 打包进去 (包名就是 `__init__.py` 所在的目录名), 效果和 `includes` 一样.

```python
options = {
      'py2exe': {
        'packages': ['first_window']
    }
}
```
<br>
# 使用 pyinstaller
## 一、初识
用过 pyinstaller 之后的第一感觉就是相见恨晚, 有这么好用的打包程序, 谁 tm 还用 py2exe, 全程根本不需要手工指定 include 哪些包、哪些 dll 应该被包含, 哪些不该包含, 全都自动实现, 基本剩我们只需要执行如下代码就可以了:

```
pyinstaller app.py
```
<br>
如果不想显示 console, 并且打包成一个单独的 exe 文件, 那就加两个参数:

```
pyinstaller app.py --noconsole --onefile
```
<br>如果你只引用了很少的资源, 你可以这样简单的打包程序在系统中的显示图标
## 二、打包所有静态资源
Qt 本身在资源管理器的资源是可以直接打包入程序中, 不需要做什么处理的, 但有时可能需要在程序中调用一些外部资源文件, 此时 pyinstaller 就不能帮我们自动打包了..

我们可以先用如下的命令去打包一次程序:`pyinstaller app.py --noconsole --onefile -i icon.ico`<br>
这里的 **\-i** 参数就是给程序添加在资源管理器中显示的图标, 打包完之后会在同目录下生成一个 **app.spec** 文件,我们可以通过编辑这个 **app.spec** 文件来把其他资源文件打包进 exe 文件里.

假设我们程序的里有一个图标叫 title\_bar.ico, 我们修改 spec 文件如下 (先把 **task\_bar.ico** 放在同目录下):

```js
a = Analysis([
                datas=[('task_bar.ico','.')]
            ])
```
<br>
这样就把 **task\_bar.ico** 文件打包进 exe 文件了, 每次执行 exe 文件的时候都会把这个 icon 解压到一个临时目录中供调用.

现在的问题在于, 这个临时目录的路径是不固定的, 那么我们在程序中要如何寻找这个临时目录里的资源文件呢?

pyinstaller 通过给 sys 模块提供一个 `sys._MEIPASS` 的参数来告知这个临时目录的路径.

现在我们可以写这样一个函数来保证在 python 源码运行模式和 pyinstaller 打包模式都正常获取资源文件的路径:

```python
def resource_path(rel_path='icon.ico'):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)
```
<br>
当以 python 源码运行时就获取当前的路径, 打包后运行时就获取临时目录的路径, 这样我们在 pyqt 中的 icon 设置代码就变成了:

```python
icon_file = resource_path('icon.ico')
window = MyApp()
window.setWindowIcon(QtGui.QIcon(icon_file))
```
