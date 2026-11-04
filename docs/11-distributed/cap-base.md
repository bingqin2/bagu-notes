---
title: "CAP 与 BASE、一致性模型"
freq: 2
status: todo
summary: "网络分区一定会发生，所以只能在一致性（C）和可用性（A）之间取舍：ZooKeeper 是 CP，Eureka、Nacos（AP 模式）是 AP。BASE 是基本可用 + 软状态 + 最终一致。"
---

# CAP 与 BASE、一致性模型

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

网络分区一定会发生，所以只能在一致性（C）和可用性（A）之间取舍：ZooKeeper 是 CP，Eureka、Nacos（AP 模式）是 AP。BASE 是基本可用 + 软状态 + 最终一致。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 强一致和最终一致
- Raft 选主过程
- 注册中心选型

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
