---
title: "深分页优化"
freq: 2
status: todo
summary: "limit 100000, 10 要扫描并丢弃前 10 万行。优化：记住上一页最后的 id 用 where id > last_id limit 10（游标分页）；或者先用覆盖索引查出 id，再 join 回表。"
---

# 深分页优化

> 频率：★★☆ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

limit 100000, 10 要扫描并丢弃前 10 万行。优化：记住上一页最后的 id 用 where id > last_id limit 10（游标分页）；或者先用覆盖索引查出 id，再 join 回表。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 分库分表后跨分片怎么分页
- Elasticsearch 深分页（search_after）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
