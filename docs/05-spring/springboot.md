---
title: "Spring Boot 自动配置与启动流程"
freq: 2
status: todo
summary: "@SpringBootApplication 里的 @EnableAutoConfiguration 会加载 AutoConfiguration.imports 里列出的配置类，再用 @ConditionalOnClass 等条件决定是否生效。"
---

# Spring Boot 自动配置与启动流程

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

@SpringBootApplication 里的 @EnableAutoConfiguration 会加载 AutoConfiguration.imports 里列出的配置类，再用 @ConditionalOnClass 等条件决定是否生效。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- starter 是什么、怎么写一个
- 启动流程
- 配置文件的加载顺序

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
