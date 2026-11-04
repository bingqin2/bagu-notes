---
title: "synchronized 原理与锁升级"
freq: 3
status: todo
summary: "编译后是 monitorenter/monitorexit 指令（方法上是 ACC_SYNCHRONIZED 标志），依赖对象头的 Mark Word。锁会从无锁 → 偏向锁 → 轻量级锁（CAS 自旋）→ 重量级锁（操作系统互斥量）逐步升级。JDK 15 起默认关闭偏向锁。"
---

# synchronized 原理与锁升级

> 频率：★★★ · 参考：[JavaGuide](https://javaguide.cn/)

## 一句话答案

编译后是 monitorenter/monitorexit 指令（方法上是 ACC_SYNCHRONIZED 标志），依赖对象头的 Mark Word。锁会从无锁 → 偏向锁 → 轻量级锁（CAS 自旋）→ 重量级锁（操作系统互斥量）逐步升级。JDK 15 起默认关闭偏向锁。

## 展开（1–2 分钟能讲完）

TODO：用自己的话写，写完合上页面讲一遍。

## 图解

TODO：用 Mermaid 画出流程或结构。

## 追问链

- synchronized 锁的是什么（实例、Class 对象）
- 和 ReentrantLock 的区别
- synchronized 和自旋锁的区别
- 可重入是怎么实现的

## 我的项目里

TODO：项目里哪里用到了它，当时为什么这么做。
