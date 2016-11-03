Title: 08、pyqt 中文问题
Author: Martin
Date: 2016-05-14 20:33
Summary: 解决 PyQt 中文乱码...

这里会出现两种情况:

- 一种是中文乱码
- 另一个是报 `ascii` 错误

先用我一节笔记 `43. Python 字符编码判断` 中的内容判断下字符是什么编码...

PyQt 支持的中文是 unicode 编码, 所以如果获取到的编码是 gbk 之类的话, 就用 `decode()` 解下码, 如果是 ascii 的话, 就用 `unicode()` 编下码...
