---
title: "AQS 与 ReentrantLock"
freq: 3
status: todo
summary: "AQS 用一个 volatile int state 表示锁状态，加一个 CLH 变体的双向等待队列；抢锁失败的线程入队并挂起。ReentrantLock、Semaphore、CountDownLatch 都基于它。ReentrantLock 支持公平/非公平、可中断、超时和多个 Condition。"
---

# AQS 与 ReentrantLock

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

AQS 用一个 volatile int state 表示锁状态，加一个 CLH 变体的双向等待队列；抢锁失败的线程入队并挂起。ReentrantLock、Semaphore、CountDownLatch 都基于它。ReentrantLock 支持公平/非公平、可中断、超时和多个 Condition。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 公平锁和非公平锁的区别
- Condition 和 wait/notify 的区别
- CountDownLatch 和 CyclicBarrier
- 读写锁、StampedLock

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
