---
title: "线程池实战：异常处理、OOM、隔离"
freq: 2
status: todo
summary: "execute 提交的任务抛异常会打印并让线程退出重建；submit 会把异常包进 Future，不调用 get() 就看不到。不同业务要用不同线程池隔离，防止一个慢业务拖垮全部。"
---

# 线程池实战：异常处理、OOM、隔离

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

execute 提交的任务抛异常会打印并让线程退出重建；submit 会把异常包进 Future，不调用 get() 就看不到。不同业务要用不同线程池隔离，防止一个慢业务拖垮全部。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- submit 和 execute 的区别
- 线程池导致 OOM 的几种情况
- 如何优雅关闭（shutdown 与 shutdownNow）
- 手写一个线程池（见算法库设计题）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
