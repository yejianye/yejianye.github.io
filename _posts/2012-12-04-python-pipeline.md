---
layout: post
title:  "Python – 管道式的函数调用"
---

在编程中，常常碰到需要对数据做一系列的变换。在Python中，最常见写法有两种，一种是使用List Comprehension，另一种是用`map`和`filter`。我们今天就从`map`和`filter`讲起。

map/filter方式

```python
data = filter(cond, data)
data = map(transform1, data)
data = map(transform2, data)
data = sorted(data, cmp=comparator)
```

当然从效率和内存空间上考虑，我们应该使用`itertools`，

itertools方式

```python
from itertools import imap, ifilter
data = ifilter(cond, data)
data = imap(transform1, data)
data = imap(transform2, data)
data = sorted(data, cmp=comparator)
```

这样的写法没什么问题，但是不够简洁。我们也可以将几个函数调用写在一起

```python
from itertools import imap, ifiler
data = list(map(transform2, map(transform1, filter(cond, data))))
```

上述的写法很明显有可读性问题。对*unix熟悉的朋友一定对shell中的管道(pipe)并不陌生，这是一种非常自然的处理数据的方式，如同一个产品在流水线上的加工。假设我们可以用shell来写这段代码，应该写成这样

```python
$ cat data |
  filter cond |
  map transform1 |
  map transform2 |
  sorted comparator
```

Ok, 那在python中该如何实现类似的写法呢。我有一个自己使用的小模块pipe，代码非常的简单。

```python
from itertools import imap, ifilter
from functools import partial

def pipe(data, *transforms):
    for t in transforms:
        data = t(data)
    return data

def pmap(func):
    return partial(imap, func)

def pfilter(func):
    return partial(ifilter, func)

def psort(cmp=None, key=None, reverse=False):
    return partial(sorted, cmp=cmp, key=key, reverse=reverse)
```

使用pipe模块，之前的代码可以写成

```python
from pipe import *
data = pipe(data,
    pfilter(cond),
    pmap(transform1),
    pmap(transform2),
    psort(cmp=comparator))
```

是不是简洁明了呢?

在pipe模块中，用到了`functools.partial`，它实现在functional programming中最基本的一个函数变换curly，将一个多参数的函数中一部分参数固定，形成一个单参数的函数。在我们这里，`imap`本来需要`(func, iterable)`两个参数，`partial(imap, func)`就生成了一个只需要`(iterable)`的单参函数，其效果等同于`lambda iterable: imap(func, iterable)`。
