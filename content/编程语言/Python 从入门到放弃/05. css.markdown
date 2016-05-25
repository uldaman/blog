author: Martin
date: 2015-08-27 10:02
title: CSS


链接：[http://pan.baidu.com/s/1uhgM6](http://pan.baidu.com/s/1uhgM6) 密码：z1gq

div 和 span 的存在就是为了应用 CSS 样式, 他们单独存在没有意义.
div 和 span 的区别, 在于 span 是内联元素, 而 div 是块级元素(简单地说, 它等同于其前后有断行).

**盒模型**

![](http://i59.tinypic.com/zt6o8w.jpg)

<table cellpadding="2" width="656" border="1" cellspacing="0" class="table" > <tbody > <tr >
<td width="200" valign="top" >Margin
</td>
<td width="454" valign="top" >是定义区块间距离的属性, 用1到4个值来设置元素的边界, 每个值都是长度、百分比或者auto, 百分比值参考上级元素的宽度, 允许使用负值边际.如果四个值都给出了, 它们分别被应用于上、右、下和左边界.如果只给出一个值, 它被应用于所有边界.如果两个或三个值给出了, 省略了的值与对边相等.注意如果边界在垂直方向邻接(重叠)了, 会改用其中最大的那个边界值.而水平方向则不会.也可以选择使用上边界margin-top、下边界margin-bottom、左边界margin-left和右边界margin-right属性分别设置与上级元素的外边距.
</td></tr> <tr >
<td width="200" valign="top" >padding
</td>
<td width="454" valign="top" >用于设置区块的内边距属性, 是边框和元素内容之间的间隔距离.与margin属性相返, 但使用的是相同属性值.是上补白padding-top、右补白padding-right、下补白padding-bottom和左补白padding-left属性的略写.
</td></tr> <tr >
<td width="200" valign="top" >Border
</td>
<td width="454" valign="top" >属性:
border-color: red
border-width: 1px
border-style: dotted(点划线) dashed(虚线) solid(实线) double(双重线)
简写: border: 1px solid #F00
</td></tr></tbody></table>

* * *



**布局相关**

![](http://i58.tinypic.com/2ng8nls.jpg)

clear 是指定一个元素是否允许有元素漂浮在它的旁边;
值 left 将移动元素到在其左边的漂浮元素下面, 同样的值 right 将移动元素到其右边的漂浮元素下面, 其他的还有缺省的 none 值, 和移动元素到其两边的漂浮元素下面的 both 值.
?
