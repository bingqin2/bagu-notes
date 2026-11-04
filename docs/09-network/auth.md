---
title: "Cookie、Session、Token 与 JWT"
freq: 2
status: todo
summary: "Session 存服务端、靠 Cookie 里的 session id 关联，集群下要共享 Session（Redis）；JWT 把信息签名后放在客户端，服务端无状态，缺点是不能主动失效。"
---

# Cookie、Session、Token 与 JWT

> 频率：★★☆ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

Session 存服务端、靠 Cookie 里的 session id 关联，集群下要共享 Session（Redis）；JWT 把信息签名后放在客户端，服务端无状态，缺点是不能主动失效。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- JWT 怎么实现退出登录、续期
- 单点登录
- CSRF 和 XSS

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
