Title: 去除 golint 对 self this 的警告
Author: Martin
Date: 2017-12-01 14:00
Summary: 去除 golint 对方法接收者命名为 self、this 的警告.

[TOC]

首先, Go 官方指出不应该将方法的接收者命名为 self 和 this ([Receiver Names](https://github.com/golang/go/wiki/CodeReviewComments#receiver-names)).

但是早期的版本中并没有做这种要求, 所以很多其它面向对象语言转过来的开发会采用这种命名法, 造成的结果就是用新版的 golint 检测代码时会报一堆的命名警告, 看起来很不舒服. 此时正确的做法应该是重构代码. 如果怕麻烦的话, 也可以像我一样修改 golint 的源代码...

golint 项目地址是: [github.com/golang/lint](https://github.com/golang/lint). fork 并 clone 到本地.

将 lint 包下 lint.go 中的以下代码注释掉:

```go
if name == "this" || name == "self" {
  f.errorf(n, 1, link(ref), category("naming"), `receiver name should be a reflection of its identity; don't use generic names such as "this" or "self"`)
  return true
}
```
<br>
然后全局替换 `github.com/golang/lint` \-\> `github.com/z351522453/lint`, 修改好后 `git push`.

> 主要是因为 golint 包下 golint.go 中用全路径 import 了 lint 包 (`import "github.com/golang/lint"`), 应该把路径改成自己的 github 库路径.

最后再执行 `go get -u github.com/z351522453/lint/golint`.

或者在本地 `cd` 到 golint 包下执行 `go build -o golint` 直接生成 golint 二进制文件 (要注意是 golint 包下执行, 而不是 lint 包, 因为 main 函数在 golint.go 中).
