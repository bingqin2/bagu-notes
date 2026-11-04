---
title: "排行榜、点赞、Feed 流设计"
freq: 2
status: todo
summary: "排行榜用 Redis ZSet，千万级用户可以按分数段分桶；点赞用 Set 或 Hash 记录，计数异步落库；Feed 流分推模式（写扩散）、拉模式（读扩散）和推拉结合（大 V 用拉）。"
---

# 排行榜、点赞、Feed 流设计

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

排行榜用 Redis ZSet，千万级用户可以按分数段分桶；点赞用 Set 或 Hash 记录，计数异步落库；Feed 流分推模式（写扩散）、拉模式（读扩散）和推拉结合（大 V 用拉）。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 同分时怎么排序
- 直播间点赞的热 key

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
