---
title: "数据类型与底层结构（跳表、listpack）"
freq: 3
status: todo
summary: "五种基本类型：String（SDS）、List（quicklist）、Hash（listpack / 哈希表）、Set（整数集合 / 哈希表）、ZSet（listpack / 跳表 + 哈希表）。另有 Bitmap、HyperLogLog、Geo、Stream。"
---

# 数据类型与底层结构（跳表、listpack）

> 频率：★★★ · 参考：[小林coding](https://xiaolincoding.com/)

## 一句话答案

五种基本类型：String（SDS）、List（quicklist）、Hash（listpack / 哈希表）、Set（整数集合 / 哈希表）、ZSet（listpack / 跳表 + 哈希表）。另有 Bitmap、HyperLogLog、Geo、Stream。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- ZSet 为什么用跳表不用红黑树
- SDS 比 C 字符串好在哪
- 排行榜、点赞、签到分别用什么类型

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
