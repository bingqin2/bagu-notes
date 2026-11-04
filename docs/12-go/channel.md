---
title: "channel 原理与无锁化思想"
freq: 2
status: todo
summary: "channel 底层是 hchan：环形缓冲区 + 发送和接收两个等待队列 + 一把互斥锁。「不要通过共享内存来通信，而要通过通信来共享内存」。"
---

# channel 原理与无锁化思想

> 频率：★★☆ · 参考：[Go 语言设计与实现](https://draveness.me/golang/)

## 一句话答案

channel 底层是 hchan：环形缓冲区 + 发送和接收两个等待队列 + 一把互斥锁。「不要通过共享内存来通信，而要通过通信来共享内存」。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 有缓冲和无缓冲的区别
- 向关闭的 channel 读写会怎样
- select 的用法

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
