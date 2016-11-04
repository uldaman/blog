Title: Python 高级特性之生成器表达式
Author: Martin
Date: 2016-01-26 21:32
Summary: 当列表过长, 而我们也不需要一次性获取全部数据时, 应当考虑使用生成器(generator)表达式而不是列表解析;

当列表过长, 而我们也不需要一次性获取全部数据时, 应当考虑使用生成器(**generator**)表达式而不是列表解析;

生成器表达式的语法和列表解析一样, 只不过生成器表达式是被（）括起来的, 而不是[ ], 如下:

**(exp for iter_var in iterable)**

**(exp for iter_var in iterable if cond_exp)**
```python
g = (x * x for x in range(10))
>>> g <generator object <genexpr> at 0x1022ef630>
```

如此,  我们得到的就是一个生成器, 如果想要一个一个提取元素出来, 可以通过 **next()** 函数获得 **generator** 的下一个返回值:
```python
next(g)
>>>0
next(g)
>>>1
next(g)
>>>4
.
.
.
next(g)
>>>81
next(g)
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
StopIteration
```

或者使用 **for** 循环遍历, 因为 **generator** 也是可迭代对象:
```python
g = (x * x for x in range(10))
for n in g:
    print(n)

0
1
4
9
16
25
36
49
64
81
```

生成器表达式并不真正创建数字列表, 而是返回一个生成器, 这个生成器在每次计算出一个条目后, 把这个条目“产生”(**yield**)出来;

生成器表达式使用了“惰性计算”(lazy evaluation, 也有翻译为“延迟求值”, 我以为这种按需调用 call by need 的方式翻译为惰性更好一些), 只有在检索时才被赋值(evaluated), 所以在列表比较长的情况下使用更有效(节省内存).
