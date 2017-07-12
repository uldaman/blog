author: Martin
date: 2015-02-15 14:11
title: 3、Hello qt

按上一篇的内容, 新建一个 VS Qt 工程.

[![image](http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb16.png)](http://www.smallcpp.cn/wp-content/uploads/2015/02/image16.png)

main.cpp 里是程序的入口, 里面只有一个 main 函数, 它维护一个 Qt 对象实例.

    #include <span style="color: #800000">"</span><span style="color: #800000">demo.h</span><span style="color: #800000">"</span><span style="color: #000000">
    #include </span><QtWidgets/QApplication>

    <span style="color: #0000ff">int</span> main(<span style="color: #0000ff">int</span> argc, <span style="color: #0000ff">char</span> *<span style="color: #000000">argv[])
    {
        QApplication a(argc, argv);
        Demo w;
        w.show();
        </span><span style="color: #0000ff">return</span><span style="color: #000000"> a.exec();
    }</span>




对于 Qt 程序来说, `main()`函数一般以创建 application 对象开始(GUI 程序是`QApplication`, 非 GUI 程序是`QCoreApplication`, `QApplication`实际上是`QCoreApplication`的子类),后面才是实际业务的代码. 这个对象用于管理 Qt 程序的生命周期、 开启事件循环.







而 demo.h 里是我们 Qt 程序的界面类, 它继承于 QWidget类, 它是 Qt 程序所有用户界面对象的基类.




    <span style="color: #000000">#ifndef DEMO_H
    </span><span style="color: #0000ff">#define</span> DEMO_H<span style="color: #000000">

    #include </span><QtWidgets/QWidget><span style="color: #000000">
    #include </span><span style="color: #800000">"</span><span style="color: #800000">ui_demo.h</span><span style="color: #800000">"</span>

    <span style="color: #0000ff">class</span> Demo : <span style="color: #0000ff">public</span><span style="color: #000000"> QWidget
    {
        Q_OBJECT

    </span><span style="color: #0000ff">public</span><span style="color: #000000">:
        Demo(QWidget </span>*parent = <span style="color: #800080">0</span><span style="color: #000000">);
        </span>~<span style="color: #000000">Demo();

    </span><span style="color: #0000ff">private</span><span style="color: #000000">:
        Ui::DemoClass ui;
    };

    </span><span style="color: #0000ff">#endif</span> <span style="color: #008000">//</span><span style="color: #008000"> DEMO_H</span>




这里面的代码我们以后再分析, 先写出 Hellp Qt! 出来.







双击 emo.ui 文件, 就会用 Qt Creator 打开界面.




[![image](http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb17.png)](http://www.smallcpp.cn/wp-content/uploads/2015/02/image17.png)







左侧是 Qt 程序的控件, 我们主要使用的有:





<table cellpadding="2" cellspacing="0" border="0" width="400" >
<tbody >
<tr >

<td width="200" valign="top" >QLabel(可以有超链接和图片)
</td>

<td width="200" valign="top" >静态文本
</td></tr>
<tr >

<td width="200" valign="top" >QTabWidget
</td>

<td width="200" valign="top" >选项卡
</td></tr>
<tr >

<td width="200" valign="top" >QTextEdit
</td>

<td width="200" valign="top" >多行文本框
</td></tr>
<tr >

<td width="200" valign="top" >QLineEdit
</td>

<td width="200" valign="top" >单行文本框
</td></tr>
<tr >

<td width="200" valign="top" >QGroupBox
</td>

<td width="200" valign="top" >分组框
</td></tr>
<tr >

<td width="200" valign="top" >QSplitLine
</td>

<td width="200" valign="top" >分隔线
</td></tr>
<tr >

<td width="200" valign="top" >QTableWidget
</td>

<td width="200" valign="top" >列表框
</td></tr>
<tr >

<td width="200" valign="top" >QPushButton
</td>

<td width="200" valign="top" >按钮
</td></tr>
<tr >

<td width="200" valign="top" >QCheckBox
</td>

<td width="200" valign="top" >复选
</td></tr>
<tr >

<td width="200" valign="top" >QRadioButton
</td>

<td width="200" valign="top" >单选
</td></tr>
<tr >

<td width="200" valign="top" >QHBoxLayout
</td>

<td width="200" valign="top" >水平布局
</td></tr>
<tr >

<td width="200" valign="top" >QVBoxLayout
</td>

<td width="200" valign="top" >垂直布局
</td></tr></tbody></table>




在左侧找到 Label 控件, 拖拽到中间的窗口界面上




[![image](http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb18.png)](http://www.smallcpp.cn/wp-content/uploads/2015/02/image18.png)







右键选择改变对象名称, 改成我们想要的对象名:




[![image](http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb19.png)](http://www.smallcpp.cn/wp-content/uploads/2015/02/image19.png)







右侧可以设计控件的一些属性, 例如我们把 Label 的文本改成局中显示:




[![image](http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb20.png)](http://www.smallcpp.cn/wp-content/uploads/2015/02/image20.png)







返回我们的 VS 工程, 打开 demo.cpp:




    #include <span style="color: #800000">"</span><span style="color: #800000">demo.h</span><span style="color: #800000">"</span><span style="color: #000000">
    <font style="background-color: #ff0000">#include </font></span><font style="background-color: #ff0000"><span style="color: #800000">"</span><span style="color: #800000">QLabel</span><span style="color: #800000">"</span></font><span style="color: #000000">

    Demo::Demo(QWidget </span>*<span style="color: #000000">parent)
        : QWidget(parent)
    {
        ui.setupUi(</span><span style="color: #0000ff">this</span><span style="color: #000000">);
        <font style="background-color: #ff0000">ui.label_Hello</font></span><font style="background-color: #ff0000">->setText(<span style="color: #800000">"</span><span style="color: #800000">Hello Qt!</span><span style="color: #800000">"</span></font><span style="color: #000000"><font style="background-color: #ff0000">);</font>
    }

    Demo::</span>~<span style="color: #000000">Demo()
    {

    }</span>







红色部分是我们新添加的代码, 功能是设计刚才拖拽的 QLabel 的显示文字.




注意我们要使用 Qt 的哪个类, 就要添加那个类的头文件.







编译运行:




[![image](http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb21.png)](http://www.smallcpp.cn/wp-content/uploads/2015/02/image21.png)
??
