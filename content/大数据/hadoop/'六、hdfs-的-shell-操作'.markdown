author: Martin
date: 2016-01-19 21:05
title: (六)、HDFS 常用 shell 操作

[http://yunpan.cn/cHVRtwWCBpHC6](http://yunpan.cn/cHVRtwWCBpHC6)  访问密码 4624

hadoop fs -ls hdfs://itcast01:9000/, 可简写成 hadoop fs -ls / 表示根目录 -R 递归查看 -h 简化大小显示

hadoop fs -copyFormLocal <本地文件> 类似 put

hadoop fs -cp

hadoop fs -moveFormLocal <本地文件> 剪切本地文件到 hdfs 上

hadoop fs -mv

hadoop fs -cat 查看文件内容 (| more 分页)

hadoop fs -copyToLocal <本地文件> 类似 get

hadoop fs -moveToLocal <本地文件> 剪切hdfs文件到 本地

hadoop fs -count <目录> 统计目录文件数量 (文件夹数量(含根目录) 文件数量 总大小)

hadoop fs –rm <文件> 删除文件 -r <目录> 删除目录

hadoop fs –mkdir <目录> 创建目录

hadoop fs –tail <文件> 查看文件结尾内容

hadoop fs -chmod 改变权限 -R 递归修改

hadoop fs -chown 改变用户

hadoop fs -chgrp 改变用户组

hadoop fs –chown <组:用户> 同时改变用户组和用户

在 hadoop 中, hdfs 的操作被单独分离出来了, 可以这样调用: **hdfs dfs** -ls /
