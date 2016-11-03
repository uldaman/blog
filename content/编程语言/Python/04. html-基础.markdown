author: Martin
date: 2015-08-26 13:04
title: Html 基础

http 的本质也是 socket, 但它是一种短链接方式, 和之前做歪挂时用的 socket 不同, http 的服务端接收到客户端(一般是浏览器)的请求后, 先建立链接, 然后处理客户端的请求(登录, 验证, 回发数据等等), 处理完过后就会断开客户端的链接.

Html 的结构如下:
![](http://i62.tinypic.com/28s0xhu.jpg)

DOCTYPE 告诉浏览器使用什么样的 html 或 xhtml 规范来解析 html 文档.
如果没有 DOCTYPE 的声明, 那么浏览器会按照自己的方式来解析渲染页面, 这样就会导致不同事浏览器显示不同的样式, 所以一般会在 html 文档前面添加 DOCTYPE 来声明规范.

在 HTML 4.01 中, <!DOCTYPE> 声明引用 DTD, 因为 HTML 4.01 基于 SGML.
DTD 规定了标记语言的规则, 这样浏览器才能正确地呈现内容.
而 HTML5 不基于 SGML, 所以不需要引用 DTD. 直接使用 <!DOCTYPE html> 即可.
参考 [http://www.w3school.com.cn/tags/tag_doctype.asp](http://www.w3school.com.cn/tags/tag_doctype.asp)** (或者 [http://www.divcss5.com/](http://www.divcss5.com/))
DOCTYPE 仅做了解就好.**

* * *



**Html 标记
(思维导图 链接：[http://pan.baidu.com/s/1dDwIPqh](http://pan.baidu.com/s/1dDwIPqh) 密码：jg2q)**

格式标记
![](http://i58.tinypic.com/a43kzt.jpg)

文本标记
![](http://i59.tinypic.com/58g3p.jpg)

至于详细使用说明, 参考 [http://www.w3school.com.cn/tags/index.asp](http://www.w3school.com.cn/tags/index.asp) 即可.

另外, 需要注意的是, 某个字符(如 <), 它是 html 中的关键字, 如果想要在页面中输出它们, 就必须使用 html 中的字符实体(类似转义字符).
![](http://i61.tinypic.com/4rrd4h.jpg)
参考 [http://www.w3school.com.cn/html/html_entities.asp](http://www.w3school.com.cn/html/html_entities.asp)

* * *



**表格设计**

![](http://i57.tinypic.com/2eybehh.jpg)

* * *



**框架设计**

![](http://i62.tinypic.com/biych.jpg)

* * *

**表单设计**

![](http://i61.tinypic.com/do16qe.jpg)

* * *

**HTML 4.01 和 HTML 5**

html 5 中 DOCYTPE 只需要 <!DOCTYPE html> 一句, 而 4.01 中要收入 DTD 文件, 如:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

另外, html 4.01 中:
*. 单标记必须闭合, 如 <br> 必须写为 <br/>
*. 单属性必须添加属性值, 如 <input type=”radio” checked> 要写为 <input type=”radio” checked="checkend">
*. 标记和属性必须使用小写
00l
