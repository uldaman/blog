Title: 10、使用 pyqt 帮助文档
Author: Martin
Date: 2016-05-15 01:18
Summary: 官方文档永远是最好的学习资料...

官方文档永远是最好的学习资料, 学习 Pyqt 也不例外, 可惜的是默认的 `Qt Assistant` 中并没有包含 pyqt 的参考.

不过倒是有份在线版的.. [http://pyqt.sourceforge.net/Docs/PyQt4/classes.html](http://pyqt.sourceforge.net/Docs/PyQt4/classes.html)

在线版的使用起来总是不爽, 于是在网上找参考了一些文章, 终于在 Qt Assistant 上集成了 pyqt 参考.

首先, 安装 pyqt 后在 `\site-packages\PyQt4\doc\html` 目录下是有 html 格式的参考文档的, 只是 Qt Assistant 识别的是 `qch` 文件, 于是, 我们只要找办法把这些 html 文件生成 `qch` 文件, 再添加到 Qt Assistant 中就可以了.

参考资料:<br>
[基于Qt Assistant制作软件帮助文档](http://blog.chinaunix.net/uid-28194872-id-3672811.html)<br>
[pyqt class reference添加到qt设计师的qt助手中](http://askandstudy.blog.163.com/blog/static/199752058201202823638708/)<br>
[利用Qt Assistant 定制帮助文档](http://www.cnblogs.com/Braveliu/p/5055387.html)<br>

我们在 `\site-packages\PyQt4\doc\html` 目录下新建个 `pyqtclassreference.qhp` 文件, 这个文件就把它理解成一个配置文件好了, 等下要根据这个配置文件生成 `qch` 文件, 在 `pyqtclassreference.qhp` 中写入以下内容 (这个文件我共享了一份: [传送门](http://share.weiyun.com/f65c8c82d20c167f13880412d5fbe673)):

```xml
<?xml version="1.0" encoding="UTF-8"?>
 <QtHelpProject version="1.0">
     <namespace>pyqt.doc</namespace>
     <virtualFolder>doc</virtualFolder>
     <filterSection>
         <toc> <!-- 该标签指定了目录, 这些关键字会显示在 Qt Assistant 的目录页面 -->
            <section title="qabstractanimation" ref="qabstractanimation.html"></section>
            <section title="qabstractbutton" ref="qabstractbutton.html"></section>
            <!-- 省略了 N 多, 足有 500 个左右 -->
            <section title="qxmlstreamreader" ref="qxmlstreamreader.html"></section>
            <section title="qxmlstreamwriter" ref="qxmlstreamwriter.html"></section>
         </toc>
         <keywords> <!-- 该标签指定了索引, 这些关键字会显示在 Qt Assistant 的索引页面 -->
            <keyword name="qabstractanimation" ref="qabstractanimation.html"></keyword>
            <keyword name="qabstractbutton" ref="qabstractbutton.html"></keyword>
            <!-- 省略了 N 多, 足有 500 个左右 -->
            <keyword name="qxmlstreamreader" ref="qxmlstreamreader.html"></keyword>
            <keyword name="qxmlstreamwriter" ref="qxmlstreamwriter.html"></keyword>
         </keywords>
         <files> <!-- 该标签指定了实际的文件 -->
            <file>qabstractanimation.html</file>
            <file>qabstractbutton.html</file>
            <!-- 省略了 N 多 -->
            <file>images/alphafill.png</file>
            <file>images/assistant-toolbar.png</file>
            <!-- 省略了 N 多 -->
            <file>_static/ajax-loader.gif</file>
            <file>_static/basic.css</file>
            <file>_sources/buffer_interface.txt</file>
            <file>_sources/build_system.txt</file>
            <!-- 省略了 N 多 -->
         </files>
     </filterSection>
 </QtHelpProject>
```
<br>
这个文件里面的内容太多了, 手写是不可能的...所以用写个脚本去生成这个文件比较靠谱, 脚本关键性代码如下:

```python
# -*- coding: utf-8 -*-
import os

files=os.listdir('\site-packages\PyQt4\doc\html')
for file in files:
    if file != 'make_qch.py':
        title_name = os.path.basename(file)
        title_name = title_name.split('.', 1)[0]
        file = '<section title="' + title_name + '" ref="' + file + '"></section>'
        # file = '<keyword name="' + title_name + '" ref="' + file + '"></keyword>'
        # file = '<file>_sources/' + file + '</file>'
        print file
```
<br>
然后是用命令生成 `pyqtclassreference.qch` 文件:

```
C:\Python27\Lib\site-packages\PyQt4\doc\html>qhelpgenerator pyqtclassreference.qhp -o pyqtclassreference.qch
Building up file structure...
Insert custom filters...
Insert help data for filter section (1 of 1)...
Insert files...
Insert contents...
Insert indices...
Documentation successfully generated.

C:\Python27\Lib\site-packages\PyQt4\doc\html>
```
<br>
再把该 pyqtclassreference.qch 文件添加到 Qt Assistant 中就可以了 (编辑 \-\> 首选项), 下图是添加后的界面:

![](http://i64.tinypic.com/2rztls1.jpg)

pyqtclassreference.qch 我也共享了一份生成好的: [传送门](http://share.weiyun.com/52a4278e52ef50769583509dbbc76544)
