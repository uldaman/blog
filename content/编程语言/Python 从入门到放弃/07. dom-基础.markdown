author: Martin
date: 2015-08-31 14:41
title: DOM 基础

**选择器:**

document.getElementById('id')

document.getElementsByName('name')

document.getElementsByTagName('tagname') // html 中的各种标记

**获取或者修改样式:** obj.className

**获取或设置属性:** getattribute(key) setattribute(key, val)

**获取或修改标签文本内容(指<> </>中间的文本部分):** obj.innerText -- 以文本方式

**获取或修改标签文本内容(指<> </>中间的文本部分):** obj.innerHTML -- 以 HTML 方式
如果用 obj.innerText = '<a href="">assssss</a>'; 那么最终页面将会显示成文本格式并不是超链接.
而用 obj.innerHTML = '<a href="">assssss</a>'; 那么最终就显示成一个超链接.

**创建标签:**
var link = document.createElement('a');
link.href = '[https://www.baidu.com/';](https://www.baidu.com/';)
link.innerText = '百度'; // 注意, 不是 value, 是 innerText
var bodys = document.getElementsByTagName('body');
bodys[0].appendChild(link);

**获取或修改样式中的属性:** obj.style.属性
注意, js 中的属性和 css 中的属性名称可能不一致, 如 background-color == style.background

**提交表单:** document.getElementById('form').submit()

**常用事件(HTML中使用调用js):**
onclick
onblur
onfocus
on…
eg: <input type="button" value="伪提交" onclick="Foo();"/> 按钮点击时会执行 js 中的 Foo() 函数

例子 (提交验证):


    <span style="color: #0000ff"><</span><span style="color: #800000">form </span><span style="color: #ff0000">id</span><span style="color: #0000ff">="F1"</span><span style="color: #ff0000"> action</span><span style="color: #0000ff">="https://www.sogou.com/web"</span><span style="color: #ff0000"> method</span><span style="color: #0000ff">="get"</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">input </span><span style="color: #ff0000">id</span><span style="color: #0000ff">="query"</span><span style="color: #ff0000"> type</span><span style="color: #0000ff">="text"</span><span style="color: #ff0000"> name</span><span style="color: #0000ff">='query'</span><span style="color: #0000ff">/></span>
        <span style="color: #008000"><!--</span><span style="color: #008000"><input type="submit" value="提交"/></span><span style="color: #008000">--></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">input </span><span style="color: #ff0000">type</span><span style="color: #0000ff">="button"</span><span style="color: #ff0000"> value</span><span style="color: #0000ff">="伪提交"</span><span style="color: #ff0000"> onclick</span><span style="color: #0000ff">="Foo();"</span><span style="color: #0000ff">/></span>
    <span style="color: #0000ff"></</span><span style="color: #800000">form</span><span style="color: #0000ff">></span>




    <span style="color: #0000ff">function</span><span style="color: #000000"> Foo() {
        </span><span style="color: #0000ff">var</span> query = document.getElementById('query'<span style="color: #000000">);
        </span><span style="color: #0000ff">if</span><span style="color: #000000"> (query.value) {
            </span><span style="color: #0000ff">var</span> forms = document.getElementsByTagName('form'<span style="color: #000000">);
            forms[</span>0<span style="color: #000000">].submit();
        }
    }</span>





**
还有几个常用的函数:**




setInterval("alert()", 2000); clearInterval(obj); -- 循环




setTimeout(); clearTimeout(obj); -- 执行一次
CI?
