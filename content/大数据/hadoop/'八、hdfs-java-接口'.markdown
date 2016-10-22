author: Martin
date: 2016-01-19 21:07
title: (八)、HDFS Java 接口

环境:<br>windows 7<br>eclipse

先在 windows 7 下搭建好 eclipse 项目环境, 参考 [安装 Eclipse](http://www.smallcpp.cn/'%E5%9B%9B-%E5%AE%89%E8%A3%85-eclipse'.html)

新建 hadoop 工程, 新建个 lib 文件夹, 导入 hdfs 的相关 jar 包:

- /usr/itcast/hadoop-2.7.1/share/hadoop/common
- /usr/itcast/hadoop-2.7.1/share/hadoop/common/lib
- /usr/itcast/hadoop-2.7.1/share/hadoop/hdfs

测试 hdfs 导入这些目录下的 jar 就可以了…

选中导入后所有的 jar 包, 右键 [构建路径] -> [添加到构建路径]

![](http://i59.tinypic.com/2m43bex.jpg)

接下来, 设置下 eclipse 的自动提示.<br>window –> Preferences –> Java –> Editor –> Content Assist:

![](http://i60.tinypic.com/1zoj2no.jpg)

abcdefghijklmnopqrstuvwxyz.

接下来直接上源码好了:

```java
package cn.itcast.hadoop.hdfs;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URI;
import java.net.URISyntaxException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.junit.Before;
import org.junit.Test;


public class HDFSDemo {
    FileSystem fs = null;

    // 链接 hdfs
    @Before
    public void init() throws IOException, URISyntaxException, InterruptedException {
        // 首先创建  FileSystem 的实现类(工具类) -- 用来操作 hdfs
        fs = FileSystem.get(new URI("hdfs://192.168.31.200:9000"), new Configuration());
    }

    // 上传文件
    public void testUpload() throws IllegalArgumentException, IOException {
        InputStream in = new FileInputStream("C:\\Users\\Public.Public-PC\\Desktop\\test.txt");
        OutputStream out = fs.create(new Path("/test.txt"));
        IOUtils.copyBytes(in, out, 4096, true);
    }

    // 另一种方式 下载文件
    @Test
    public void testDownload() throws IllegalArgumentException, IOException {
        fs.copyToLocalFile(new Path("/words.txt"), new Path("C:\\Users\\Public.Public-PC\\Desktop\\words.txt"));
    }

    // 删除文件
    public void testDelete() throws IllegalArgumentException, IOException {
        fs.delete(new Path("/test.txt"), true);
    }

    // 下载文件
    public static void main(String[] args) throws IOException, URISyntaxException {
        // TODO Auto-generated method stub
        InputStream in = fs.open(new Path("/words.txt"));
        OutputStream out = new FileOutputStream("C:\\Users\\Public.Public-PC\\Desktop\\words.txt");
        IOUtils.copyBytes(in, out, 4096, true);
    }

}
```

当我们上传文件时, 可能会报权限不足的错误, 此时, 需要去 linux 里修改下 hdfs 的配置.<br>进入 sbin vim hdfs-site.xml
```xml
<property>
    <name>dfs.permissions</name>
    <value>false</value>
</property>
```
不过, 这种方式总感觉不安全, 期待以后有更好的方法.

另外, 可以在 hadoop 官网上下载它的源码, 添加到 eclipse 里关联起来.
