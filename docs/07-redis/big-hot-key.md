---
title: "大 key 与热 key"
freq: 3
status: todo
summary: "大 key（单个 value 过大或集合元素过多）会导致阻塞、网络拥塞、迁移慢，用 --bigkeys 或 memory usage 发现，拆分后用 unlink 异步删除。热 key 访问集中在一个分片，用本地缓存、key 加随机后缀分散、读写分离。"
---

# 大 key 与热 key

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

大 key（单个 value 过大或集合元素过多）会导致阻塞、网络拥塞、迁移慢，用 --bigkeys 或 memory usage 发现，拆分后用 unlink 异步删除。热 key 访问集中在一个分片，用本地缓存、key 加随机后缀分散、读写分离。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 怎么发现热 key（客户端统计、--hotkeys、代理层）
- 点赞系统的热 key 设计

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
