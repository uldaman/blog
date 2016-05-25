author: Martin
date: 2015-06-13 13:37
title: (二十四) 时间的处理

如果需要处理日期和时间的相关数据, 可以使用 java.util 包中的 Date 类;
这个类最主要的作用就是获取当前时间.


    Date d = <span style="color: #0000ff">new</span> Date(); <span style="color: #008000">//</span><span style="color: #008000"> Date 类的默认无参构造方法创建出的对象就代表当前时间</span>
    <span style="color: #000000">Sysem.out.println(d);
    </span><span style="color: #008000">//</span><span style="color: #008000"> 输出结果如下:
    </span><span style="color: #008000">//</span><span style="color: #008000"> Wed Jun 11 21:10:30 CST 2015</span>







显然, 这种输出格式不是很友好, 如果想要输出成 2015-06-13 09:22:30 这种格式就需要使用 java.text 包中的 SimpleDateFormat 类;
该类可以对日期时间进行格式化, 如可以将日期转换为指定格式的文本, 也可将文本转换为日期.




*. 使用 format() 方法将日期转换为指定格式的文本



    Date d = <span style="color: #0000ff">new</span><span style="color: #000000"> Date();
    SimpleDateFormat sdf </span>= <span style="color: #0000ff">new</span> SimpleDateFormat("yyyy-MM-dd HH:mm:ss"<span style="color: #000000">);
    String today </span>=<span style="color: #000000"> sdf.format(d);
    System.out.println(today);</span>







*. 使用 parse() 方法将文本转换为日期



    String day = "2014年02月14日 10:30:25"<span style="color: #000000">;
    SimpleDateFormat df </span>= <span style="color: #0000ff">new</span> SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss"<span style="color: #000000">);
    Date date </span>=<span style="color: #000000"> df.parse(day);
    System.out.println(date);</span>




需要注意的是: 调用 SimpleDateFormat 对象的 parse() 方法时可能会出现转换异常, 即 ParseException, 因此需要进行异常处理.




* * *





Calendar 类




Date 类最主要的作用就是获得当前时间, 同时这个类里面也具有设置时间以及一些其他的功能, 但是由于本身设计的问题, 这些方法却遭到众多批评, 不建议使用, 更推荐使用 Calendar 类进行时间和日期的处理.




Calendar 类也包含在 java.util 中, 它是一个抽象类, 可以通过调用 getInstance()** **静态方法获取一个 Calendar 对象, 此对象已由当前日期时间初始化, 即默认代表当前时间, 如 Calendar c = Calendar.getInstance();




    Calendar c = Calendar.getInstance(); <span style="color: #008000">//</span><span style="color: #008000"> 创建 Calendar 对象</span>
    <span style="color: #0000ff">int</span> year =<span style="color: #000000"> c.get(Calendar.YEAR);
    </span><span style="color: #0000ff">int</span> month = c.get(Calendar.MONTH) + 1; <span style="color: #008000">//</span><span style="color: #008000"> 月是以0开始</span>
    <span style="color: #0000ff">int</span> day =<span style="color: #000000"> c.get(Calendar.DAY_OF_MONTH);
    </span><span style="color: #0000ff">int</span> hour =<span style="color: #000000"> c.get(Calendar.HOUR_OF_DAY);
    </span><span style="color: #0000ff">int</span> minute =<span style="color: #000000"> c.get(Calendar.MINUTE);
    </span><span style="color: #0000ff">int</span> second =<span style="color: #000000"> c.get(Calendar.SECOND);
    System.out.println(</span>"当前时间: " + yer + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second);

![](http://i60.tinypic.com/286sso0.jpg)





Calendar 还提供了 getTime() 方法, 用来获取 Date 对象, 完成 Calendar 和 Date 的转换, 还可通过 getTimeInMillis() 方法, 获取”从历元至现在所经过的 UTC 毫秒数”.
p?o
