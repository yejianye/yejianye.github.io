---
layout: post
title:  "如何在电子邮件中发送敏感信息"
---

如果你需要别人在电子邮件中发送某些敏感信息给你，例如帐号密码，你会怎么做呢？明文发送当然是不安全的，那该如何加密呢？

凡是用过ssh的人对于keypair认证应该都有所了解，keypair中的public key用于加密信息，private key用于解密信息。任何人都可以通过public key向你发送密文，但因为private key只有你自己知道，所以只有你才能解密出信息的原文。

举个例子来说明一下流程，如果我需要某人发送一个管理员帐号密码给我，可以写信对他说“能否将网站管理员密码发给我，请用附件中的public key加密” 。对方收到后用我的public key加密，并将密文回复给我。如果这两封邮件的内容都被第三方获取，但依靠密文和public key，他是没办法得到原文。

Ok，那到底该如何实际操作呢？这里以RSA算法为例，很多人在使用ssh时都生成过自己的keypair，通常为`~/.ssh/id_rsa`和`~/.ssh/id_rsa.pub`。首先，我们要把openssh的public key格式转为openssl的pem格式。

```bash
$ ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PEM > pubkey.pem
```

将pubkey.pem发给对方，对方收到后就可以对信息加密

```bash
$ echo 'secret password' | openssl rsautl -encrypt -pubin -inkey pubkey.pem > secret.txt
```

当你收到密文后，就可以用你的private key解密

```bash
$ cat secret.txt | openssl rsautl -decrypt -inkey ~/.ssh/id_rsa
```

我见过一些人直接把自己的public key放在邮件的签名栏里，这的确是一个不错的主意。这样任何人都可以直接向你发送加密邮件了。
