---
title: "线上排查：OOM、Full GC 频繁、CPU 100%"
freq: 3
status: todo
summary: "OOM：加 -XX:+HeapDumpOnOutOfMemoryError 导出 dump，用 MAT 看大对象和引用链。CPU 100%：top 找进程 → top -H 找线程 → 线程 id 转十六进制 → jstack 找对应栈。Full GC 频繁：jstat 看 GC 情况，检查大对象、内存泄漏、元空间。"
---

# 线上排查：OOM、Full GC 频繁、CPU 100%

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

OOM：加 -XX:+HeapDumpOnOutOfMemoryError 导出 dump，用 MAT 看大对象和引用链。CPU 100%：top 找进程 → top -H 找线程 → 线程 id 转十六进制 → jstack 找对应栈。Full GC 频繁：jstat 看 GC 情况，检查大对象、内存泄漏、元空间。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 常用 JVM 参数
- 四核 8G 机器怎么设堆大小
- Arthas 能做什么

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
