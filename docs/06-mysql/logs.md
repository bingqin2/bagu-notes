---
title: "三大日志：redo、undo、binlog 与两阶段提交"
freq: 3
status: todo
summary: "redo log 是 InnoDB 的物理日志，保证崩溃恢复（WAL）；undo log 记录旧版本，用于回滚和 MVCC；binlog 是 Server 层的逻辑日志，用于主从复制和恢复。两阶段提交（redo prepare → 写 binlog → redo commit）保证两份日志一致。"
---

# 三大日志：redo、undo、binlog 与两阶段提交

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

redo log 是 InnoDB 的物理日志，保证崩溃恢复（WAL）；undo log 记录旧版本，用于回滚和 MVCC；binlog 是 Server 层的逻辑日志，用于主从复制和恢复。两阶段提交（redo prepare → 写 binlog → redo commit）保证两份日志一致。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 为什么需要两阶段提交
- binlog 的三种格式
- 刷盘策略（innodb_flush_log_at_trx_commit、sync_binlog）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
