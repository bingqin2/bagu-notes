---
title: "消息不丢失"
freq: 3
status: todo
summary: "三个环节都要保证：生产端用同步发送 + 确认（Kafka acks=all）+ 失败重试；Broker 端多副本（min.insync.replicas ≥ 2）+ 刷盘；消费端业务处理完再手动提交 offset。"
---

# 消息不丢失

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

三个环节都要保证：生产端用同步发送 + 确认（Kafka acks=all）+ 失败重试；Broker 端多副本（min.insync.replicas ≥ 2）+ 刷盘；消费端业务处理完再手动提交 offset。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- Kafka acks 的三个取值
- RabbitMQ 的 confirm 和持久化
- 至少一次、至多一次、恰好一次

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
