author: Martin
date: 2015-02-15 14:13
title: 5、QT 中文乱码

在 Qt 代码的 const char* 这种窄字符串中使用中文就会发现显示的全是乱码.

在 Qt5 之前, 大多数人通过下面这三句代码来解决:

    QTextCodec::setCodecForTr(...)
    QTextCodec::setCodecForCStrings(...)
    QTextCodec::setCodecForLocale(...)



    然后这三句代码是有安全隐患的, 下面的文章都有说明:






  *


[QString 与中文问题](http://hi.baidu.com/cyclone/blog/item/9d7293130e5a498d6538dbf1.html)



  *


[Qt中translate、tr关系 与中文问题](http://hi.baidu.com/cyclone/blog/item/aa56e5dd1a79f7e176c638be.html)



  *


[Qt国际化（源码含中文时）的点滴分析](http://blog.csdn.net/dbzhang800/article/details/6334852)







但是在 Qt5 之后, 移除了 setCodecForTr 函数, 之前的 setCodecxxx 各种副作用都不再存在, 而且中文问题更为简单:




    QString s1 = QStringLiteral(<span style="color: #800000">"</span><span style="color: #800000">中文</span><span style="color: #800000">"</span><span style="color: #000000">);
    QString s2 </span>= QString::fromWCharArray(L<span style="color: #800000">"</span><span style="color: #800000">中文</span><span style="color: #800000">"</span>);







这两种写法都是可以的.

    <a href="http://www.smallcpp.cn/wp-content/uploads/2015/02/image25.png"><img src="http://www.smallcpp.cn/wp-content/uploads/2015/02/image_thumb25.png" style="background-image: none; border-right-width: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px; padding-top: 0px" title="image" height="342" width="502" alt="image" border="0"></a>



    因为在 VS 中鼓励大家使用 TEXT/_T 宏而不用L, 所以 QStringLiteral 用的相对要多点.






关于 Qt 中文的问题, 可参考下面两篇文章:




[zz 解释QStringLiteral](http://www.tuicool.com/articles/6nUrIr)




[QString 乱谈(3)-Qt5与中文](http://blog.csdn.net/dbzhang800/article/details/7542672)
es0
