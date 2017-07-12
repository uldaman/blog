author: Martin
date: 2015-04-03 15:48
title: 08. Linux 的权限控制

首先,
Linux 中的每个文件都有 所有者、所在组、其它组 三种权限.

**所有者**
一般让文件的创建者, 谁创建了该文件, 谁就是该文件的所有者.
用 ls -ahl 可以看到文件的所有者.
也可以用 chown 用户名 文件名 来修改文件的所有者.

**所在组**
当某个用户创建了一个文件后, 该文件的所在组就是该用户所在的组.
用 ls -ahl 可以看到文件的所在组.
也可以用 chgrp 组名 文件名 来修改文件的所在组.

**其它组**
除开文件的所有者和所在组的用户外, 系统的其它用户都文件的其它组.

usermod -g 组名 用户名 指定用户某个组中.
usermod -d 目录名 用户名 改变该用户登陆的初始目录.

在终端输入 ls –l 查看当前目录详情:
![](http://i59.tinypic.com/2d165c9.jpg)

每行前面的第一段(例如:drwxr-xr-x)就是文件权限的描述.

拿 drwxr-xr-x 这段做例子, 它实际被分为 4 部分.
[![image](http://www.smallcpp.cn/wp-content/uploads/2015/04/image_thumb.png)](http://www.smallcpp.cn/wp-content/uploads/2015/04/image.png)
不过在说这个之前, 先说一下 r w x 的意思:
r 表示 read 权限
w 表示 write 权限
x 表示 可执行 权限

第一个 d, 表示文件的类型, 如果是 d 表示目录, - 表示文件;

第二个 rwx, 表示所有者的权限;

第三个 r-x, 表示所在组的权限;

第四个 r-x, 表示其它组的权限.


使用 chmod 命令可以更改指定文件的权限(chmod 权限 文件名).
不过需要注意的是, 在 chmod 中权限是用数字来表示的, r 是 4, w 是 2, x 是 1.
rwx : 4+2+1 = 7
r-x : 4+1 = 5
r-x : 4+1 = 5
ap<
