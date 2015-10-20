---
layout: post
title:  "为什么应该在Web开发中使用LessCSS"
---

在如今的web开发领域，新技术日新月异，但也如大浪淘沙，只有少部分真正出色的变革能得以保留。LessCSS就是其中之一。

任何新技术的引入都会带来一定的开销。以LessCSS为例，它使我的开发工具包中又多了一层依赖(lessc)，在开发测试循环中多了一步编译(less -> css)，在调试过程中又多了一层抽象，并在我的脑袋里占了一块内存来记忆它的语法。所以虽然我会时常尝试一些新技术，但只有发现特别有价值的技术才会长久使用。至今为止我只用less开发过一个网站，但我非常确定在将来所有的web开发都会使用它，而不再用原生的CSS。less有两个主要的特性，一是嵌套式结构，二是mixin，它们解决了css语法上最根本的缺陷。

先说嵌套式结构，html中的元素与css中的样式往往是一一对应的，但html的结构是嵌套式，从根结点到叶结点层层缩进，而css却是完全平铺的，它永远只有一层，样式间没有父子关系，也没有传统语言中的namespace或是scope概念。这使得html与css之间很难建立可读性良好的映射关系。less的嵌套式结构很优雅的解决了这一问题。以下是我的某个网站中导航条的html代码

```html
<div class='nav-bar'>
    <a href='/' class='logo'></a>
    <ul class='menu'>
        <li><a href='/shop'>SHOP</a></li>
        <li><a href='/about'>ABOUT</a></li>
        <li><a href='/faq'>FAQ</a></li>
        <li><a href='/contact'>CONTACT</a></li>
    </ul>
    <ul class='buttons'>
        <li class='cart'><a href='/cart'>0</a></li>
        <li class='signin'><a href='/login'>sign in</a></li>
    </ul>
</div>
```

以及它对应的Less样式代码

```css
div.nav-bar {
    width: 1024px;
    height: 185px;
    margin: 0px auto;       

    a.logo {
        display: inline-block;
        width: 179px;
        height: 143px;
        background-image: url('../images/logo.png');
    }

    ul.menu {
        display: inline-block;
        margin-left: 10px;
        li{
            display: inline-block;
            width: 128px;
            height: 110px;
            border-left: black 1px dotted;
            a {
                font-size: 20px;
                color: black;
            }
        }
    }

    ul.buttons {
        display: inline-block;
        margin-left: 40px;
        li {
            display: inline-block;
            width: 107px;
            height: 46px;
            text-align: center;
            a {
                font-size: 14px;
                color: white;
            }
        }
        li.signin {
            background-image: url('../images/nav-signin-bg.png');
        }
        li.cart {
            background-image: url('../images/nav-cart-bg.png');
        }
    }
}
```

html元素与样式间的对应关系非常清晰明了。即使你依然使用原生的css，我也建议你将css文件用less缩进方式来写，对于整体的可读性会有非常大的帮助。

再来谈谈less的mixin，它解决了css另一个根本性的问题，也就是css class难以复用的问题。以著名的twitter的bootstrap css库为例 ，如果在我的网站中一个登录按钮要复用bootstrap中按钮的样式，我在html需要这样写

```html
<button class='signin-btn btn btn-large btn-primary'>Sign In</button>
```

btn, btn-large, btn-primary都是bootstrap中的样式，分别定义的按钮的基本样式，大小和颜色。sigin-btn的class是定义在我的网站样式表里的，用来描术这个按钮相对周围元素的margin及其他属性。可以想象，为了做到css复用，网站的html的各个元素都需要被赋予许多个class。更本质的问题是这使得表现层的细节注入到了内容层(html)的结构中。这里我还没有提到class无法参数化的问题，在css中如果要定义一个可复用的圆角class，就需要对于不同大小的圆角分别定义。同样的元素当使用html + less来开发应该这样写

html代码:

```html
<button class='signin-btn'>Sign In</button>
```

less代码:

```css
.signin-btn {
	.btn;
	.btn-primary;
	.btn-large;
	margin-left: 10px;
}
```

表现层的所有细节全部被封装在less样式表中，使得html代码非常的简洁清晰。

css语言在设计之初存在很多缺陷，但如同javascript一样，由于web浏览器的兼容性问题，在可见的未来都不可能有所改变。less语言修补了css最根本的一些问题，而且非常轻量，我觉得完全可以在所有的项目中使用，百利而无一害。说到这里，很容易联想到javascript和coffeescript之间的关系，但对coffeescript做评价要难许多，以后再和大家分享。
