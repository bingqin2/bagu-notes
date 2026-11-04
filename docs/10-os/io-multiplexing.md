---
title: "IO 多路复用：select、poll、epoll"
freq: 3
status: todo
summary: "select 和 poll 每次都要把全部 fd 拷贝到内核并线性扫描；epoll 用红黑树管理 fd、就绪链表返回结果，只返回就绪的 fd。epoll 有水平触发（LT）和边缘触发（ET）两种模式。"
---

# IO 多路复用：select、poll、epoll

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

select 和 poll 每次都要把全部 fd 拷贝到内核并线性扫描；epoll 用红黑树管理 fd、就绪链表返回结果，只返回就绪的 fd。epoll 有水平触发（LT）和边缘触发（ET）两种模式。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- ET 模式为什么要配合非阻塞 IO
- Reactor 模型
- BIO、NIO、AIO

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
