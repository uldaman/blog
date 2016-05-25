author: Martin
date: 2015-09-14 03:56
title: 自定义 cookies

Django cookies 操作
设置: response.set_cookie(key, value)
获取 request.COOKIES.get(key, default)

HTML cookies 操作
需要引用 jquery.js 和 jquery.cookies.js 两个文件
设置: $.cookie(key, value, path), 如: $.cookie(‘pager_num’, 10, { path:'/’})
获取: $.cookie(key)

cookies 一般要 server 端和 ui 端配合展示, 例如, 可以在 html 中设置 cookie, 然后在 django 中获取、判断、使用, 也可以在 django 中设置, 然后在 html 中获取、判断、使用.

**上案例:**

Django 端:


    <span style="color: #0000ff">def</span><span style="color: #000000"> All(request, p):
        loginDict </span>= request.session.get(<span style="color: #800000">'</span><span style="color: #800000">is_login</span><span style="color: #800000">'</span><span style="color: #000000">, None)
        </span><span style="color: #0000ff">if</span><span style="color: #000000"> loginDict :
            currentPage </span>=<span style="color: #000000"> int(p)
            nPage </span>= int(request.COOKIES.get(<span style="color: #800000">'</span><span style="color: #800000">page_num</span><span style="color: #800000">'</span>, 5)) <span style="color: #008000">#</span><span style="color: #008000"> 当前设置的显示多少条</span>
            start = nPage * (currentPage - 1<span style="color: #000000">)
            end </span>= nPage *<span style="color: #000000"> currentPage
            itemList </span>=<span style="color: #000000"> Asset.objects.all()[start : end]

            nMaxCount </span>=<span style="color: #000000"> Asset.objects.all().count()
            nPages </span>= (nMaxCount + nPage -1)//<span style="color: #000000"> nPage
            pageList </span>=<span style="color: #000000"> []


            </span><span style="color: #0000ff">if</span> currentPage > 1<span style="color: #000000">:
                pre_herf </span>= <span style="color: #800000">'</span><span style="color: #800000"><a href="/web/all/%d">上一页</a></span><span style="color: #800000">'</span> % (currentPage - 1<span style="color: #000000">)
                pageList.append(mark_safe(pre_herf))

            </span><span style="color: #0000ff">for</span> x <span style="color: #0000ff">in</span> range(1,nPages + 1<span style="color: #000000">):
                herf </span>= <span style="color: #800000">'</span><span style="color: #800000"><a href="/web/all/%d">%d</a></span><span style="color: #800000">'</span> %<span style="color: #000000"> (x, x)
                pageList.append(mark_safe(herf))

            </span><span style="color: #0000ff">if</span> currentPage <<span style="color: #000000"> nPages:
                next_herf </span>= <span style="color: #800000">'</span><span style="color: #800000"><a href="/web/all/%d">下一页</a></span><span style="color: #800000">'</span> % (currentPage + 1<span style="color: #000000">)
                pageList.append(mark_safe(next_herf))

            result </span>= render_to_response(<span style="color: #800000">'</span><span style="color: #800000">index.html</span><span style="color: #800000">'</span><span style="color: #000000">,
                                        {</span><span style="color: #800000">'</span><span style="color: #800000">data</span><span style="color: #800000">'</span><span style="color: #000000">:itemList,
                                         </span><span style="color: #800000">'</span><span style="color: #800000">count</span><span style="color: #800000">'</span><span style="color: #000000">:nMaxCount,
                                         </span><span style="color: #800000">'</span><span style="color: #800000">pages</span><span style="color: #800000">'</span><span style="color: #000000">:nPages,
                                         </span><span style="color: #800000">'</span><span style="color: #800000">pageList</span><span style="color: #800000">'</span><span style="color: #000000">:pageList,
                                         </span><span style="color: #800000">'</span><span style="color: #800000">user</span><span style="color: #800000">'</span>:loginDict[<span style="color: #800000">'</span><span style="color: #800000">user</span><span style="color: #800000">'</span><span style="color: #000000">]})
            </span><span style="color: #008000">#</span><span style="color: #008000"> result.set_cookie('page_num', nPages) # 设置 cookie</span>
            <span style="color: #0000ff">return</span><span style="color: #000000"> result

        </span><span style="color: #0000ff">return</span> redirect(<span style="color: #800000">'</span><span style="color: #800000">/web/login</span><span style="color: #800000">'</span>)


HTML 端:



    <span style="color: #0000ff"><!</span><span style="color: #ff00ff">DOCTYPE html</span><span style="color: #0000ff">></span>
    <span style="color: #0000ff"><</span><span style="color: #800000">html</span><span style="color: #0000ff">></span>
    <span style="color: #0000ff"><</span><span style="color: #800000">head </span><span style="color: #ff0000">lang</span><span style="color: #0000ff">="en"</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">meta </span><span style="color: #ff0000">charset</span><span style="color: #0000ff">="UTF-8"</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">title</span><span style="color: #0000ff">></span>你好<span style="color: #0000ff"></</span><span style="color: #800000">title</span><span style="color: #0000ff">></span>
    <span style="color: #0000ff"></</span><span style="color: #800000">head</span><span style="color: #0000ff">></span>
    <span style="color: #0000ff"><</span><span style="color: #800000">body</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">div</span><span style="color: #0000ff">></span><span style="color: #000000">
            用户: {{user}}
        </span><span style="color: #0000ff"></</span><span style="color: #800000">div</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">div</span><span style="color: #0000ff">></span>
            <span style="color: #0000ff"><</span><span style="color: #800000">table </span><span style="color: #ff0000">border</span><span style="color: #0000ff">="1px"</span><span style="color: #0000ff">></span><span style="color: #000000">
                {% for item in data %}
                    </span><span style="color: #0000ff"><</span><span style="color: #800000">tr</span><span style="color: #0000ff">></span>
                        <span style="color: #0000ff"><</span><span style="color: #800000">td</span><span style="color: #0000ff">></span>{{item.id}}<span style="color: #0000ff"></</span><span style="color: #800000">td</span><span style="color: #0000ff">></span>
                        <span style="color: #0000ff"><</span><span style="color: #800000">td</span><span style="color: #0000ff">></span>{{item.hostName}}<span style="color: #0000ff"></</span><span style="color: #800000">td</span><span style="color: #0000ff">></span>
                    <span style="color: #0000ff"></</span><span style="color: #800000">tr</span><span style="color: #0000ff">></span><span style="color: #000000">
                {% endfor %}
            </span><span style="color: #0000ff"></</span><span style="color: #800000">table</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"></</span><span style="color: #800000">div</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">div</span><span style="color: #0000ff">></span><span style="color: #000000">
            总条数: {{count}}
        </span><span style="color: #0000ff"></</span><span style="color: #800000">div</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">div</span><span style="color: #0000ff">></span><span style="color: #000000">
            总页: {{pages}}
            </span><span style="color: #0000ff"><</span><span style="color: #800000">select </span><span style="color: #ff0000">id</span><span style="color: #0000ff">="s1"</span><span style="color: #ff0000"> onchange</span><span style="color: #0000ff">="OnChange(this);"</span><span style="color: #0000ff">></span>
                <span style="color: #0000ff"><</span><span style="color: #800000">option </span><span style="color: #ff0000">value </span><span style="color: #0000ff">="5"</span><span style="color: #0000ff">></span>5<span style="color: #0000ff"></</span><span style="color: #800000">option</span><span style="color: #0000ff">></span>
                <span style="color: #0000ff"><</span><span style="color: #800000">option </span><span style="color: #ff0000">value </span><span style="color: #0000ff">="10"</span><span style="color: #0000ff">></span>10<span style="color: #0000ff"></</span><span style="color: #800000">option</span><span style="color: #0000ff">></span>
                <span style="color: #0000ff"><</span><span style="color: #800000">option </span><span style="color: #ff0000">value</span><span style="color: #0000ff">="15"</span><span style="color: #0000ff">></span>15<span style="color: #0000ff"></</span><span style="color: #800000">option</span><span style="color: #0000ff">></span>
            <span style="color: #0000ff"></</span><span style="color: #800000">select</span><span style="color: #0000ff">></span>
            <span style="color: #0000ff"><</span><span style="color: #800000">br</span><span style="color: #0000ff">/></span><span style="color: #000000">
            {% for item in pageList %}
                </span><span style="color: #0000ff"><</span><span style="color: #800000">span</span><span style="color: #0000ff">></span>{{item}}<span style="color: #0000ff"></</span><span style="color: #800000">span</span><span style="color: #0000ff">></span><span style="color: #000000">
            {% endfor %}
        </span><span style="color: #0000ff"></</span><span style="color: #800000">div</span><span style="color: #0000ff">></span>
    <span style="color: #0000ff"></</span><span style="color: #800000">body</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">script </span><span style="color: #ff0000">src</span><span style="color: #0000ff">="/static/jquery-1.11.3.js"</span><span style="color: #0000ff">></</span><span style="color: #800000">script</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">script </span><span style="color: #ff0000">src</span><span style="color: #0000ff">="/static/jquery.cookie.js"</span><span style="color: #0000ff">></</span><span style="color: #800000">script</span><span style="color: #0000ff">></span>
        <span style="color: #0000ff"><</span><span style="color: #800000">script </span><span style="color: #ff0000">type</span><span style="color: #0000ff">="text/javascript"</span><span style="color: #0000ff">></span><span style="color: #000000; background-color: #f5f5f5">
            $(</span><span style="color: #0000ff; background-color: #f5f5f5">function</span><span style="color: #000000; background-color: #f5f5f5">() {
                </span><span style="color: #0000ff; background-color: #f5f5f5">var</span><span style="color: #000000; background-color: #f5f5f5"> nPage </span><span style="color: #000000; background-color: #f5f5f5">=</span><span style="color: #000000; background-color: #f5f5f5"> $.cookie(</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">page_num</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">);
                </span><span style="color: #0000ff; background-color: #f5f5f5">if</span><span style="color: #000000; background-color: #f5f5f5"> (nPage) {
                    $(</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">#s1</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">).val(nPage);
                } </span><span style="color: #0000ff; background-color: #f5f5f5">else</span><span style="color: #000000; background-color: #f5f5f5"> {

                }
            })();

            </span><span style="color: #0000ff; background-color: #f5f5f5">function</span><span style="color: #000000; background-color: #f5f5f5"> OnChange(arg) {
                </span><span style="color: #0000ff; background-color: #f5f5f5">var</span><span style="color: #000000; background-color: #f5f5f5"> nPage </span><span style="color: #000000; background-color: #f5f5f5">=</span><span style="color: #000000; background-color: #f5f5f5"> $(arg).val();
                $.cookie(</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">page_num</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">, nPage, { path : </span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5">/</span><span style="color: #000000; background-color: #f5f5f5">'</span><span style="color: #000000; background-color: #f5f5f5"> });
            }
        </span><span style="color: #0000ff"></</span><span style="color: #800000">script</span><span style="color: #0000ff">></span>
    <span style="color: #0000ff"></</span><span style="color: #800000">html</span><span style="color: #0000ff">></span>
   
