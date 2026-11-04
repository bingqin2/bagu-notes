---
title: "CompletableFuture 与异步编排"
freq: 2
status: todo
summary: "支持链式组合异步任务（thenApply、thenCompose、allOf），默认用 ForkJoinPool.commonPool，生产环境要传自定义线程池，异常用 exceptionally 或 handle 处理。"
---

# CompletableFuture 与异步编排

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

支持链式组合异步任务（thenApply、thenCompose、allOf），默认用 ForkJoinPool.commonPool，生产环境要传自定义线程池，异常用 exceptionally 或 handle 处理。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 和 Future 的区别
- 为什么不能用默认线程池
- 多个接口并行调用、整体超时怎么做

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
