---
title: "TCP 三次握手、四次挥手、TIME_WAIT"
freq: 3
status: todo
summary: "三次握手同步双方初始序列号，并防止历史连接；四次挥手是因为 TCP 全双工，两个方向分别关闭。主动关闭方进入 TIME_WAIT 等 2MSL，保证最后的 ACK 能重传、旧连接的报文在网络里消失。"
---

# TCP 三次握手、四次挥手、TIME_WAIT

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

三次握手同步双方初始序列号，并防止历史连接；四次挥手是因为 TCP 全双工，两个方向分别关闭。主动关闭方进入 TIME_WAIT 等 2MSL，保证最后的 ACK 能重传、旧连接的报文在网络里消失。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- 为什么不是两次握手
- TIME_WAIT 过多怎么办
- 半连接队列和全连接队列、SYN 洪泛
- 对端突然断电怎么感知（keepalive、心跳）

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
