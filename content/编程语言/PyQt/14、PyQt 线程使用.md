Title: 14、PyQt 线程使用
Author: Martin
Date: 2016-05-16 20:40
Summary: 由于 Python 的线程历史性原因, 所以在 PyQt 中还是推荐使用 Qt 的线程机制.

由于 Python 的线程历史性原因, 所以在 PyQt 中还是推荐使用 Qt 的线程机制.

[TOC]

# 初识 QThread
Qt 使用 `QThread` 来管理线程, 首先我们要从 QThread 继承一个子类, 并重写它的 `run()` 方法, 我们可以认为, run() 方法就是线程需要执行的代码, 然后在需要的时候, 调用 QThread::start() 方法启动一个线程.
最后, 还需要将 `QThread.deleteLater()` 方法与 `QThread.finished()` 信号连接起来, 以便当线程完成时, 系统可以帮我们清除线程实例.

例如:

```python
import time

class WorkThread(QThread):
    def __int__(self):
        self.finished.connect(self.deleteLater)
        super(WorkThread, self).__init__()

    def run(self):
        time.sleep(10)

workThread = WorkThread()
workThread.start()
```
<br>
需要注意, 如果你在一个类的方法里 start 一个线程, 你需要将线程实例申明为类的属性, 否则, 当你调用完这个 start 线程的类方法后, 由于方法退出, 局部的线程实例被销毁, 就会报错: `QThread: Destroyed while thread is still running`.

例如下面这样就会报错:

```python
def word_start(self):
    workThread = WorkThread()
    workThread.start()
```
<br>
要改成:

```python
def word_start(self):
    self.workThread = WorkThread()
    self.workThread.start()
```
<br>
# 线程间通信
在 Qt 中, 可以很方便的利用信号槽的机制在多线程间进行通信:

```python
import time
from PyQt4.QtCore import pyqtSignal

class WorkThread(QThread):
    sin_out = pyqtSignal()  # 定义一个信号

    def __int__(self):
        self.finished.connect(self.deleteLater)
        super(WorkThread, self).__init__()

    def run(self):
        time.sleep(10)
        self.sin_out.emit()  # 发射信号

def on_output():
    print u'线程结束'

workThread = WorkThread()
workThread.sin_out.connect(on_output)  # 连接信号槽
workThread.start()
```
<br>
# Qt 的线程同步
### 可用的类
Qt 提供以下几个类来保证线程同步问题:

- **QMutex** 提供相互排斥的锁, 或互斥量
    + **QMutexLocker** 是一个便利类, 它可以自动对 QMutex 加锁与解锁
- **QReadWriterLock** 提供了一个可以同时读/写操作的锁
    + **QWriteLocker** 与 **QReadLocker** 是便利类, 它们自动对 **QReadWriteLock** 加锁与解锁
- **QSemaphore** 提供了一个整型信号量, 是互斥量的泛化
- **QWaitCondition** 提供了一种方法, 使得线程可以在被另外线程唤醒之前一直休眠

参考资料:<br>
[Qt 多线程](http://www.cnblogs.com/NeuqUstcIim/archive/2008/08/02/1258871.html)<br>
[Qt 线程同步](http://www.cnblogs.com/findumars/p/5176046.html)

具体的例子参考上面的资料和官方文档, 这里仅解释下重点感念.

### QMutex 与 QReadWriterLock
如果使用 **QMutex**, 那么当一个线程对受保护的数据进行读的时候, 那么其它任何线程都不能对受保护的数据进行操作...

而使用 **QReadWriterLock**, 加了 **QWriteLocker** 的锁和 QMutex 效果一样, 不允许其它任何线程都不能对受保护的数据进行操作,因为我正在写数据内, 还没写完, 你读什么..<br>
但是加了 **QReadLocker** 的锁就不一样了, 它允许其它也使用 **QReadLocker** 的线程对受保护的数据进行读取, 因为大家都是读嘛, 无所谓了, 却不允许使用 **QWriteLocker** 的线程对受保护的数据进行写入, 因为必须要我读完你才能写...

### QSemaphore
QSemaphore (信号量)支持两个基本是函数, acquire() 和 release()

- acquire(n): 尝试获取 n 个资源, 如果没有足够的可用资源, 这个调用将阻塞, 直到足够的资源可用
- release(n): 释放 n 个资源, 如果释放的数量大于上面获取的数量, 则可用资源增加, 即这是一个增量的过程

**那这货的使用场景是什么呢?**

举个例子来说明这个问题可能比较好理解一点.

假设有一个餐厅, 信号量的初始值为餐厅凳子总数目, 当有客人到，他就需要凳子, 当凳子被坐下, 可用的凳子数就减少, 当客人离开, 可用的凳子数就增加, 就允许更多的人进入, 如果有 10 个人需要凳子, 但是只有 9 张凳子, 那么这 10 个人将等待, 如果有 4 个人需要凳子, 他们可以直接坐下 (这样就只剩下 5 张凳子空着，那 10 个人将等得更久), 这就类似 **QSemaphore** 的概念.

信号量的一个典型的应用就是用来控制缓冲区的读写,下面通过一个典型用例: 生产者和消费者, 来实现这二者之间的同步.

这里就不用 Python 代码了, 上一份别人的 C++ 代码: [Qt 信号量 QSemaphore](http://www.cnblogs.com/venow/archive/2012/10/15/2724943.html)

```cpp
#include <QtCore/QCoreApplication>
#include <QSemaphore>
#include <QThread>
#include <iostream>
#include <QTime>

const int DataSize = 100;
const int BufferSize = 1;
char buffer[BufferSize];

QSemaphore freeSpace(BufferSize);
QSemaphore usedSpace(0);  // 必须要用 0, 因为要和 freeSpace 共用信号, 也就是说当 freeSpace - 1 时则 usedSpace + 1, 具体看下面的详细分析

class Producer : public QThread {
protected:
    void run() {
        qsrand(QTime(0, 0, 0).secsTo(QTime::currentTime()));
        qsrand(NULL);
        for (int i = 0; i < DataSize; ++i) {
            freeSpace.acquire();
            std::cerr<<"P";
            usedSpace.release();
        }
    }
};

class Consumer : public QThread {
protected:
    void run() {
        for (int i = 0; i < DataSize; ++i) {
            usedSpace.acquire();
            std::cerr<<"C";
            freeSpace.release();
        }
        std::cerr<<std::endl;
    }
};

int main(int argc, char *argv[]) {
    Producer producer;
    Consumer consumer;
    producer.start();
    consumer.start();
    return 0;
}
```
<br>
我们来分析一下, 先来看的 producer 的 run() 方法, 好, 假设已经进入 for 循环:

- step1: `freeSpace.acquire()` 从 freeSpace 获取一个可用信号, 因为用 1 来初始化的 freeSpace, 所以这里能正常获取一个信号
- step2: 输出 P
- step3: `usedSpace.release()` 释放 usedSpace 的信号
- step4: 回到 for 循环首, `freeSpace.acquire()` 由于第一步已经获取了一个信号, 所以现在阻塞住了

但同时, consumer 也会被启动, 并进入 for 循环:

- step1: `usedSpace.acquire()` 从 usedSpace 获取一个可用信号, 由于我们开始是用 0 来初始化的 usedSpace, 所以必须等到上面 producer 执行一次第三步, 就也是为什么 usedSpace 要用 0 来初始化的原因
- step2: 输出 C
- step3: `freeSpace.release()` 释放 freeSpace 的信号, 于是上面 producer 中的第四步从阻塞中获救了...
- step4: 回到 for 循环首, `usedSpace.acquire()` 由于第一步已经获取了一个信号, 所以现在阻塞住了, 它必须要等到上面 producer 再走到第三步释放 usedSpace

我们重新按照 producer、consumer 各自执行一次的顺序理下这个过程:

- step1 (producer): `freeSpace.acquire()` 从 freeSpace 获取一个可用信号, 因为用 1 来初始化的 freeSpace, 所以这里能正常获取一个信号
- step1 (consumer): `usedSpace.acquire()` 从 usedSpace 获取一个可用信号, 由于我们开始是用 0 来初始化的 usedSpace, 所以这里阻塞住
<br><br>
- step2 (producer): 输出 P
- step2 (consumer): 阻塞中
<br><br>
- step3 (producer): `usedSpace.release()` 释放 usedSpace 的信号
- step3 (consumer): 由于上一步释放了一个 usedSpace 信号, 所以 consumer 从 step2 的阻塞中出来了, 获取一个信号
<br><br>
- step4 (producer): 回到 for 循环首, `freeSpace.acquire()` 由于 step1 已经获取了一个信号, 所以现在阻塞住了
- step4 (consumer): 输出 C
<br><br>
- step5 (producer): 阻塞中
- step5 (consumer): `freeSpace.release()` 释放 freeSpace 的信号
<br><br>
- step6 (producer): 由于上一步释放了一个 freeSpace 信号, 所以 producer 从 step4 的阻塞中出来了, 获取一个信号
- step6 (consumer): 回到 for 循环首, `usedSpace.acquire()` 由于 step3 已经获取了一个信号, 所以现在阻塞住了
<br><br>
重复这个过程 . . .

![](http://i65.tinypic.com/2yn1cad.jpg)
