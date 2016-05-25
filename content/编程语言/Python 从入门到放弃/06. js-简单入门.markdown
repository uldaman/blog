author: Martin
date: 2015-08-29 15:14
title: js 简单入门

js 在 html 中的使用方式和 css 很像, 可以通过内联和外部引用两方式:

    <span style="color: #0000ff"><</span><span style="color: #800000">script </span><span style="color: #ff0000">type</span><span style="color: #0000ff">="text/javascript"</span><span style="color: #ff0000"> src</span><span style="color: #0000ff">="test.js"</span><span style="color: #0000ff">></</span><span style="color: #800000">script</span><span style="color: #0000ff">></span>

    <span style="color: #0000ff"><</span><span style="color: #800000">script </span><span style="color: #ff0000">type</span><span style="color: #0000ff">="text/javascript"</span><span style="color: #0000ff">></span><span style="color: #000000; background-color: #f5f5f5">
        document.write(</span><span style="color: #000000; background-color: #f5f5f5">"</span><span style="color: #000000; background-color: #f5f5f5">a</span><span style="color: #000000; background-color: #f5f5f5">"</span><span style="color: #000000; background-color: #f5f5f5">);
    </span><span style="color: #0000ff"></</span><span style="color: #800000">script</span><span style="color: #0000ff">></span>





js 可以在 <head>、<body> 以及 [</body> </html>]之间插入使用.
![](http://i57.tinypic.com/2rwulhd.jpg)




因为 html 是从下向下解释的, 所以如果把 js 放在前面, 会导致出错时, js 下面的代码无法被解释.
因此, 一般都会把 js 放在下面.




**如何调试 JS**




**console.log;** -- 输出 Log 信息, 可在审查代码的 Console 选项卡里看到.
**alert(str);** -- 弹出对话框, 类似 messagebox
**debugger;** -- 当开启浏览器的 javascript 调试器时, 代码会在这里断下来.
**window.onerror;** -- 当出错时, 会调用这个函数, 所以可以重写这个函数, 注意, 该函数只能运行时检查, 如果语法错误, 并不能提示.




    window.onerror = <span style="color: #0000ff">function</span><span style="color: #000000"> (szMsg, szUrl, szLine) {
        str </span>= ""<span style="color: #000000">;
        str </span>+=<span style="color: #000000"> szMsg;
        str </span>+= "\r\n"<span style="color: #000000">
        str </span>+=<span style="color: #000000"> szUrl;
        str </span>+= "\r\n"<span style="color: #000000">
        str </span>+=<span style="color: #000000"> szLine;
        alert(str);
        </span><span style="color: #0000ff">return</span> <span style="color: #0000ff">true</span><span style="color: #000000">;
    };</span>





js 的注释方法和 C/C++ 差不多.




同样, js 也有一些关键字和保留字.
![](http://i57.tinypic.com/2ibjlzr.jpg)




**js 的数据类型**




js 中使用 **var** 来声明局部变量, 使用 **typeof var **可以检测类型.
javascript 的全局变量和局部变量和 C/C++ 有不少的区别, 详见: [http://blog.csdn.net/zyz511919766/article/details/7276089](http://blog.csdn.net/zyz511919766/article/details/7276089)
补充一点, 如果在函数体内不带 var 声明一个变量, 那么它将会是全局变量.


<table cellpadding="2" width="400" border="1" cellspacing="0" class="table" >
<tbody >
<tr >

<td width="200" valign="top" >基本类型
</td>

<td width="200" valign="top" >复杂类型
</td></tr>
<tr >

<td width="200" valign="top" >undefined
</td>

<td width="200" valign="top" >object
</td></tr>
<tr >

<td width="200" valign="top" >null
</td>

<td width="200" valign="top" >
</td></tr>
<tr >

<td width="200" valign="top" >boolean
</td>

<td width="200" valign="top" >
</td></tr>
<tr >

<td width="200" valign="top" >number
</td>

<td width="200" valign="top" >
</td></tr>
<tr >

<td width="200" valign="top" >string
</td>

<td width="200" valign="top" >
</td></tr></tbody></table>



null 和 undefined 的区别参考: [http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html](http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html)
总结就是:
null 表示"没有对象", 即该处不应该有值.
undefined 表示"缺少值", 就是此处应该有一个值, 但是还没有定义.




    <span style="color: #0000ff">var</span> car = 123<span style="color: #000000">;
    alert(</span><span style="color: #0000ff">typeof</span> car);






**默认参数**




js 的默认参数和 C/C++及 Python 也是很不一样的, 它并不能在参数列表中直接指定, 要在函数体内指定...
![](http://i58.tinypic.com/1zp3yit.jpg)




![](http://i62.tinypic.com/2mdf7fa.jpg)




**匿名函数 -- 就是把一个函数复制给一个变量, 和 lua 差不多, 不多解释.**




**自执行函数**




不需主动调用自己就可以执行的函数, 就是通过**两个括号**...



    (<span style="color: #0000ff">function</span><span style="color: #000000">() {

    })();</span>




自执行函数还有其他写法, 记住这一种就可以.




**数组**




声明, 如: var array = Array() 或 var array = []




添加, array.push() -- 追加;
array.unshift() -- 最前插入;
array.splice() -- 插入, 这个函数比较复杂, 具体去查 google.




删除, array.pop()
array.shift()
array.splice()




其他的操作请参考 google...




遍历, 两种方式:



    <span style="color: #0000ff">var</span> array = [11, 12, 13<span style="color: #000000">]
    </span><span style="color: #0000ff">for</span>(<span style="color: #0000ff">var</span> index <span style="color: #0000ff">in</span><span style="color: #000000"> array) {
        console.log(array[index]);
    }
    </span><span style="color: #0000ff">for</span>(<span style="color: #0000ff">var</span> index = 0; index < array.length; index++<span style="color: #000000">) {
        console.log(array[index]);
    }</span>
ؔ
