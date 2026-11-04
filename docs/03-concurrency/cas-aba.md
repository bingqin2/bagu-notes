---
title: "CAS 与 ABA 问题"
freq: 2
status: todo
summary: "CAS 是 CPU 提供的原子指令：比较内存值和期望值，相等才更新。问题有三个：ABA（用版本号解决，AtomicStampedReference）、自旋开销大、只能保证一个变量的原子性。"
---

# CAS 与 ABA 问题

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

CAS 是 CPU 提供的原子指令：比较内存值和期望值，相等才更新。问题有三个：ABA（用版本号解决，AtomicStampedReference）、自旋开销大、只能保证一个变量的原子性。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- AtomicInteger 的实现
- LongAdder 为什么比 AtomicLong 快
- 乐观锁和悲观锁

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
