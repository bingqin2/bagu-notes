---
title: "虚拟线程（JDK 21）"
freq: 2
status: todo
summary: "虚拟线程由 JVM 调度，挂载在少量平台线程（载体线程）上，阻塞时自动卸载，适合大量 IO 密集任务；不适合 CPU 密集任务。synchronized 块里阻塞会把载体线程「钉住」（pinning，JDK 24 起已修复）。"
---

# 虚拟线程（JDK 21）

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

虚拟线程由 JVM 调度，挂载在少量平台线程（载体线程）上，阻塞时自动卸载，适合大量 IO 密集任务；不适合 CPU 密集任务。synchronized 块里阻塞会把载体线程「钉住」（pinning，JDK 24 起已修复）。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 和平台线程、Go 协程的区别
- 为什么不要池化虚拟线程
- pinning 是什么
- ThreadLocal 在虚拟线程下的问题

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
