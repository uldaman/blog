Title: 04、UML 时序图
Author: Martin
Date: 2016-04-05 15:26
Summary: 描述一个时间段内不同对象之间的业务情况.

[TOC]

# 概述
__何谓时序图__:<br>
简单的说, 就是描述一个时间段内不同对象之间的业务情况(时间顺序).<br>
时序图的重点在__消息时序__上, 也就是说, 描述__消息__是如何在对象间发送和接收的, 表示了对象之间传递消息的时间顺序.

__时序图与用例图__:<br>
时序图表示了__系统__与__参与者__互动执行某一个__用例__期间, 系统内部对象间的协作情况.<br>
对于程序设计来说, 一个用例就对应一个时序图, 时序图是对系统的内部行为进行描述, 用于用例分析和设计阶段.<br>
在项目的需求阶段, 架构师会根据把__用例图__细化为一个或者更多的时序图.

虽然在开发者看来, 时序图描述的是模块(类)间的交互, 然而, 现在时序图也常常被__业务人员__用来描述业务的流程.

__在 StarUML 中新建时序图__:<br>
打开 StarUML, 选择 __Rational Approach__.<br>
<<__Logical View__\>\> \-\-\> Add Diagram \-\-\> Sequence Diagram<br>
界面左边就出现了 Sequence 工具栏.

|       StarUML       |     翻译     |
|---------------------|--------------|
| Object              | 对象         |
| Stimulus            | 消息传递     |
| SelfStimulus        | 自我消息传递 |
| Combined Fragment   | 组合碎片     |
| Interaction Operand | 交互操作域   |
| Frame               | 框架         |

# Object
时序图中 Object 的命令遵循下面的格式:

```
实体名 : 类名
```
<br>

大部分情况下, 我们可能只关心__类名__, 所以可以简写成 __: 类名__.

# Lifeline 与 Focus of Control
__生命线__在时序图中表示为从对象图标向下延伸的一条__虚线__, 表示对象存在的时间.

而__控制焦点__是__生命线__中表示时间段的符号, 在这个时间段内对象将执行相应的操作, 用小矩形表示.

![](http://i63.tinypic.com/2lxi9s1.jpg)

# Stimulus
## 消息类型
消息一般分为__同步消息__(Synchronous Message), __异步消息__(Asynchronous Message)和__返回消息__(Return Message).<br>
如下图所示:

![](http://i66.tinypic.com/euh6hi.jpg)

- 同步消息: 消息的发送者把控制传递给消息的接收者, 然后停止活动, 等待消息的接收者放弃或者返回控制
- 异步消息: 消息发送者通过消息把信号传递给消息的接收者, 然后继续自己的活动, 不等待接受者返回消息或者控制
- 返回消息: 返回消息表示从过程调用返回

对于 StarUML 而言, 同步消息的 Stimulus 为 __Call__, 异步消息的 Stimulus 为 __Send__, 返回消息的 Stimulus 为 __Return__.

![](http://i68.tinypic.com/fc06mw.jpg)

## 消息约束
当为对象的交互建模时, 有时候必须满足一个条件消息才会传递给对象.

为了在一个序列图上画一个约束, 你把约束元件放在约束的消息线上, 消息名字之前.

![](http://i64.tinypic.com/14e9vo6.jpg)

注意 Stimulus 上的 __[restraint == true]__.

# Combined Fragment
Combined Fragment 用来描述一批 Stimulus 的约束, 如上面 __消息约束__ 中的 __[restraint == true]__, 如果想要其对多条 Stimulus 生效, 就可以使用 Combined Fragment.

![](http://i68.tinypic.com/b7kubs.jpg)

只有当 restraint == true 时, Combined Fragment 里的 Stimulus 才会被触发.

Combined Fragment 左上角的 __opt__ 表示选择约束, 除了 opt 外, 还有 __loop__(循环), 甚至还支持 __if else__ 结构(__alt__).

不过要使用 __alt__, 就要配合 __Interaction Operand__ 了, 把 __Interaction Operand__ 拖放到 Combined Fragment 里就可以对 Combined Fragment 进行拆分了, 效果如下:

![](http://i66.tinypic.com/2w7pto8.jpg)

如果 restraint == true, 则执行 call\_1(), 否则执行 call\_2().
