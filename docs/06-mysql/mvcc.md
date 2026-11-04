---
title: "MVCC：版本链与 Read View"
freq: 3
status: todo
summary: "每行有隐藏列 trx_id 和 roll_pointer，旧版本通过 undo log 串成版本链。快照读时用 Read View（活跃事务列表、最小/最大事务 id）判断哪个版本可见。读已提交每次查询都生成 Read View，可重复读只在第一次查询时生成。"
---

# MVCC：版本链与 Read View

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

每行有隐藏列 trx_id 和 roll_pointer，旧版本通过 undo log 串成版本链。快照读时用 Read View（活跃事务列表、最小/最大事务 id）判断哪个版本可见。读已提交每次查询都生成 Read View，可重复读只在第一次查询时生成。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 快照读和当前读
- MVCC 能完全解决幻读吗
- undo log 什么时候删除

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
