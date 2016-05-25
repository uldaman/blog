author: Martin
date: 2015-06-11 12:12
title: (三) Hello World

步骤：

1、将代码编写到扩展名为 .java 的文件中.

2、通过 Javac 命令对该 java 文件进行编译.

3、通过 java 命令执行生成的 class 文件.

新建一个 txt 文件, 然后改名为 HelloWorld.java, 用记事本打开该文件, 输写代码:

    <span style="color: #0000ff">public</span> <span style="color: #0000ff">class</span> HelloWorld { <span style="color: #008000">//</span><span style="color: #008000"> 此处要与文件名相同</span>
        <span style="color: #0000ff">public</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">void</span><span style="color: #000000"> main(String[] args) {
            System.out.println(</span>"Hello World!"<span style="color: #000000">);
        }
    }</span>




然后打开命令提示符, 按下图演示步骤输入:
![](http://i58.tinypic.com/15hfvgg.jpg)
(我的文件是在桌面新建的)




简单分析下这个 HelloWorld:




![](http://i60.tinypic.com/314vxu9.jpg)


类是 Java 中的基本单元, 可以在类中定义变量和函数, 同时 Java 也规定了, 所有的变量和函数必须存在于类中.


Java的主函数: **main** (和 C 差不多)
如果没有 main, 执行 class 文件时, 会出现提示: 缺少一个名称为 main 的方法.
main 是一个程序的入口, 代码为:
public static void main(String[] args)
此为固定写法.


注释: Java 中的注释基本和 C/C++ 类似, 但 java 有个特殊, 在文件开头:



    <span style="color: #008000">/**</span><span style="color: #008000">
    *
    *注释内容
    *
    </span><span style="color: #008000">*/</span>




这叫“文本注释”, 对程序进行说明后, 通过 JDK 中另一个工具 javadoc.exe, 将文档注释提取出来形成一个网页——程序说明书.
  >
