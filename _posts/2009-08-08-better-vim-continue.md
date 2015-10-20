---
layout: post
title:  "Better vim (Continue)"
---

许多人使用vim是迫不得已，因为当ssh到远程机器或是只有terminal的情况下，基本没有什么别的选择。他们无法理解为什么有人在自己本地的windows, linux或是mac上也使用vim，而不去用功能强大的IDE。

我对自己使用的工具非常在意，在本地使用vim的第一个原因是出于工具的连贯性。同样是进行文本编缉，若是不断在几种工具之间切换，必定不利于提升使用工具的熟练度。另一方面，vim相比目前流行的一些IDE，确实仍然有一些自己的优势。一个好的编缉器是可以大大提升coding效率，而这一提升在我看来又来源于两个方面：

1）针对编程语言的优化以及辅助功能：这其中包括变量、函数名的补全，函数声明与定义之间的跳转，自动缩进等等。虽然vim也提供了这方面的支持，但显然要弱于eclipse, xcode, netbeans, visual stuio这类IDE。

2）通用文本编缉的能力：我这里是指在一个文档中进行快速移动，删除和添加文本的能力，这是一个编缉器最基本的能力，也是vim的核心竞争力之所在。

稍有些vim使用经验的人都会用hjkl来进行移动，使手指不离开home row。也应该常常用w,b来进行word的前后移动，其实还可以用W, B来进行WORD的前后移动。注意在vim里word和WORD定义是不同的。前者可以用iskeyword来定义，而后者则由whitespace来分割。

这些仅是皮毛，不知道有多少用vim的人知道text-object? 我觉得这是vim非常实用，也很有特色的一个功能。很多人会用dw来删一个word，或是用cw来重写一个word，但在用这些命令之前你需要先把光标移动到word的第一个字符。实际上无论你的光标在word的什么位置，你都可以直接用diw, ciw来完成对整个单词的编缉。这里w就是一个text-object (word)，i表示inclusive，使操作对象仅仅为单词本身而不包括单词后面的空格。相对的还有daw, caw，aw不但包括当前的单词还包括它之后的空格。

再看个例子：

var text = “this is my second po<cursor>st about vim”

假设当前处于normal mode，光标在<cursor>位置，而你想把整个字串(this is my second post about vim)选中yank到clipboard中去。

Level 0：使用鼠标选中这个字串，然后按y(记得在vimrc里设置set mouse=a)。纯键盘则是按两下w一下e，到vim的最后一个字符，按v进入visual mode，再按7下b回到this的开始，然后按y。keystroke = wwevbbbbbbby

Level 1：keystroke = T”v,y （我很早就知道用f,F来查找字符，但t,T则晚许多，t是until的意思，也就是说会把光标移动到目标字符前一格。逗号则是反向进行上一次f,F,t,T的查找）

Level 2：keystrok = yi” (这里i”就是一个inclusive text-object，操作对象为整个双引号之内的所有文本）

vim有很多内置的text-object，除了word，单引号内文本，双引号内文本，括号内文本(包括小括号，中括号和花括号），还有tag内文本（在html/xml编缉时特别有用）。熟练的使用这些text-object绝对可以有事半功倍的效果。更有趣的是，你可以自己定义text-object，比如我就在python和javascript文件里定义了function text-object，按vaf就可以选中整个function，当然同样支持yaf, daf这些操作。

写到这里，有兴趣的话可以在vim里打:help text-objects
