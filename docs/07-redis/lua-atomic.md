---
title: "Lua 脚本与原子性、Pipeline、事务"
freq: 2
status: todo
summary: "Lua 脚本在 Redis 里整段执行，期间不会插入其他命令，可以把「判断 + 修改」做成原子操作（扣库存、限流、解锁）。Pipeline 只是批量发送减少网络往返，不保证原子；MULTI 事务不支持回滚。"
---

# Lua 脚本与原子性、Pipeline、事务

> 频率：★★☆ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

Lua 脚本在 Redis 里整段执行，期间不会插入其他命令，可以把「判断 + 修改」做成原子操作（扣库存、限流、解锁）。Pipeline 只是批量发送减少网络往返，不保证原子；MULTI 事务不支持回滚。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- Lua 脚本执行时间太长会怎样
- Cluster 下 Lua 的限制（key 要在同一个槽）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
