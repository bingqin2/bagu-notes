---
title: "死锁：条件、排查、避免"
freq: 2
status: todo
summary: "四个必要条件：互斥、占有且等待、不可剥夺、循环等待。排查用 jstack 看线程栈里的 \"Found one Java-level deadlock\"；避免的办法是按固定顺序加锁、用 tryLock 超时。"
---

# 死锁：条件、排查、避免

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

四个必要条件：互斥、占有且等待、不可剥夺、循环等待。排查用 jstack 看线程栈里的 "Found one Java-level deadlock"；避免的办法是按固定顺序加锁、用 tryLock 超时。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 数据库死锁和 Java 死锁的区别
- 写一个死锁的例子
- 线程的六种状态

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
