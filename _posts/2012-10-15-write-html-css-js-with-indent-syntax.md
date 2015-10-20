---
layout: post
title:  "以缩进式语法来写html/css/javascript"
---

刚接触Python时，对这个语言的第一印象就是它以缩进(indent)来定义code block，而不是传统的花括号或是关键字对(例如pascal的begin…end)。刚开始可能有些不习惯，但很快便觉得这种的语法非常自然简洁。对于web开发者，前台的javascript, css, html能否也以类似的语法来写呢？

使用CoffeeScript来代替Javascript
------------------------------

近一年来非常火的语言，与Dart, Typescript不同，coffeescript的每一个语句都能很直观的翻译成javascript，所以它更像是一个预编译器(pre-processor)。它也是以缩进来定义code block的。网址：http://coffeescript.org/

CoffeeScript的代码范例：

```coffeescript
class User
    _instance = null
    @current: ->
        if not _instance and Idoo.client_ctx.user
            _instance = new User(Idoo.client_ctx.user)
        return _instance
    @login: (email, password, remember, next_url) ->
        $.post("/login", {
            email: email,
            password: password,
            remember: remember,
            next_url: next_url
        })
    @logout: (next_url) ->
        $.post('/logout', {
            next_url: next_url
        })
    @signup: (email, firstname, lastname, password, next_url) ->
        $.post('/signup', {
            email: email,
            firstname: firstname,
            lastname: lastname,
            password: password,
            next_url: next_url
        })
    constructor: (data) ->
        @annoymous = if data then false else true
        if not @annoymous
            @firstname = data.firstname
            @lastname = data.lastname
            @email = data.email
```

使用Stylus来代替CSS
-----------------

与less相比, Stylus的知名度要略低一些。两者在功能上非常接近，Stylus的功能稍多一些，例如它在语法上支持分支和循环。Stylus以缩进来替代css中的花括号，并且可以省略每行结尾的分号。我有无数次发现网站的css出问题是因为漏掉了一个分号。网址：http://learnboost.github.com/stylus/

Stylus的代码范例

```
div.nav-bar
    width: 1024px
    height: 185px
    margin: 0px auto
    a.logo
        display: block
        width: 179px
        height: 143px
        background-image: url('../images/logo.png')
    ul.menu
        li
            display: inline-block
            width: 128px
            height: 110px
            border-left: black 1px dotted
            a
                font-size: 20px
                color: black
```

使用jade来写html
--------------

书写xml从来都是一件另人痛苦的事，太多冗余的代码，还常常碰到tag没有闭合的尴尬。jade的原本是node.js的模板语言，由于其简洁的语法，越来越多的人开始使用，并被port到其他语言。比如pyjade就是Python的jade实现，值得一提的是，pyjade还提供了django和flask的插件。

jade：http://jade-lang.com/

pyjade: https://github.com/SyrusAkbary/pyjade

jade的代码范例

```
doctype 5
html(lang="en")
  head
    title= pageTitle
    script(type='text/javascript')
      if (foo) {
         bar()
      }
  body
    h1 Jade - node template engine
    #container
      if youAreUsingJade
        p You are amazing
      else
        p Get on it!
```

小结
---

这些工具也许并没有什么突破性的创新，但它们让web开发更加美好了一点，这些小小的进步时常会让我在枯燥的开发过程中精神一振。与那些革命性的技术相比，它们才更让人轻松愉快。
