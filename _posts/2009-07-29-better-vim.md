---
layout: post
title:  "Better vim"
---

自己用vim也有两年时间了, 现在我所有的coding和文本编缉都是在vim下完成的。由于几乎所有的unix/linux based OS都会预装vim，而且这个编缉器可以通吃所有的文件类型，所以个人感觉即使不用来做主力编缉器，学习一下还是很有必要的。vim有一个很陡峭的学习曲线，高手与菜鸟的编缉效率会有天壤之别。自己对学习vim很有兴趣，也跟大家分享一些我的经验。

今天说一下多文件编缉，编缉大项目时最麻烦的就是文件之间的切换。以前用Notepad++或是一些IDE的时候都是顶部一字排开10几个tab。常常看得自己眼花，从一堆tab中找个目标真是非常痛苦。刚开始用vim时我也是用tab的，同样低效。但后来发现vim的原生多文件编缉是用buffer的，tab是在7.0之后才加入。用buffer有什么好处呢？关键是切换速度，buffer的切换是用:b <buffer_name>来完成的，而buffer_name可以很方便的用<tab>补全。比如一个buffer的名字是foo_bar.txt，你既可以用foo<tab>也可以用bar<tab>来进行补全。所以往往用2,3个字母就可以准确的定位一个buffer了。

这里再向大家推荐一个vim的plugin，[fuzzyfinder](http://www.vim.org/scripts/script.php?script_id=1984)。绝对的强大，它有点类似textmate的ctrl+T来寻找文件，有动态的popup menu提示匹配的buffer。它除了快速定位buffer以外，还可以快速的查找当前目录及子目录下的文件，tag以及tag检引的文件。我现在所有的文件切换几乎都是用fuzzyfinder完成的。让我列一个vim plugin top10，这个plugin肯定名列第一。
