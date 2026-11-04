---
title: "慢查询排查与 explain"
freq: 3
status: todo
summary: "开慢查询日志找出慢 SQL，用 explain 看 type（至少到 range）、key、rows、Extra（Using filesort、Using temporary 要警惕）；优化手段：加合适的索引、覆盖索引、避免 select *、拆分大查询。"
---

# 慢查询排查与 explain

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

开慢查询日志找出慢 SQL，用 explain 看 type（至少到 range）、key、rows、Extra（Using filesort、Using temporary 要警惕）；优化手段：加合适的索引、覆盖索引、避免 select *、拆分大查询。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 一条 SQL 从 800 ms 优化到 100 ms 的过程（准备自己项目的例子）
- explain 每列的含义
- count(*) 和 count(1)

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
