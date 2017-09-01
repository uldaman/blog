author: Martin
date: 2015-06-14 15:04
title: (二十八) Scanner 类的 close() 方法引起的異常

在寫測試代碼的時候, 發現個問題:
程序的不同的地方创建多个 Scanner 对象读取鍵盤信息, 每次用完后都很自然得调用了close() 方法关掉, 当第二次調用 Scanner 对象时就会出现 NoSuchElementException: No line found 的异常.

這是因為 sc.close()会把 System.in(輸入流) 也关掉, 并且关掉之后不能再打开, 不同的 Scanner 對象虽然都是独立的对象, 但是用的是同一个输入流, 關閉 System.in 後, 再調用 Scanner 對象的 nest() 方法就會報異常.
>??
