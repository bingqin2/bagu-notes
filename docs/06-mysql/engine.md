---
title: "InnoDB 与 MyISAM、一条 SQL 的执行过程"
freq: 1
status: todo
summary: "InnoDB 支持事务、行锁、外键、崩溃恢复，是默认引擎；MyISAM 只有表锁、不支持事务。SQL 执行：连接器 → 分析器 → 优化器 → 执行器 → 存储引擎。"
---

# InnoDB 与 MyISAM、一条 SQL 的执行过程

> 频率：★☆☆ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

InnoDB 支持事务、行锁、外键、崩溃恢复，是默认引擎；MyISAM 只有表锁、不支持事务。SQL 执行：连接器 → 分析器 → 优化器 → 执行器 → 存储引擎。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- Buffer Pool 的作用
- change buffer

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
