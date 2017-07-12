Title: 迁移 Github Project Page
Author: Martin
Date: 2016-05-25 18:45
Summary: 将我的博客从 User Pages site 迁移到 Project Pages site.

在很早之前我从 wordpress 迁移到 github, 参考日记: [从 wp 迁移到 pelican (github)](http://blog.smallcpp.cn/cong-wp-qian-yi-dao-pelican-github.html)

近期读到一个博主的文章: [程序员的知识管理](http://blog.xiaohansong.com/2016/01/16/kownledge-Management/), 参考了下他的 [Github Page 首页](http://xiaohansong.com/), 发现挺有意思的.

他的 [Github Page 本身](https://github.com/x-hansong/x-hansong.github.io) 很少内容, 但是 [http://blog.xiaohansong.com/](http://blog.xiaohansong.com/) 却能访问到他的 [blog 仓储](https://github.com/x-hansong/blog), 而 [http://wiki.xiaohansong.com/](http://blog.xiaohansong.com/) 也能访问 [wiki 仓储](https://github.com/x-hansong/wiki)...

查找到 [Gihub 官方 Github Page 资料](https://help.github.com/categories/github-pages-basics/) 才发现还有 **User Pages site** 和 **Project Pages site** 之分, 而上面那位就是利用了 **Project Pages site**...于是, 本着学习的态度, 我迁移了自己的 Github Page.

[TOC]

# 创建 Project Pages site
Project Pages site 和普通的 Github Repository 没两样, 但它利用一个 `gh-pages` 分支来用于构建和发布项目页面的网站, 然后通过 `username.github.io/projectname` (你也可以自定义域名) 来访问这个项目的 `gh-pages`.

我们直接在 Github 上再新建个仓库命名为 `blog`, 然后将它 clone 到本地:

```shell
git clone github.com/user/repository.git
```
<br>
再创建 `gh-pages` 分支:

```shell
cd repository

git checkout --orphan gh-pages
Switched to a new branch 'gh-pages'

git rm -rf .
```
<br>
现在, 这个 `gh-pages` 分支就是我们新的 `blog` 仓库, 类似于以前 Github Page 仓库 (username.github.io) 的主分支, 我们将以前 Github Page 仓库下的文件拷贝到这个 `gh-pages` 分支下, 最后提交到远程:

```shell
git push origin gh-pages
```
<br>
现在, 我们通过 `username.github.io/blog` 就能访问 `blog` 仓库 `gh-pages` 分支下的 `index.html` 文件.

# 添加自定义域名
首先修改 `gh-pages` 下的 `CNAME` 文件内容, 从顶级域名 `smallcpp.cn` 改为子级域名 `blog.smallcpp.cn`  (`smallcpp.cn` 是我的顶级域名, 你需要自己购买), 改完后可以通过下面的方法验证下:

- Repository settings buttonUnder your repository name, click  Settings.
- Under "GitHub Pages", you should see the custom domain from your CNAME file.

![](http://i64.tinypic.com/5dmhqc.jpg)

然后去 `dnspod` 为 `smallcpp.cn` 添加一个记录:

```
blog    CNAME        username.github.io
```
<br>
修改过后要等一段时间才能生效, 具体时间视域名运营商决定...

# 迁移博客源文件
我是用 `Pelican` 创建的博客, 在以前, 放在 `username.github.io` 下的是发布文件 (即通过 `make html` 生成的网站文件), `Pelican` 源码文件通过另一个仓库 `MyBlog` 来保存.

现在, 我有了 Project Repository, 它的 `gh-pages` 分支被用来放发布文件, 它的 `master` 分支就可以用来放博客的源码文件啦~

![](http://i63.tinypic.com/xddzia.jpg)

# 修改 Pelican 配置
在 Pelican 项目中, `pelicanconf.py` 配置文件中有一项 **SITEURL** 指向的是 `http://username.github.io`, 因此所有的静态文件都是访问 `username.github.io` 下的, 现在要改成 `http://username.github.io/blog`.

# 补充
**Pelican** 提供了 **fabric** 的方式部署代码, 直接执行 `fab gh_pages` 就能把项目的 output 目录下的文件推送到 `gh-pages` 分支, 不过要修改下 Pelican 默认的 `fabfile.py` (让其自动生成 CNAME):

```python
def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    with lcd('{deploy_path}'.format(**env)):
        local('echo blog.smallcpp.cn > CNAME')

    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))
```
<br>
# References
[GitHub Pages Basics](https://help.github.com/categories/github-pages-basics/)<br>
[Setting up your pages site repository](https://help.github.com/articles/setting-up-your-pages-site-repository/)<br>
[Setting up a custom subdomain](https://help.github.com/articles/setting-up-a-custom-subdomain/)<br>
[GitHub Pages 指南](http://wiki.jikexueyuan.com/project/github-pages-basics/)<br>
[单个 GitHub 帐号下添加多个 GitHub Pages 的相关问题](https://segmentfault.com/a/1190000003946969)
