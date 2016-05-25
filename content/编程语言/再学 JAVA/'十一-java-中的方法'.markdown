author: Martin
date: 2015-06-12 08:04
title: (十一) Java 中的方法

和 C++ 类中的方法是差不多的东西.

定义方法:
访问修饰符 返回值类型 方法名(参数列表) {
方法主体
}

*、 访问修饰符: 方法允许被访问的权限范围, 可以是 public、protected、private 甚至可以省略.

*、 方法修饰符: 用于说明该方法的使用方式, 可以是 static 或者 省略, static 表示这是一个静态方法.

*、 返回值类型: 方法返回值的类型, 如果方法不返回任何值, 则返回值类型指定为 void; 如果方法具有返回值, 则需要指定返回值的类型, 并且在方法体中使用 return 语句返回值.

*、 方法名: 定义的方法的名字, 必须使用合法的标识符.

*、 参数列表: 传递给方法的参数列表, 参数可以有多个, 多个参数间以逗号隔开, 每个参数由参数类型和参数名组成, 以空格隔开.

访问权限:
public - 表示该方法可以被其他任何代码调用;
默认 - 则是同一个包的类可以访问;
protected - 表示同一个包的类可以访问, 其他的包的该类的子类也可以访问;
private - 表示只有自己类能访问;

方法修饰符:
如果没有指定 static, 那么当需要调用方法执行某个操作时, 要先创建类的对象, 然后通过 **对象名.方法名();** 来调用, 如:


    <span style="color: #0000ff">public</span> <span style="color: #0000ff">class</span><span style="color: #000000"> HelloWorld {
        </span><span style="color: #0000ff">public</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">void</span><span style="color: #000000"> main(String[] args) {
            HelloWorld hh </span>= <span style="color: #0000ff">new</span><span style="color: #000000"> HelloWorld();
            hh.showMyLove();
        }

        </span><span style="color: #0000ff">public</span> <span style="color: #0000ff">void</span><span style="color: #000000"> showMyLove() {
            System.out.println(</span>"我爱慕课网!"<span style="color: #000000">);
        }
    }</span>







如果指定了 static, 那么可以直接用 类名.方法名(); 直接调用, 如:



    <span style="color: #0000ff">public</span> <span style="color: #0000ff">class</span><span style="color: #000000"> HelloWorld {
        </span><span style="color: #0000ff">public</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">void</span><span style="color: #000000"> main(String[] args) {
            HelloWorld.showMyLove();
        }

        </span><span style="color: #0000ff">public</span> <span style="color: #0000ff">static</span> <span style="color: #0000ff">void</span><span style="color: #000000"> showMyLove() {
            System.out.println(</span>"我爱慕课网!"<span style="color: #000000">);
        }
    }</span>







备注: 类的 static 方法中, 如果要使用类的某个属性, 则只能使用类的静态属性, 方法中也不能写 this、super 关键字.







* * *


方法重载




和 C++ 函数重载差不多, 就不多说了, 有些小问题注意下就可以了.




1、 必须是在同一个类中且方法名相同.


2、 方法参数的个数或顺序或类型不同.


3、 与方法的修饰符或返回值没有关系.
蔮
