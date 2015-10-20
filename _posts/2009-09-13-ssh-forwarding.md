---
layout: post
title:  "SSH Forwarding"
---

其实这实在是一个老得掉牙的技术了，但因为它实在太酷，所以忍不住在这里再介绍一下。

从一个实际的问题出发，有一个MySQL的Server在远程的主机coolserver上。而我本地只能通过ssh来访问该主机，也就是用直接用mysql –host=coolserver是无法从本地直接访问那个database的。Ok，这样一来我只能很悲惨的用ssh连到coolserver，然后在server上用mysql的命令行来做数据库操作了（假设没有VNC或是X11 Forwarding）

现在我们来用ssh forwarding，假设那个数据库的端口是4001，在本地执行下面这条命令

```bash
ssh -L 4001:localhost:4001 coolserver
```

这时就有了一个本地4001端口到coolserver:4001的端口映射，这时在coolserver的MySQL Server就会如同运行在你本地机器上。

在本地启动任何的MySQL GUI Client，例如我用Sequel，在Connection的host里键入127.0.0.1，端口设为4001，直接connect就OK了。

再举个例子，有一个Perforce Server运行在远程的主机上，而你想把所有的文件都Sync到本地，用SSH Forwarding一样轻松完成，呵呵，具体步骤就不说了…

