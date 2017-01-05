Title: 06、Redis 发布订阅模式
Author: Martin
Date: 2016-03-28 12:40
Summary: Redis 提供了两种方式来作消息队列: 生产者/消费者 和 发布/订阅

[TOC]

## MQ 系统
Redis 提供了两种方式来作消息队列:

- 生产者/消费者模式 模式 (采用 redis 的 list 类型)
    + 一个或者多个客户端监听消息队列, 一旦消息到达, 消费者马上消费, 谁先抢到算谁的, 如果队列里没有消息, 则消费者继续监听
- 发布/订阅 模式 (redis 自实现的一种__观察者__模式)
    + 一个或多个客户端订阅消息频道, 只要发布者发布消息, 所有订阅者都能收到消息

简单的说

- 第一种队列方式, 一个任务只会被一个客户端消费
- 第二种队列方式, 一个任务会被所有客户端消费

## 发布订阅模式
这可以说是一种__观察者__模式<br>
发布订阅模式中有两个角色: __发布者__ 和 __订阅者__<br>
__订阅者__可以订阅一个或多个频道(channel)<br>
__发布者__可以向指定频道发布消息(publish)<br>
所以订阅了该频道的订阅者都将接受到该消息.

### subscribe 订阅
- subscribe channel1 channel2 ...
    + 订阅一个或多个频道
    + 如 subscribe news.it
        * 使用 subscribe 时的返回值
            - 1) "subscribe"
                + 返回值的类型: 显示订阅成功
            - 2) "news.it"
                + 订阅的频道
            - 3) (integer) 1
                + 目前已订阅的模式的数量(包含自身)
        * 接收到消息时的返回值
            - 1) "message"
                + 返回值的类型: 消息
            - 2) "news.it"
                + 消息本身的频道
            - 3) "Google buy Motorola"
                + 消息的内容

### unsubscribe 退订
- unsubscribe channe1 channe2 ...
    + 退订通过 __subscribe__ 订阅的频道
        * 如果没有频道被指定, 那么客户端通过 __subscribe__ 订阅的所有频道都会被退订

### psubscribe 订阅(RegEx)
- psubscribe mode1 mode2 ...
    + 订阅一个或多个符合给定模式(RegEx)的频道
        * \* 匹配所有字符
        * ? 匹配一个任意字符
        * \[\] 匹配字符组
        * \x 匹配转义字符
    + 如 psubscribe news.*
        * 使用 subscribe 时的返回值
            - 1) "ppsubscribe"
                + 返回值的类型: 显示订阅成功
            - 2) "news.*"
                + 订阅的频道模式
            - 3) (integer) 1
                + 目前已订阅的模式的数量(包含自身)
        * 接收到消息时的返回值
            - 1) "pmessage"
                + 返回值的类型: 消息
            - 2) "news.*"
                + 消息匹配的频道模式
            - 3) "news.it"
                + 消息本身的频道
            - 4) "Google buy Motorola"
                + 消息的内容

### punsubscribe 退订
- punsubscribe mode1 mode2 ...
    + 退订通过 __psubscribe__ 订阅的频道
        * 如果没有频道被指定, 那么客户端通过 __psubscribe__ 订阅的所有频道都会被退订


### publish 发布
- publish channel message
    + 发布消息, 返回接收到这个消息的客户端个数

### pubsub 自省
pubsub 是一个查看订阅与发布系统状态的内省命令，它由数个不同格式的子命令组成.

参考连接: [http://doc.redisfans.com/pub_sub/pubsub.html](http://doc.redisfans.com/pub_sub/pubsub.html)
