author: Martin
date: 2016-01-19 21:00
title: (一)、认识 hadoop

hadoop不是一个英文单词, 是作者(Doug Cutiing)发明的词, hadoop名称来源作者小孩的一个絨毛填充黄色大象玩具.
它的发音是：[hædu:p] -- 嗨都泼

hadoop不是一个英文单词, 是作者(Doug Cutiing)发明的词, hadoop名称来源作者小孩的一个絨毛填充黄色大象玩具. 它的发音是：[hædu:p] – 嗨都泼

对于 hadoop 2.0 来说, 它的核心有三部分: HDFS、MapReduce 和 YARN, 其中 YARN 是 2.0 新加的, 它是为了解决 MapReduce 的缺陷, 有了它, hadoop 就可以很好的兼容 storm、spark等等框架.

理解下相关的关键字含义:
- HDFS: 简单的理解成一种文件格式, 类似 FAT32、NTFS 这种.
- MapReduce: 离线计算模型.
- YARN: 资源协调者.
- Storm: 流式计算模型.
- Spark: 内存计算模型.
- Hive: 数据仓库工具, 它是为了简化编写 MapReduce.
- HBse: 一种分布式、面向列的开源数据库, 可以很好的使用在 HDFS 上.

![HDFS](http://i62.tinypic.com/2ex55ih.jpg)

![架构](http://i61.tinypic.com/t866c1.jpg)
