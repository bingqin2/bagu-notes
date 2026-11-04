---
title: "过期删除与内存淘汰"
freq: 3
status: todo
summary: "过期删除：惰性删除（访问时检查）+ 定期删除（每秒抽样检查）。内存满了按 maxmemory-policy 淘汰，常用 allkeys-lru；LRU 是近似算法（随机抽样），4.0 起还有 LFU。"
---

# 过期删除与内存淘汰

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

过期删除：惰性删除（访问时检查）+ 定期删除（每秒抽样检查）。内存满了按 maxmemory-policy 淘汰，常用 allkeys-lru；LRU 是近似算法（随机抽样），4.0 起还有 LFU。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- LRU 和 LFU 的区别
- Redis 的 LRU 和手写 LRU 的区别（见算法库 146）
- 主从下过期 key 怎么处理

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
