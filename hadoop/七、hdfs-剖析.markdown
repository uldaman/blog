author: Martin
date: 2016-01-19 21:06
title: (七)、HDFS 剖析

NameNode -- 管理节点

DataNode -- 存储节点

Secondary NameNode -- NameNode 助手 (hp 1.0)

#1. Client
机架感知, 数据就近原则, 因为数据是分布式存储的, Client 会感知最近那个 DataNode 取数据.

#2. Metadata(元数据)
存储细节: 为了安全, Metadata 在 HDFS 中会存储两份, 内存一份, 磁盘一份(镜像)<br>/test/a.log, 3 ,{blk_1,blk_2}, [{blk_1:[h0,h1,h3]},{blk_2:[h0,h2,h4]}], 这几项分别是:<br>文件名、副本数、文件被分多少块以及每个块分别被保存在哪个 DataNode 上.<br>HDFS 通过 CRC 校验 块的完整性.<br>为了速度, metadata 始终保存内存中, 为了安全, 它会在磁盘中再创建一份镜像.

#3. NameNode -- 管理节点
*. 维护 文件目录树、文件/目录的元信息、每个文件对应的数据块列表<br>*. 接收用户的操作请求

NameNode 的文件包括:

- fsimage: 元数据镜像文件(即 磁盘上的文件), 存储某一时候 NameNode 的内存元数据信息
- edits: 操作日志文件
- fstime: 保存最近一次 checkpoint 的时间 (还原点)

这些文件保存在之前设置的 tmp 文件夹中.

"写": NameNode 首先向写 editlog 到磁盘, 即向 edits 文件中写日志, 成功返回后, 才会修改内存, 并且向客户端返回.

Hadoop 会维护一个 fsimage 文件, 也就是 NameNode 中 metadata 的镜像,<br>但是 fsimage 不会随时与 NameNode 内存中的 metedata 保持一致,<br>而是每隔一段时间通过合并 edits 文件来更新内容(仅限 1.0 和 伪分布式, 2.0 集群是实时的), edits 合并后就会进行一次清空.<br>Secondary NameNode 就是用来合并 fsimage 和 edits 文件来更新 NameNode 的 metedata 的.

#4. Secondary NameNode
(1.0 和 伪分布式才有, 2.0 集群中是没有的)<br>HA 解决方案 (高可)

工作模式:<br>从 NameNode 下载元数据信息(fsimage, edits), 然后合并二者, 生成新的 fsimage, 在本地保存一份后推送到 NameNode, 替换旧的 fsimage.

![](http://i57.tinypic.com/1zpi04p.jpg)

什么时候同步?<br>1. fs.checkpoint.period 指定两次 checkpoint 的最大时间间隔, 默认 3600 秒<br>2. fs.checkpoint.size 规定 edits 的大小, 默认 64M

#5. DataNode
真实文件数据存储服务<br>文件块(block): 最基本存储单位, hp 1.0 默认 64M, hp 2.0 默认 128M, 从文件的 0 编号开始, 按指定大小, 顺序对文件进行划分并编号.<br>HDFS中, 如果一个文件小于一个数据块的大小 , 并不占用整个数据块 (这些文件最终被保存在 tmp/dfs/data/current/.../finalized/ 中).<br>默认 3 个副本 (如果已存在一份存储好的文件(3个副本), 突然有一个小弟挂掉了, NameNode 会再安排另一个小弟重新备份这个文件, 这是基于心跳包机制的).
