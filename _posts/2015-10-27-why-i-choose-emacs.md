---
layout: post
title:  "聊聊为什么我转投了Emacs"
---

我用Vim已经8年了，虽然说不上是骨灰级用户，但我花在定制化Vim上的时间绝对不少，公司里的许多人也是在我怂恿之下才开始用Vim的。当年在Nvidia工作时，闲来无事，为公司Bug tracking系统写了一个Vim插件。离开多年后，依然有人在用，这似乎也是我在Nivdia唯一留下的东西，真不知道是该高兴还是悲哀。

在聊为什么转投Emacs之前，我想先说说为何我对text editor如此重视。以前在我别的文章中也谈到，程序员的大部分时间在与代码打交道，好的文本编缉器能让你长期受益，所以有投资的价值。这也是为什么我会花时间在Vim，Emacs这种功能强大，但学习曲线陡峭的编缉器上。但这个理由其实还是留于表面，还有一个更重要的想法在驱使我去不断尝试。

目前大家工作时用到的工具大致分为两类，一类是图形化界面的工具，像是Office, Evernote和IDE这些，另一类则是命令行工具，包括zsh, grep, make等。许多资深的程序员会更偏向于命令行工具，因为他们懂得unix的核心理念及其强大之处。

> Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

合理地拼接组合使看似功能单一的几个工具变得强大而有无限多的可能性。同时，优秀的程序员往往会为自己写很多的实用工具，而开发一个命令行工具的代价要远远小于一个GUI工具。但另一方面，即使对于那些10x程序员来说，GUI工具依然有它的魅力。这魅力并不来自于它们华丽的界面，而来自于实实在在工作中效率地提升。通过图形化界面，可以为当前的工作提供大量的上下文信息，IDE中的Debugger就是一个典型的例子。另外，有些数据信息以图形的方式呈现，更容易让人理解，比如数据分析中常用的走势图，饼图，就比单纯的数字表格更易消化。

虽然命令行工具与GUI工具如同光谱的两端，有着完全不同的理念，但我并不觉得它们是相互冲突的。我想要兼得两者的优点，更具体地说，我希望有这样一个平台

- 在这个平台上开发工具，就如同开发命令行工具一样简单。
- 所有的工具都以纯文本做为输入与输出，可以相互合作。
- 平台上的工具可以充分利用屏幕呈现大量信息，合理地对屏幕信息布局
- 有显示图形的能力

在我看来，有着强大可扩展性的文本编缉器，有成为这种平台的潜质。无论是Vim, Emacs, Sublime或是Atom，都有一些功能强大让人赞叹的插件。你完全可以把这些编缉器看成是一个个操作系统，而那些插件则是其上的杀手级应用。

绕了那么大一个圈子，让我回到原点，为什么我会转Emacs？因为在我所熟知的所有编缉器中，只有两个从一开始就想要成为平台，而不是单纯的编缉器，那就是Emacs和Atom。在编缉器圣战中，Vim的拥护者们经常挂在口中的一句话就是"The Emacs operating system needs a better editor."，讽刺的背后也道出了Emacs的理念，正因为Emacs是一个操作系统，如今Emacs上的Evil插件几乎完全复制了Vim的核心功能，换句话说，Vim成了Emacs操作系统上的一款应用。Richard Stallman在编写Emacs时，先用20%的C代码创造了Emacs Lisp语言，然后用剩下的80% Elisp代码创造了整个编辑器。在之后的30年里，Elisp也被用于开发各种Emacs上的插件。也就是说Emacs的插件开发者与编缉器的创造者使用的是同样的工具，所以它的扩展性才那么被人称道。Emacs那超越所有同时代软件（以及绝大部分现代软件）的思想让我不得不钦佩。当然，Emacs满足我之前所提到的对于平台的所有要求，包括图形显示，通过几行代码，就可以实现把屏幕截图直接粘贴到Emacs中的功能。(如下图)

![Emacs](/images/emacs-screenshot.png)

最后提一下Atom，它是另一个有着平台野心的编缉器，Github团队在编写Atom时创造了Electron，这是一个让开发者用web技术来搭建跨平台桌面应用的框架，比如现在大红大紫的Slack就是它开发的。从目前Atom的官方博客来看，Atom团队正在不留余力地推广Electron。我个人没有选择Atom的原因有两点

- 生态圈刚刚形成，插件数量还不够
- 虽然Web比桌面GUI要简单些，我仍然觉得编写Web界面的应用要比文本界面的应用复杂。(看到CSS就头大...)

不过我很看好Atom的未来，如果你觉得Emacs太古老，Atom是个不错的选择。
