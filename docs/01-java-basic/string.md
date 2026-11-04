---
title: "String 不可变、常量池、StringBuilder 与 StringBuffer"
freq: 2
status: todo
summary: "String 底层数组是 final 且不对外暴露，所以不可变，可以安全地放进常量池共享；拼接多时用 StringBuilder（非线程安全、快），多线程共享时用 StringBuffer（方法加了 synchronized）。"
---

# String 不可变、常量池、StringBuilder 与 StringBuffer

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

String 底层数组是 final 且不对外暴露，所以不可变，可以安全地放进常量池共享；拼接多时用 StringBuilder（非线程安全、快），多线程共享时用 StringBuffer（方法加了 synchronized）。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- new String("a") 创建了几个对象
- intern() 的作用
- + 拼接在编译期和运行期分别怎么处理

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
