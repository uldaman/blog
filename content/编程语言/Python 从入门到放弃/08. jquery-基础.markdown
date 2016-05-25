author: Martin
date: 2015-09-02 10:25
title: jQuery 基础

jQuery 是一套跨浏览器的 JavaScript 库, 简化 HTML 与 JavaScript 之间的操作.
使用 jQuery 先从其官网上下载它, 我提供一个 1.11.3 的版本.
[http://yunpan.cn/cmrJPrqjPZ35c](http://yunpan.cn/cmrJPrqjPZ35c) 访问密码 271a

有问题查帮助就可以了 [http://www.php100.com/manual/jquery/](http://www.php100.com/manual/jquery/)

再说一个 prop 和 attr 区别:
![](http://oi58.tinypic.com/jgte8i.jpg)

* * *

$(function(){…}) -- 类似自执行功能, 当页面加载完全后会自动执行一次, 如:


    <span style="color: #000000">$(
        </span><span style="color: #0000ff">function</span><span style="color: #000000"> () {
            $(</span>":button").click( <span style="color: #0000ff">function</span><span style="color: #000000"> () {
                ...
            });
        }
    );</span>




这样就给页面里的按钮注册了一个点击事件.




$(this) -- 当前 jQuery 对象.




推荐一个工具: font awesome -- the iconic font and CSS toolkit.
tt?
