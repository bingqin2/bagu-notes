---
title: "equals 与 hashCode"
freq: 2
status: todo
summary: "两个对象 equals 相等，hashCode 必须相等；重写 equals 不重写 hashCode，放进 HashMap/HashSet 时会被当成两个不同的 key。"
---

# equals 与 hashCode

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

两个对象 equals 相等，hashCode 必须相等；重写 equals 不重写 hashCode，放进 HashMap/HashSet 时会被当成两个不同的 key。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- == 和 equals 的区别
- hashCode 冲突了怎么办
- 为什么 String 的 hashCode 用 31

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
