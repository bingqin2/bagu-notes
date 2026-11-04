---
title: "map 与 slice 底层"
freq: 2
status: todo
summary: "slice 是指向数组的指针 + 长度 + 容量，扩容可能换底层数组；map 是哈希表（Go 1.24 起改为 Swiss Table），不是并发安全的，并发读写会直接 panic，要用 sync.Map 或加锁。"
---

# map 与 slice 底层

> 频率：★★☆ · 参考：[Go 语言设计与实现](https://draveness.me/golang/)

## 一句话答案

slice 是指向数组的指针 + 长度 + 容量，扩容可能换底层数组；map 是哈希表（Go 1.24 起改为 Swiss Table），不是并发安全的，并发读写会直接 panic，要用 sync.Map 或加锁。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- slice 作为参数传递的坑
- sync.Map 的读写分离设计（read/dirty）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
