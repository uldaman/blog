author: Martin
date: 2015-06-15 19:47
title: 02. Lua 中的面向對象

在 Cocos2d-x 中, 經常使用 Lua 作為腳本語言輔助編程, Lua 的基礎應用就不多學了, 來看一看 Lua 中的面向對象.

Lua 中本身並沒有類這個數據結構, 但是可以使用 Lua 中的 table 來為什麼面向對象中的類, 如下所示:

    People =<span style="color: #000000"> {}
    People.sayHi </span>= <span style="color: #0000ff">function</span><span style="color: #000000">()
        </span><span style="color: #ff00ff">print</span>(<span style="color: #800000">"</span><span style="color: #800000">Hi People!</span><span style="color: #800000">"</span><span style="color: #000000">)
    </span><span style="color: #0000ff">end</span>





或者可以這樣:




    <span style="color: #0000ff">function</span><span style="color: #000000"> People.sayHi()
         </span><span style="color: #ff00ff">print</span>(<span style="color: #800000">"</span><span style="color: #800000">Hi People!</span><span style="color: #800000">"</span><span style="color: #000000">)
    </span><span style="color: #0000ff">end</span>





這就相當於創建一個類 People, 那怎麼生成這個類的實例呢? 它的構造函數呢?往下看:




    People.new = <span style="color: #0000ff">function</span><span style="color: #000000">()
        </span><span style="color: #0000ff">local</span> self =<span style="color: #000000"> {}
        </span><span style="color: #0000ff">for</span> key, var <span style="color: #0000ff">in</span> <span style="color: #ff00ff">pairs</span>(People) <span style="color: #0000ff">do</span><span style="color: #000000">
            self[key] </span>=<span style="color: #000000"> var
        </span><span style="color: #0000ff">end</span>
        <span style="color: #0000ff">return</span><span style="color: #000000"> self
    </span><span style="color: #0000ff">end</span>

    <span style="color: #0000ff">local</span> p1 =<span style="color: #000000"> People.new()
    p1.sayHi()</span>





我們還可以為這個類添加帶參數的構造函數:




    People.new = <span style="color: #0000ff">function</span><span style="color: #000000">(name)
        </span><span style="color: #0000ff">local</span> self =<span style="color: #000000"> {}
        self.name </span>=<span style="color: #000000"> name;
        </span><span style="color: #0000ff">for</span> key, var <span style="color: #0000ff">in</span> <span style="color: #ff00ff">pairs</span>(People) <span style="color: #0000ff">do</span><span style="color: #000000">
            self[key] </span>=<span style="color: #000000"> var
        </span><span style="color: #0000ff">end</span>
        <span style="color: #0000ff">return</span><span style="color: #000000"> self
    </span><span style="color: #0000ff">end</span>

    <span style="color: #0000ff">local</span> p2 = People.new(<span style="color: #800000">"</span><span style="color: #800000">李四</span><span style="color: #800000">"</span><span style="color: #000000">)
    </span><span style="color: #ff00ff">print</span>(p2.name)





現在, 我們類可以通過 new() 方法來實例化了.




新問題是, 我們都知道, C++ 類有個 this 指針, 這點, 又要怎麼實現了? 可以借助 Lua 的語法糖(冒號):




    People.sayHello = <span style="color: #0000ff">function</span><span style="color: #000000">(this)
        </span><span style="color: #ff00ff">print</span>(this.name .. <span style="color: #800000">"</span><span style="color: #800000"> Say Hello!</span><span style="color: #800000">"</span><span style="color: #000000">)
    </span><span style="color: #0000ff">end</span>

    <span style="color: #0000ff">local</span> p3 = People.new(<span style="color: #800000">"</span><span style="color: #800000">張三</span><span style="color: #800000">"</span><span style="color: #000000">)
    p3:sayHello()</span>





this 指針現在也有了, 那 C++ 類可以繼承, Lua 中又怎麼實現呢?




    Man =<span style="color: #000000"> {}
    Man.new </span>= <span style="color: #0000ff">function</span><span style="color: #000000">(this)
        </span><span style="color: #0000ff">local</span> self =<span style="color: #000000"> People.new()
        </span><span style="color: #0000ff">for</span> key, var <span style="color: #0000ff">in</span> <span style="color: #ff00ff">pairs</span>(Man) <span style="color: #0000ff">do</span><span style="color: #000000">
            self[key] </span>=<span style="color: #000000"> var
        </span><span style="color: #0000ff">end</span>
        <span style="color: #0000ff">return</span><span style="color: #000000"> self
    </span><span style="color: #0000ff">end</span>





這裡先生成一個 Peolple "對象", 然後把這個對象 Key 對應的 value 替換成 Man 中 Key 對應的 value, 這樣的話, 如果 Man 中沒有 "重寫" People 中的方法, 那麼, 返回的 self 中的方法還是為 People 中的方法, 如果 "重寫" 了 People 中的方法, 因為做了替換操作, 所以返回的 self 中的方法其實是對應的 Man 中的方法, 這裡比較難理解, 我在下面錄製了個視頻來解釋這點.




然後, 我們來重寫下 sayHi() 方法:




    Man.sayHi = <span style="color: #0000ff">function()</span>
        <span style="color: #ff00ff">print</span>(<span style="color: #800000">"</span><span style="color: #800000">Hi Man</span><span style="color: #800000">"</span><span style="color: #000000">)
    </span><span style="color: #0000ff">end</span>





不管怎麼樣, 我們現在已經可以實現多態了:




    <span style="color: #0000ff">function</span><span style="color: #000000"> 多態(tab)
        tab.sayHi()
    </span><span style="color: #0000ff">end</span><span style="color: #000000">
    多態(m)</span>




<blockquote>

>
>
勘誤: 之前提到了 Lua 中的語法糖, 其實 Lua 是有個默認 self 參數的, 和 this 指針一樣, 具體參考: [http://blog.csdn.net/stormbjm/article/details/38532413](http://blog.csdn.net/stormbjm/article/details/38532413)
>
> </blockquote>



.L
