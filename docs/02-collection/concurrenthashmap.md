---
title: "ConcurrentHashMap：1.7 分段锁与 1.8 CAS + synchronized"
freq: 3
status: todo
summary: "1.7 用 Segment 分段锁；1.8 去掉分段，空桶用 CAS 插入，非空桶只锁桶的头结点（synchronized），扩容时多个线程协助迁移，读操作不加锁。"
---

# ConcurrentHashMap：1.7 分段锁与 1.8 CAS + synchronized

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

1.7 用 Segment 分段锁；1.8 去掉分段，空桶用 CAS 插入，非空桶只锁桶的头结点（synchronized），扩容时多个线程协助迁移，读操作不加锁。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- size() 怎么统计（baseCount + CounterCell）
- 为什么 key 和 value 不能为 null
- 扩容时读写怎么处理（ForwardingNode）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
