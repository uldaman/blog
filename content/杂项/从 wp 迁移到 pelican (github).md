Title: 从 wp 迁移到 pelican (github)
Author: Martin
Date: 2016-01-03 23:00
Summary: 考虑了很久, 终于下定决心把博客从 wordpress 迁移到 github 上了, 这里作个记录, 方便以后查询.

考虑了很久, 终于下定决心把博客从 wordpress 迁移到 github 上了, 这里作个记录, 方便以后查询.

#1. Pelican 博客搭建
首先, 要在 github 上建立自己的主页, 方法很简单, 在自己的 github 上 new 一个 repository，名字必须是 **yourname.github.com**, 然后通过 yourname.github.com 就能访问了这个 repository 主干下的 index.html 文件了, 为方便测试, 可以手动添加一个 index.html, 然后随便写上几句话, 然后通过 yourname.github.com 查看效果.

接下来, 就是搭建本地博客了, 这里使用的是 pelican 系统, why? 因为它是 Python 写的, 而我又刚好懂那么一丢丢 python...
```
pip install pelican
pip install Markdown
```
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

对于 pelicanconf.py, 除了 THEME 外, 还有一些有用的设置:
```
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
然后再重新用 cmd 进入 myblog 目录, 执行 **make html** + **make serve**, 访问: **http://localhost:8000/**, 看看我们的博客主题是不是已经发生变化啦~~

#3. 迁移 wordpress
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


files=os.listdir('C:/Users/Administrator/Desktop/exitwp-master/build/jekyll/www.smallcpp.com/_posts') # 路径自己改
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
好了, 现在我们的 wp 已经迁移到了本地博客系统, 运行 **make serve** 看看是不是成功了...

#4. 发布到 github
这个其实没啥好讲的了, 我是用的 github for windows 工具来管理 github, 每次 **make html** 后, 把 output 下的文件同步到 github 上 page 项目的主干下就行了...

再来说说顶级域名吧, 首先, 在 github 的 page 项目的目录下, 新建一个 **CNAME** 文件, 里面写上你的顶级域名地址, 例如我的: **www.smallcpp.com**, 然后到域名供应商那里 添加 or 修改 下解析设置, 我用的是 dnspod:
```
@      CNAME        yourname.github.com
www    CNAME        yourname.github.com
blog   显性URL      http://www.smallcpp.com/
```
