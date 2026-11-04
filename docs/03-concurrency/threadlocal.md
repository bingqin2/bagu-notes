---
title: "ThreadLocal 原理与内存泄漏"
freq: 3
status: todo
summary: "每个线程有自己的 ThreadLocalMap，key 是 ThreadLocal 的弱引用，value 是强引用。线程池里线程不会结束，用完不 remove 的话 value 一直留着，造成内存泄漏和数据串用。"
---

# ThreadLocal 原理与内存泄漏

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

每个线程有自己的 ThreadLocalMap，key 是 ThreadLocal 的弱引用，value 是强引用。线程池里线程不会结束，用完不 remove 的话 value 一直留着，造成内存泄漏和数据串用。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 为什么 key 用弱引用
- InheritableThreadLocal 和 TransmittableThreadLocal
- 项目里用 ThreadLocal 存了什么（用户上下文）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
