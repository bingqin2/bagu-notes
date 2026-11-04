---
title: "JMM 与 volatile"
freq: 3
status: todo
summary: "JMM 规定了可见性、有序性、原子性三个问题的规则。volatile 保证可见性（写后立即刷回主存，读时从主存读）和有序性（内存屏障禁止重排序），但不保证原子性，i++ 仍然不安全。"
---

# JMM 与 volatile

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

JMM 规定了可见性、有序性、原子性三个问题的规则。volatile 保证可见性（写后立即刷回主存，读时从主存读）和有序性（内存屏障禁止重排序），但不保证原子性，i++ 仍然不安全。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- happens-before 规则
- DCL 单例为什么要加 volatile
- volatile 和 synchronized 的区别

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
