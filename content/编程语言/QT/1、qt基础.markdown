author: Martin
date: 2015-02-15 14:08
title: 1、QT基础

# QT是什么?

  1. 一个基于C++语言的框架(就是封装了很多类库, 我们可以直接拿来用)
  2. 一个专注于用户图形界面的框架
  3. 一个跨平台的框架

QT不仅仅是 GUI 组件. 使用 Qt, 在一定程度上你获得的是一个"一站式"的解决方案: 不再需要研究 STL, 不再需要 C++ 的<string>, 不再需要到处去找解析 XML、连接数据库、访问网络的各种第三方库, 因为 Qt 自己内置了这些技术.

# QT的主要工具

qmake : 可以把 C++ 的代码文件组织成一个 .pro 文件(QT的工程文件), 继续生成 Makefile 文件(编译文件)

qmake –v : 查看 qmake 的版本

qmake –project : 生成 .pro 的命令

make : 根据生成的 Makefile 文件编译连接, 生成可执行文件

assistant : Qt 的帮助手册

designer : 设计器, 用于设计界面, 设计出来的文件以 .ui 为后缀(就是用来拖拽控件的...)

uic : 用于把 .ui 文件转换成.h文件

qtcreator : Qt 的集成开发环境

# 编写Qt程序的流程(了解下就行, 我们将使用 vs + Qt 方式编程)

编写 .cpp 文件

使用 qmake –project 生成项目描述文件(.pro)

使用 qmake 生成 Makefile 文件

使用 make 生成可执行文件

注意: 任何一个 Qt 程序都要看作成工程, 放在一个单独的文件夹中.

当然这是 Qt 本身的编写流程, 我们在 windows 下开发, 可以和 vs 结合起来, 那将方便很多.

??
