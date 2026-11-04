---
title: "持久化：RDB、AOF 与混合持久化"
freq: 3
status: todo
summary: "RDB 定时 fork 子进程生成快照，恢复快但可能丢最近的数据；AOF 记录每条写命令，appendfsync everysec 最多丢 1 秒，文件大要重写；4.0 起混合持久化：AOF 重写时前半部分写 RDB 格式。"
---

# 持久化：RDB、AOF 与混合持久化

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

RDB 定时 fork 子进程生成快照，恢复快但可能丢最近的数据；AOF 记录每条写命令，appendfsync everysec 最多丢 1 秒，文件大要重写；4.0 起混合持久化：AOF 重写时前半部分写 RDB 格式。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- fork 时的写时复制
- 异常停机怎么尽量不丢数据
- AOF 重写过程

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
