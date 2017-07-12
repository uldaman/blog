author: Martin
date: 2016-01-19 21:02
title: (三)、配置 SecureCRT、SSH 及 ShadowSocks

为方便操作, 我们为 ubuntu 安装上 SecureCRT、SSH 及 ShadowSocks

SecureCRT 参考: [传送门](http://blog.smallcpp.cn/si-securecrt-de-an-zhuang-he-shi-yong.html)

**配置 SSH 免密码**

cd ~<br>进入根目录

ls -la<br>查看下当前目录文件, 可以看到有个隐藏的 .ssh 文件夹 (点开头就是隐藏的)

cd .ssh/<br>进入 .ssh 目录, ls 一下, 看看该目录下有没有 id_rsa、id_rsa.pub 两个文件, 如果没有, 就生成一对:
ssh-keygen -t(加密类型) rsa<br>--四个回车--<br>然后就会在 .ssh 下生成两个文件 id_rsa、id_rsa.pub

cp id_rsa.pub authorized_keys<br>此时不需要密码就能启动/停止 hadoop 了...

如果要向其他主机发送自己的公钥: ssh-copy-id xxx(ip)

**ShadowSocks**

1. 安装图形界面客户端:<br>sudo add-apt-repository ppa:hzwhuang/ss-qt5<br>sudo apt-get update<br>sudo apt-get install shadowsocks-qt5

2. 使用

![](http://i62.tinypic.com/2wcnwy1.jpg)

![](http://i62.tinypic.com/jjlamt.jpg)

![](http://i58.tinypic.com/10psqyp.jpg)

**将下来, 打开 firefox.**

![](http://i59.tinypic.com/4ift35.jpg)

![](http://i57.tinypic.com/2s6udkp.jpg)

![](http://i60.tinypic.com/33cyi5k.jpg)
