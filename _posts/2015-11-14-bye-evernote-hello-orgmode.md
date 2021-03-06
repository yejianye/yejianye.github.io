---
layout: post
title:  "再见Evernote, 你好Orgmode"
---

我这个人记性不好，所有的事情必须写下来才不会忘记。可偏偏字又写得难看，不然定会去买本精美的手账，随身带着。幸亏打字的速度不慢，所以一直靠键盘记事。记事的软件从最初的Word，到Google Notebook（这个项目后来关了，几年后又以Google Keep重生），再到Evernote，最近这些日子又看上了Orgmode。

Evernote
--------

我是从2009年Google Notebook关站后，开始用Evernote的，至今也记了几千条的笔记。Evernote的CEO Phil说要把Evernote打造成人脑的延伸，瞬间让这个公司的愿景变得高大上起来，不过我倒是很认同这个说法，并不觉得浮夸。我在Evernote中的工作流程相当简单，有数量不多的Notebook，将笔记归为几个大类，像是工作，个人生活，技术知识等。我有两个Notebook stack，一个是Current Projects，一个是Project Archive，每一个进行中的项目都会在Current Projects的建一个独立Notebook，完成后的项目会被移到Project Archive中。 总体来说，这个流程工作得还不错，但Evernote要成为“人脑的延伸”还有很长的路要走（也不知它是否能撑到这天，近来都说这只独角兽不行了）。

先说说Evernote的长处，它非常善于捕获信息，这些信息可以来自于web，图片，声音，PDF文档，电子邮件等等。无论是在桌面端还是移动端，任何时候你都可以轻松地将外界的信息导入到Evernote中。其次，它具有很强的全文检索功能，不但可以检索笔记中的文字，甚至连PDF或是图片中的文字都可以搜索出来。

Evernote不足之处在于它的文本编缉与信息组织能力。先说文本编缉上的缺点，简而言之就是Evernote的写作体验不好，缺少Distraction-free模式，不支持Markdown。对于程序员而言，在笔记中无法方便地嵌入代码块也是一大硬伤。不过比起文本编缉，我觉得缺乏强大的信息组织能力，才是更致命的弱点。要先解释一下这里说的“信息组织”是指什么，为什么它重要？收录有价值的网页片段，或是记录你的工作日志，这只能算是原始素材的积累，它们需要被组织与提炼才能产生思想。人思考问题的方式不是自顶向下就是自下而上，最后的结果都是一个树状图，或称为层级结构。为了能记录下这种思考过程，我希望笔记软件提供两个功能

- 笔记需要支持层级结构。
- 笔记之间可以相互链接引用。

打个比方，就像写一本书，你会先收集原始素材，然后开始由总纲开始，定义章节，小节，段落，再逐步细化。首先，Evernote的单个笔记中不存在层级关系，也无法折叠或是展开笔记中的某一个段落。其次，虽然Evernote支持笔记之间的引用，但不支持引用其他笔记中某个特定位置。若是把Evernote的笔记链接比做URL，那么它就是一个不支持带#的URL。因为这两个缺点，当Evernote里的笔记多了以后，笔记间的关系非常松散，很难对笔记的内容做二次提炼。

这里我想提一下微软的OneNote。OneNote支持笔记间的层级关系，也可以生成不同层级粒度上的笔记链接，可以说完美解决了上节中提到的两大问题。不过微软在Mac上的产品，总有一种二等公民的感觉，所以我不太想用。但客观地讲，即使在Mac OSX上，OneNote也是一款比Evernote更出色的笔记软件。OneNote从去年开始发力，现在又是全平台，又是完全免费，Evernote前景堪忧啊...

Orgmode
-------

上一篇博客中提到最近我的主力编缉器从Vim转向Emacs。Orgmode做为Emacs上的杀手级应用，果然名不虚传，用了之后爱不释手。Orgmode的功能很难三言两语讲清楚，在GoogleTechTalks上有[一个著名的关于Orgmode的演讲](https://www.youtube.com/watch?v=oJTwQvgfgMM)。简单地说，你可以把Orgmode看成加强版的Markdown。Org文件里可以有无限深的层级，不但可以方便地折叠或是展开一个层级，也可以快速地在各层级间跳转。有不少Orgmode的使用者把整本书的内容写在一个org文件中，并能轻松地在各级目录间跳转。

Orgmode的链接引用功能强大，几乎可以将所有资源都转化为链接。它不但可以指向一个URL，本地的一个文件，也可以指向一封电子邮件，或是org文件中某个具体的位置。最后一点尤为实用，比Evernote只能将整个笔记转化为一个链接，强太多了。

Orgmode不仅是一个优秀的笔记软件外，还是一个出色的任务管理工具。在做项目时，我需要将项目分成多个任务，而在做每个任务时也会有工作笔记。在用Evernote的时候，我会需要一款任务管理软件来配合，像Trello, Asana或是Things。但我很不喜欢任务管理与任务笔记被分散在两个平台上的感觉。Orgmode将这两者合并为一个平台。

Orgmode对于在笔记中内嵌代码有着完美的支持。不但如此，Orgmode还可以直接执行文档中的代码，并将执行结果输出到文档中，甚至做为文档中另一段代码的输入。这是一个非常强大的功能，但已超出本文要讨论的范围，有兴趣的可以看[这个视频](http://youtu.be/1-dUkyn_fZA)。

除了以上说的几点之外，Orgmode中还有许多亮点，例如

- 支持笔记模板。
- 可以专注于某个子章节，暂时隐藏文档中所有其他内容。
- 可以对整个文档加密。(Evernote只能加密笔记中的一部分内容)

最后也是最重要的一点，因为Orgmode是Emacs的一部分，在写笔记时，可以100%利用Emacs强大的文本编缉功能。Orgmode也可以通过Emacs Lisp进行扩展，让我根据自己的工作流程来定制它。这种灵活性是Evernote或是OneNote无法比拟的。

在Orgmode中，我的工作流程与在Evernote中略有不同。在用Orgmode时，我最常用的两个笔记文件是`tasks.org`与`journal.org`。前者做任务管理，后者则是日志。在`tasks.org`文件中包含所有待处理的任务，根据优先级分为`NEXT`,`SOON`,`SOMEDAY`三级，完成的任务会被归档于`tasks.org_archive`文件中。我用`journal.org`来记录日志，包括每天做的所有事情以及产生的各种想法。日志文件以`journal_YYYY_MM.org`方式命名，每个月会生成一个新文件, `journal.org`是指向当月日志文件的一个link。每天会自动生成一个以日期为标题的新章节，不同的事件则记在自己的子标题下。

我的笔记文件并不止以上两个，对于每一个我有兴趣的领域，我都会创建一个org文件（或是一个目录），例如`server-architecture.org`, `engineering-management.org`等等。每周我会对日志文件进行整理，将其中有价值的内容提炼，添加到相应领域的文件中去，同时也会包含一个指向日志文件中原始笔记的链接。完成后，将日志文件中相应的日期标题置为“Reviewed”，这样在下次整理时我会很清楚哪些日期是还未整理的。二次提炼会驱使自己对问题做更深的思考与总结，益处颇多。

我所有的笔记文件都在一个git repo下，同时也用Dropbox进行备份。

Orgmode + Evernote
------------------

Orgmode唯一的不足之处是缺少移动端的支持，虽然有开源的[MobileOrg项目](http://mobileorg.github.io/)，但它的iOS版已经超过两年未更新了，app的界面更是已经古老到没办法看的地步。在移动端，我的主要需求是查阅过往的笔记。受[Geeknote项目](http://www.geeknote.me/)的启发，我写了一个[将Orgmode笔记同步到Evernote的程序](https://github.com/yejianye/eversync)。它的工作原理很简单，将一个git repo下所有的org文件，每一个文件生成一条对应的Evernote笔记，除普通文本外，还支持标题、列表、表格、待办事项等基本的Orgmode元素。通过这个工具，便可以在移动端利用Evernote的app来查阅我的Orgmode笔记了。

小结
----

我依然在用Evernote收集网络上的素材，例如看到好的文章，我仍会用Evernote的web clipper全文摘录下来，以备将来搜索和查阅。但我已经很少在Evernote里写东西了，所有的记录与写作转移到了Orgmode里。我对目前的工作流程很满意，所以写成博文分享给大家。其实理论上来说，即使在Evernote，也可以采取记日志，定时整理的流程。只是Evernote不适合写结构化的笔记，用OneNote或是Orgmode会更有效。有兴趣的同学，欢迎留言讨论，或是写邮件给到[yejianye@gmail.com](mailto:yejianye@gmail.com)。
