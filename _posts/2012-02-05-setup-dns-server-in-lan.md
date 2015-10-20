---
layout: post
title:  "轻松架设局域网内的DNS服务器"
---

Linux下架设DNS服务器（nameserver)的传统方案是使用bind，尽管功能强大，但配置起来相当麻烦。如果你只是需要非常基本的功能，那我推荐使用dnsmasq这个工具。它几乎不用任何配置就可以直接使用了。假设局域网内有若干台机器，你希望给每台机器一个hostname，并且能让它们可以通过域名(而不是IP地址)来相互访问。那么通过下面几步操作就可以完成了：

第一步 – 安装dnsmasq
------------------

选择一台主机做你的nameserver，假设这台主机的IP是192.168.0.1。你可以在这里下载dnsmasq的源码并编译安装，如果你的linux distribution是ubuntu，可以通过apt-get直接安装

```bash
$ sudo apt-get install dnsmasq
```

第二步 – 设置/etc/hosts
---------------------

在做为nameserver的主机上配置/etc/hosts文件，将局域网上每台机器的hostname和IP写入这个文件。一个IP允许有多个hostname。以下是一个范例，其中配置了4台机器的IP和hostname。

```bash
192.168.0.1 gateway
192.168.0.2 stage0
192.168.0.3 stage1
192.168.0.4 playground
```

更发/etc/hosts后，我们需要重启dnsmasq服务，可以使用

```bash
$ sudo /etc/init.d/dnsmasq restart
```

在ubuntu环境下推荐用

```bash
$ sudo service dnsmasq restart
```

第三步 – 添加nameserver
---------------------

注意，这一步配置对局域网中每台机器都需要操作。编缉/etc/resolv.conf文件，并在文件的最前面加上局域网的nameserver的IP地址

```bash
nameserver 192.168.0.1
```

到这里，如果一切正常的话，局域网中所有机器都可以用hostname来访问其他机器了。当有新的机器加入局域网时，只需在nameserver的/etc/hosts文件中新加一行并重启dnsmasq服务即可生效。
