---
title: "Kafka 原理：分区、副本、ISR、高水位、Rebalance"
freq: 2
status: todo
summary: "Topic 分为多个分区，每个分区有 leader 和 follower 副本；和 leader 保持同步的副本集合叫 ISR；高水位（HW）是所有 ISR 都确认的位置，消费者只能读到 HW 之前。消费者组成员变化会触发 Rebalance，期间停止消费。"
---

# Kafka 原理：分区、副本、ISR、高水位、Rebalance

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

Topic 分为多个分区，每个分区有 leader 和 follower 副本；和 leader 保持同步的副本集合叫 ISR；高水位（HW）是所有 ISR 都确认的位置，消费者只能读到 HW 之前。消费者组成员变化会触发 Rebalance，期间停止消费。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- Kafka 为什么快（顺序写、零拷贝、页缓存、批量）
- 怎么减少 Rebalance
- offset 存在哪

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
