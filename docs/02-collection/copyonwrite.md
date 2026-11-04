---
title: "CopyOnWriteArrayList 与写时复制"
freq: 1
status: todo
summary: "写操作加锁并复制一份新数组，改完再替换引用；读操作不加锁读旧数组。适合读多写少，代价是写入慢、占内存、读到的可能是旧数据。"
---

# CopyOnWriteArrayList 与写时复制

> 频率：★☆☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

写操作加锁并复制一份新数组，改完再替换引用；读操作不加锁读旧数组。适合读多写少，代价是写入慢、占内存、读到的可能是旧数据。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 和 Collections.synchronizedList 的区别
- 写时复制在 Redis RDB、Linux fork 中的应用

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
