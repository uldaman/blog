Title: 使用 Simiki 进行碎片整理
Author: Martin
Date: 2016-05-27 19:46
Summary: 一些零散的知识, 如某个常用命令的语法、特定的软件配置等等, 记到博客上太零碎, 本地记录的也不够系统, 放到个人 Wiki 是最不过了.

[TOC]

# 开始
从 Hansong Xiao 的[程序员的知识管理](http://blog.xiaohansong.com/2016/01/16/kownledge-Management/)中学到用 wiki 来进行知识碎片整理, 确实, 一些零散的知识, 如某个常用命令的语法、特定的软件配置等等, 记到博客上太零碎, 本地记录的也不够系统, 放到个人 Wiki 是最不过了, 使用的就是 Hansong Xiao 推荐的 [Simiki](http://simiki.org/).

Simiki 提供了[中文文档](http://simiki.org/zh-docs/), 十分简单, 参考[中文文档](http://simiki.org/zh-docs/)分分钟就上手了, 所以就简单说说我折腾了的地方吧...

# DIY 主题
Simiki 自带的主题稍微有点 low, 可以使用官网推荐的另一款主题: [yasimple](https://github.com/tankywoo/yasimple/tree/ce4af036ab95ef1d5235266d8231f97dc14dd871), Clone 到本地后替换掉 `~/themes/simple` 下的文件;

这些主题都没有网站图标, 所以要再 DIY 一下, 先准备好网站图标, 如 `favicon.ico`, 放到 `~/themes/simple/static/images` 目录下 (没有 `images` 目录就新建一个), 然后打开 `~/themes/simple/base.html`, 在 **head** 标签中添加如下内容:

```html
<link rel="shortcut icon" href="{{ site.root }}/static/images/favicon.ico" type="image/x-icon">
<link rel="icon" href="{{ site.root }}/static/images/favicon.ico" type="image/x-icon">
```
<br>
# DIY 部署
我使用的是 Github Project Page, 所以可以把 **output** 目录加入 **.gitignore** 来忽略每次生成时的变化.

- **master** 分支托管源文件
- **gh-pages** 分支放 **output** 的发布文件

> 注意, 第一次使用时要先 **push** 一次 **master** 分支

推送 **gh-pages** 分支这一步可以使用 [ghp-import](https://github.com/davisp/ghp-import) 来简化操作, **ghp-import** 是一个 python 工具包, 能把一个文件夹里的内容推送到一个 branch 里, 不过 ghp-import 在 windows 下各种坑, 所以 windows 下就别想了...

官方给出了自动化部署的 `fabfile.py` 文件 (依赖于 **gh-pages**, windows 下勿使用), 只需在 `_config.yml` 中添加如下内容:

```
deploy:
  - type: git
```
<br>
然后使用 `fab deploy` 就能自动把 **output** 目录推送到远程 **gh-pages** 分支.

最后, 由于 Github Project Page 需要用到一个 `CNAME` 文件, 所以我修改了官方 `fabfile.py` 文件的 `deploy_git` 函数, 让部署时自动生成 `CNAME` 文件:

```python
def deploy_git(deploy_configs):
    '''for pages service of such as github/gitcafe ...'''
    with settings(warn_only=True):
        res = local('which ghp-import > /dev/null 2>&1; echo $?', capture=True)
        if int(res.strip()):
            do_exit('Warning: ghp-import not installed! '
                    'run: `pip install ghp-import`')
    output_dir = configs['destination']
    with lcd(output_dir):  # 添加 CNAME 文件
        local('echo wiki.smallcpp.com > CNAME')
    remote = deploy_configs.get('remote', 'origin')
    branch = deploy_configs.get('branch', 'gh-pages')
    # commit gh-pages branch and push to remote
    _mesg = 'Update output documentation'
    local('ghp-import -p -m "{0}" -r {1} -b {2} {3}'
          .format(_mesg, remote, branch, output_dir))
```
<br>
# 补充
由于我大部分情况在 windows 下工作, 所以上面的部署方法还是有些不足, 参考这篇博文 [Simiki + Travis-ci + Github-Pages 搭建自动部署的个人 Wiki](http://www.jianshu.com/p/d56008e6c2e1), 感觉也可以使用 **Travis-ci**, 所以继续折腾...
