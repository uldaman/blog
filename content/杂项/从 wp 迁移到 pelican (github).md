Title: 从 wp 迁移到 pelican (github)
Author: Martin
Date: 2016-01-03 23:00
Summary: 考虑了很久, 终于下定决心把博客从 wordpress 迁移到 github 上了, 这里作个记录, 方便以后查询.

考虑了很久, 终于下定决心把博客从 wordpress 迁移到 github 上了, 这里作个记录, 方便以后查询.

[TOC]

#1. Pelican 博客搭建
首先, 要在 github 上建立自己的主页, 方法很简单, 在自己的 github 上 new 一个 repository，名字必须是 **yourname.github.com**, 然后通过 yourname.github.com 就能访问了这个 repository 主干下的 index.html 文件了, 为方便测试, 可以手动添加一个 index.html, 然后随便写上几句话, 然后通过 yourname.github.com 查看效果.

接下来, 就是搭建本地博客了, 这里使用的是 pelican 系统, why? 因为它是 Python 写的, 而我又刚好懂那么一丢丢 python...

```shell
pip install pelican
pip install Markdown
```
<br>
然后新建一个 myblog 文件夹, 运行 cmd, 进入这个文件夹, 然后执行 **pelican-quickstart**, 运行命令后, 会让做一些选项设置:

```
> Where do you want to create your new web site? [.]
> What will be the title of this web site? SmallCpp
> Who will be the author of this web site? Martin
> What will be the default language of this web site? [en] zh
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) http://z351522453.github.com
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Asia/Shanghai
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
Done. Your new project is available at C:\Users\Administrator\Desktop\test
```
<br>
然后, 在当前的 myblog 目录下就有以下文件:

```
myblog/
├── content
│   └── (pages)
├── output
├── develop_server.sh
├── fabfile.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```
<br>
content: 这里是放置博文的 md 文件, 例如 hello_python.markdown 文章;

output: 这个目录下放置的就是一会利用 pelican 生成的静态博客内容, 当然是 html 的;

pelicanconf.py: 是博客的配置文件;

publishconf.py: 发布配置文件,可有可无;

Makefile: make 命令的配置文件, 如果你懂 linux 这个就so easy! 不过不懂也没事, 基本用不上;

develop_server.sh: 本地服务的脚本, 用来测试当前生成的博客的.

接下来就是写个测试博客~

到 content 目录下新建个 my_first.markdown 文件:

```
Title: 标题
Author: 作者
Date: 2010-12-03 10:20
Category: 分类
Tags: 标签1, 标签2
Slug: url 别名
Summary: 摘要

正文
```
<br>
保存好后, 用 cmd 进入 myblog 目录, 执行 **make html**, 过一会, output 目录下就生成了博客文件, 再执行 **make serve**, 然后打开浏览器, 访问: **http://localhost:8000/**, 如果不出问题, 应该能够看到我们博客了...

pelican 支持很多插件, 这里暂时用不上, 因为我只是用来当一个静态页面而已, 不过换个自己喜欢的主题还是蛮不错的~

#2. 更换主题
从 **https://github.com/getpelican/pelican-themes.git** 上把项目 clone 下来, 解压文件夹到 myblog 目录下(与 output 同级), 然后在 **pelicanconf.py** 文件里设置要使用的主题: **THEME = 'pelican-themes/xxx'**, 我这里使用的是 THEME = 'pelican-themes/zurb-F5-basic'.

zurb-F5-basic 主题现在有个 Bug, 那就是第一篇博文竟然是全文显示, 这特么简直就是巨坑... 不过还好, 机智的我找到了解决方案, 依次打开文件 **myblog/pelican-themes/zurb-F5-basic/templates/index.html**, 更改如下:

```html
{% extends "base.html" %}
{% block content_title %}{% endblock %}
{% block content %}
{% if articles %}
    {% for article in articles_page.object_list %}
        <article>
            <a href="{{ SITEURL }}/{{ article.url }}"><h3 class="article-title">{{ article.title }}</h3></a>
            {% include 'article_infos.html' %}{{ article.summary }}{% include 'article_infos_bottom.html' %}{% include 'comments.html' %}
            <a class="button radius secondary small right" href="{{ SITEURL }}/{{ article.url }}">Read More</a>
            <hr  class="gradient"/>
        </article>

        {% if loop.last %}
            <!-- /#posts-list -->
            {% if loop.last and (articles_page.has_previous() or not articles_page.has_previous() and loop.length > 1) %}
                {% include 'pagination.html' %}
            {% endif %}
        {% endif %}
    {% endfor %}

{% else %}

    <h3>Pages</h3>
    {% for page in PAGES %}
        <li><a href="{{ SITEURL }}/{{ page.url }}">{{ page.title }}</a></li>
    {% endfor %}

{% endif %}
{% endblock content %}
```
<br>
对于 `pelicanconf.py`, 除了 THEME 外, 还有一些有用的设置:

```python
AUTHOR = u'martin'
SITENAME = u'Small Cpp'
SITEURL = 'http://z351522453.github.com'

THEME = 'pelican-themes/zurb-F5-basic'
USE_FOLDER_AS_CATEGORY = True # 这个可以让 pelican 根据 content 里的文件夹结构自动生成文章分类
DELETE_OUTPUT_DIRECTORY = True # 编译之前删除 output 目录，这样保证 output 下生成的内容干净
SUMMARY_MAX_LENGTH = 30 # 文章摘要最大字数

# 设置 MD 语法高亮
MD_EXTENSIONS = [
  "extra",
  "toc",
  "headerid",
  "meta",
  "sane_lists",
  "smarty",
  "wikilinks",
  "admonition",
  "codehilite(guess_lang=False,pygments_style=monokai,noclasses=True)"]
```
<br>
**注意**, MD 语法高亮的设置需要 python 包 `pygments` 支持, 所以, 先安装 `pygments` 吧.

> pygments\_style 可以在 [http://pygments.org/demo/](http://pygments.org/demo/?lang=cpp&sort=) 进行调试<br>
> Reference:<br>
> [Introduction to Pelican](http://crunk.io/post/introduction-to-pelican/)<br>
> [Django 中使用 markdown 和代码高亮](http://fatsoon.com/2014/07/26/2014-07-26-use-highlite-in-django/)<br>
> [Python Markdown v2.6.6 documentation » CodeHilite Extension](https://pythonhosted.org/Markdown/extensions/code_hilite.html)<br>
> [Markdown Preview](https://packagecontrol.io/packages/Markdown%20Preview)

然后再重新用 cmd 进入 myblog 目录, 执行 **make html** + **make serve**, 访问: [http://localhost:8000/](http://localhost:8000/), 看看我们的博客主题是不是已经发生变化啦~~

## 2.1 添加评论系统
pelican 原生支持 DISQUS 评论系统, 然而坑爹的 GFW . . .

所以我改用了国内的[多说评论系统](http://duoshuo.com/) (来必力也是一个不错的评论系统, 可以去试试), 首先去[多说官网](http://duoshuo.com/)注册一个账号, 然后为我们的 blog 添加一个站点.

![](http://i66.tinypic.com/t0p00h.jpg)

添加好后, 在管理页面会看到如下信息:

![](http://i67.tinypic.com/2cg2dxy.jpg)

打开 pelican 主题目录下的 `article.html` 文件, 在 `</article>` 上面添加上图中的代码, 我这里改成了:

```html
{% extends "base.html" %}
{% block title %}{{ article.title|striptags }}{% endblock %}
{% block content %}
<article>
    <header>
        <h3 class="article-title"><a href="{{ SITEURL }}/{{ article.url }}" rel="bookmark"
        title="Permalink to {{ article.title|striptags }}">{{ article.title }}</a></h3>
        {% include 'twitter.html' %}
    </header>

    {% include 'article_infos.html' %}
    {{ article.content }}
    {% include 'article_infos_bottom.html' %}

<!--     {% if DISQUS_SITENAME and SITEURL and article.status != "draft" %}
    <h4>Comments</h4>
    {% include 'disqus_script.html' %}
    {% endif %} -->

    <!-- 多说评论框 start -->
    <h4>Comments !</h4>
    <div class="ds-thread" data-thread-key="{{ article.slug }}" data-title="{{ article.title }}" data-url="{{ SITEURL }}/{{ article.url }}"></div>
    <!-- 多说评论框 end -->
    <!-- 多说公共JS代码 start (一个网页只需插入一次) -->
    <script type="text/javascript">
        var duoshuoQuery = {short_name:"smallcpp"};
            (function() {
                var ds = document.createElement('script');
                ds.type = 'text/javascript';ds.async = true;
                ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
                ds.charset = 'UTF-8';
                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
            })();
    </script>
    <!-- 多说公共JS代码 end -->
</article>
{% endblock %}
```
<br>
#3. 解析 GFM
> 使用 GFM 后, 有些 markdown 样式渲染不出来, 不再推荐使用~ 仅了解下就好.

GFM 即 Github Flavored Mardown, 它是现在比较受欢迎的一种 Markdown 风格, 但 pygments 本身并不支持 (py\-markdown 的语法高亮通过 pygments 来支持), 要通过第三方扩展来实现.

首先, 要安装 pymdown  第三方扩展 `pip install pymdown-extensions`, 然后把 `pelicanconf.py` 文件中 `MD_EXTENSIONS` 的 **extra** 替换成 **pymdownx.github**.

Pymdown Extensions Documentation 对 **pymdownx.github** 说明如下:

```
For code highlighting, you will also need to load the markdown.extensions.codehilite extension yourself as well with guess_lang=False and your preferred Pygments style (if available or use some other JavaScript highlighter). Though there is no Github style included with this extension, you are most likely able to find a suitable theme online by searching. I do have older Github styles found at the pymdown-styles repo; it contains the original Pygments Github style (github) and the Github 2014 style (github2014) which Github used before they ditched Pygments for their own in-house highlighter.
```
<br>
简单的说, 就是 **pymdownx.github** 提供了一些功能用来模仿 Github, 但不是全部, 如果想要使用 Github 的代码高亮, 你需要设置 `markdown.extensions.codehilite` 的 `guess_lang=False`, 并且引用一个 `Pygments style` 文件, 虽然该扩展本身并不包含 Github style, 但是你可以去找....然后作者也给了一个 [pymdown-styles repo](https://github.com/z351522453/pymdown-styles) 供使用 (我将它 Fork 回自己的仓库, 做了点更改, 让它更像 Github 的高亮风格).

使用方法比较简单, clone 项目到本地, 执行 `python setup.py install`, 然后修改 `pelicanconf.py` 文件中 `MD_EXTENSIONS` 的 **codehilite**, 最终的 **MD_EXTENSIONS** 如下:

```js
MD_EXTENSIONS = [
  "pymdownx.github(no_nl2br=True)",
  "toc",
  "headerid",
  "meta",
  "sane_lists",
  "smarty",
  "wikilinks",
  "admonition",
  "codehilite(guess_lang=False,pygments_style=github2014,noclasses=True)"]
```
<br>
References:<br>
[Python Markdown Documentation](https://pythonhosted.org/Markdown/extensions/)<br>
[Pymdown Extensions Documentation For Github](http://facelessuser.github.io/pymdown-extensions/extensions/github/)<br>
[Markdown Preview](https://packagecontrol.io/packages/Markdown%20Preview)


#4. 添加网站图标
不同的 pelican 主题添加方法不一样, 我这里用的是 `zurb-F5-basic` 主题, 就以它为例说明下.

首先准备好 `ico` 文件如 `favicon.ico`, 放到主题的静态图标目录下 (`~\pelican-themes\zurb-F5-basic\static\images\icons`), 然后打开文件 **~/pelican-themes/zurb-F5-basic/templates/base.html**, 在 `head` 标签中添加一行:

```html
<link rel="shortcut icon" type="image/x-icon" href="{{ SITEURL }}/theme/images/favicon.ico" />
```
<br>
#5. 迁移 wordpress
环境搭建好后, 就是把我们 wordpress(后面简称 wp) 的内容迁移过来啦.

**第一步**, 进入 wp 后台, 工具->导出, 然后把 '全部' 和 '文章' 这两个都导出一份(其实我们导出文章就可以了, 把 '全部' 也都导出是为了以后可能还有用处, 以防万一嘛), 然后进入我们的主机管理系统(这个我们购买的主机商那就有提供), 把 mysql 数据也导出一份, 然后进入主机空间, 把整个空间都 dump 一份.

**第二步**, 到 https://github.com/thomasf/exitwp.git **clone** 项目到本地, 把刚从 wp 导出的 '文章' xml 放到 exitwp 目录下的 **wordpress-xml** 子目录里, 然后 cmd 进入 exitwp 目录, 执行 **python exitwp.py**, 稍等片刻, 我们的文章全部都转成 *.md 格式啦(路径: **exitwp/build/jekyll/原 wp 路径/_posts**).

不过, 这里有个坑, 这个工具导出的 md 文件, 是按文件内容里的 slug 项来命名的, 特么 py 对中文的处理不大好, 导致 md 的文件名都有问题, 于是写了个脚本用来转换用户名.

```python
'''
当使用 exitwp 生成 md 文件时, 文件名会乱码, 使用该脚本可以修复

'''
# -*- coding: utf-8 -*-
import re
import urllib
import os

files=os.listdir('C:/Users/Administrator/Desktop/exitwp-master/build/jekyll/www.smallcpp.cn/_posts') # 路径自己改
for file in files:
    if file != u'change_md_file_name.py':
        file_object = open(file)
        all_the_text = file_object.read( )
        header = re.search('''---(.*?)---''', all_the_text, re.S)
        slug = re.search('''slug: (.*?)title''', header.group(1), re.S)
        new = urllib.unquote(slug.group(1)).replace('\n', '').decode('utf-8')
        file_object.close()

        os.renames(file, new + '.markdown')
```
<br>
**第三步**, 有了 md 文件了, 剩下的还不好办吗, 全部拷贝到 myblog/content 目录下, 然而问题又来了, 一堆 md 文件堆在一个文件夹下显然是很乱的, 而且也无法利用 **USE_FOLDER_AS_CATEGORY = True # 这个可以让 pelican 根据 content 里的文件夹结构自动生成文章分类** 这条设置了, 所以又写了个脚本把文章按类别分类(在运行脚本之前要手动建好文件夹).

```python
# -*- coding: utf-8 -*-
'''
读取文件中的 Category, 然后将文件放到 Category 指定的文件夹
'''
import re
import urllib
import os
import shutil


files=os.listdir('C:/Users/Administrator/Desktop/content')
for file in files:
    file = file.decode('gbk').encode('utf-8')
    if file != 'sss.py':
        file_object = open(file.decode('utf-8').encode('gbk'))
        lnum = 0
        for line in file_object:
                lnum += 1
                if lnum == 5:
                    result = re.search('''Category: (.*?)\n''', line, re.S)
                    tar = 'C:/Users/Administrator/Desktop/field/' + result.group(1)
                    shutil.copy(file.decode('utf-8').encode('gbk'),  tar.decode('utf-8').encode('gbk'))
                    break
        file_object.close()
```
<br>
**第四步**, md 按类别整理好后, 就可以用 **make html** 来生成 blog 啦, 不过遗憾的是特么生成的文件名依然是乱码, 于是又写了个脚本修复文件名...(应该可以改源码的, 暂时没空看源码, 先用这个脚本过度下).

```python
# -*- coding: utf-8 -*-
'''
当使用 make html 生成 html 文件, 文件名乱码, 使用该脚本可以修复
'''
import re
import urllib
import os


files=os.listdir('C:/Users/Administrator/Desktop/123')
for file in files:
    if file != 'change_hml_file_name.py':
        new = urllib.unquote(file).replace('\r', '').replace('\n', '')
        print new
        os.renames(file, new.decode('utf-8'))
```
<br>
好了, 现在我们的 wp 已经迁移到了本地博客系统, 运行 **make serve** 看看是不是成功了...

#6. 发布到 Github
> 更新: 关于发布到 Github 还是有些东西要说的, 见我另一篇笔记: [迁移 Github Project Page](http://blog.smallcpp.cn/qian-yi-github-project-page.html)

这个其实没啥好讲的了, 我是用的 github for windows 工具来管理 github, 每次 **make html** 后, 把 output 下的文件同步到 github 上 page 项目的主干下就行了...

再来说说顶级域名吧, 首先, 在 github 的 page 项目的目录下, 新建一个 **CNAME** 文件, 里面写上你的顶级域名地址, 例如我的: **www.smallcpp.cn**, 然后到域名供应商那里 添加 or 修改 下解析设置, 我用的是 dnspod:

```
@      CNAME        yourname.github.com
www    CNAME        yourname.github.com
```
