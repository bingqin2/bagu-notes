---
title: "IoC 与 AOP"
freq: 3
status: todo
summary: "IoC 把对象的创建和依赖注入交给容器；AOP 在不改原代码的情况下织入横切逻辑（日志、事务、权限），实现方式是动态代理：有接口用 JDK 动态代理，没有接口用 CGLIB。"
---

# IoC 与 AOP

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

IoC 把对象的创建和依赖注入交给容器；AOP 在不改原代码的情况下织入横切逻辑（日志、事务、权限），实现方式是动态代理：有接口用 JDK 动态代理，没有接口用 CGLIB。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- JDK 代理和 CGLIB 的区别
- 多个切面的执行顺序
- @Autowired 和 @Resource 的区别

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
