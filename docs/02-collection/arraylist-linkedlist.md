---
title: "ArrayList 与 LinkedList"
freq: 2
status: todo
summary: "ArrayList 是动态数组，随机访问 O(1)，扩容为 1.5 倍；LinkedList 是双向链表，插入删除本身 O(1) 但要先 O(n) 找到位置。实际开发几乎总用 ArrayList，因为内存连续、缓存友好。"
---

# ArrayList 与 LinkedList

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

ArrayList 是动态数组，随机访问 O(1)，扩容为 1.5 倍；LinkedList 是双向链表，插入删除本身 O(1) 但要先 O(n) 找到位置。实际开发几乎总用 ArrayList，因为内存连续、缓存友好。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- ArrayList 扩容过程
- fail-fast 与 ConcurrentModificationException
- 怎么在遍历时安全删除

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
