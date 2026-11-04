---
title: "Bean 生命周期与作用域"
freq: 2
status: todo
summary: "实例化 → 属性填充 → Aware 回调 → BeanPostProcessor 前置 → 初始化（@PostConstruct、afterPropertiesSet、init-method）→ BeanPostProcessor 后置（AOP 代理在这里生成）→ 使用 → 销毁。"
---

# Bean 生命周期与作用域

> 频率：★★☆ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

实例化 → 属性填充 → Aware 回调 → BeanPostProcessor 前置 → 初始化（@PostConstruct、afterPropertiesSet、init-method）→ BeanPostProcessor 后置（AOP 代理在这里生成）→ 使用 → 销毁。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- Bean 是线程安全的吗
- singleton 和 prototype
- BeanFactory 和 FactoryBean

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
