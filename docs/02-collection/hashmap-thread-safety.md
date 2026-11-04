---
title: "HashMap 线程不安全：头插与尾插"
freq: 2
status: todo
summary: "JDK 7 用头插法，并发扩容会把链表变成环导致死循环；JDK 8 改成尾插，没有死循环了，但并发 put 仍会丢数据、size 不准，所以多线程要用 ConcurrentHashMap。"
---

# HashMap 线程不安全：头插与尾插

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

JDK 7 用头插法，并发扩容会把链表变成环导致死循环；JDK 8 改成尾插，没有死循环了，但并发 put 仍会丢数据、size 不准，所以多线程要用 ConcurrentHashMap。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- Hashtable、Collections.synchronizedMap 和 ConcurrentHashMap 的区别
- 线上遇到 HashMap 并发问题怎么排查

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
