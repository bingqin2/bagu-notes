---
title: "零拷贝"
freq: 2
status: todo
summary: "传统读文件再发网络要 4 次拷贝和 4 次上下文切换；sendfile 让数据在内核里直接从页缓存到网卡，省掉用户态拷贝。Kafka、Nginx 都在用。"
---

# 零拷贝

> 频率：★★☆ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

传统读文件再发网络要 4 次拷贝和 4 次上下文切换；sendfile 让数据在内核里直接从页缓存到网卡，省掉用户态拷贝。Kafka、Nginx 都在用。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- mmap 和 sendfile 的区别
- 页缓存

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
