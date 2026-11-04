---
title: "GMP 调度模型"
freq: 2
status: todo
summary: "G 是协程，M 是系统线程，P 是处理器（持有本地 G 队列），M 必须绑定 P 才能运行 G。P 的本地队列空了会从全局队列取或从其他 P 偷取（work stealing）；G 阻塞在系统调用时 M 和 P 解绑。"
---

# GMP 调度模型

> 频率：★★☆ · 参考：[Go 语言设计与实现](https://draveness.me/golang/)

## 一句话答案

G 是协程，M 是系统线程，P 是处理器（持有本地 G 队列），M 必须绑定 P 才能运行 G。P 的本地队列空了会从全局队列取或从其他 P 偷取（work stealing）；G 阻塞在系统调用时 M 和 P 解绑。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 和 Java 线程模型的区别
- 协程泄漏怎么排查
- GOMAXPROCS

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
