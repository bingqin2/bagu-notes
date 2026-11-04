---
title: "事务：传播行为与失效场景"
freq: 3
status: todo
summary: "@Transactional 靠 AOP 代理实现。常见失效：同类内部方法调用（绕过代理）、方法不是 public、异常被吞掉、抛出受检异常（默认只回滚运行时异常）、数据库引擎不支持事务。"
---

# 事务：传播行为与失效场景

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

@Transactional 靠 AOP 代理实现。常见失效：同类内部方法调用（绕过代理）、方法不是 public、异常被吞掉、抛出受检异常（默认只回滚运行时异常）、数据库引擎不支持事务。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 七种传播行为（REQUIRED、REQUIRES_NEW、NESTED）
- 大事务的问题
- 事务里调用远程接口的问题

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
