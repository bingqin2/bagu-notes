---
title: 近两年考什么（2025–2026）
---

# 近两年考什么（2025–2026）

## 样本

统计自[面灵面经](https://mj.mianlingai.com/)聚合的牛客、脉脉面经摘要：**字节约 90 条、腾讯约 40 条、美团约 50 条、阿里约 20 条后端岗记录**，另外参考了 Java 标签下其他公司的约 70 条。时间是 2025 年 4 月到 2026 年 11 月，大部分在 2026 年。

这是摘要级的粗略计数，同一场面试可能被重复收录，只用来排优先级。另外参考了 [JavaGuide 的面试重点（2026-05 更新）](https://javaguide.cn/interview-preparation/key-points-of-interview.html)。

## 结论一：核心八股没变，排序是 Redis ≈ MySQL > 并发 > MQ > 网络 > JVM

| 排名 | 模块 | 近两年最常被问的点 |
|---|---|---|
| 1 | [Redis](/07-redis/) | [缓存一致性](/07-redis/cache-consistency)、[分布式锁](/07-redis/distributed-lock)、[穿透/击穿/雪崩](/07-redis/cache-problems)、[持久化](/07-redis/persistence)、[大 key 热 key](/07-redis/big-hot-key) |
| 2 | [MySQL](/06-mysql/) | [索引结构](/06-mysql/index-structure)、[联合索引与回表](/06-mysql/index-types)、[隔离级别与幻读](/06-mysql/transaction-isolation)、[MVCC](/06-mysql/mvcc)、[间隙锁](/06-mysql/locks)、[慢 SQL](/06-mysql/slow-sql)、[深分页](/06-mysql/deep-pagination) |
| 3 | [Java 并发](/03-concurrency/) | [线程池](/03-concurrency/thread-pool)（几乎必问）、[synchronized 锁升级](/03-concurrency/synchronized)、[AQS](/03-concurrency/aqs-reentrantlock)、[CAS](/03-concurrency/cas-aba)、[ThreadLocal](/03-concurrency/threadlocal) |
| 4 | [消息队列](/08-mq/) | [不丢失](/08-mq/reliability)、[重复消费与幂等](/08-mq/idempotency)、[顺序](/08-mq/ordering)、[堆积](/08-mq/backlog) |
| 5 | [集合](/02-collection/) | [HashMap](/02-collection/hashmap)、[ConcurrentHashMap](/02-collection/concurrenthashmap) |
| 6 | [计算机网络](/09-network/) | [三次握手四次挥手](/09-network/tcp-handshake)、[TCP 与 UDP](/09-network/tcp-udp)、[HTTPS](/09-network/https) |
| 7 | [JVM](/04-jvm/) | [内存区域](/04-jvm/memory-areas)、[GC 与 G1/ZGC](/04-jvm/gc-algorithms)、[OOM 排查](/04-jvm/troubleshooting) |
| 8 | [Spring](/05-spring/) | [循环依赖](/05-spring/circular-dependency)、[事务失效](/05-spring/transaction)、[IoC/AOP](/05-spring/ioc-aop) |

## 结论二：AI 方向已经成了后端面试的常规部分

2026 年的后端面经里，**大约一半的记录问到了 RAG、Agent 或 AI 编程**，连普通的 Java 后端岗也会问「你平时怎么用 AI 写代码」。最常见的是：

1. [RAG 流程](/13-ai-agent/rag)和[切块、混合检索](/13-ai-agent/chunking-retrieval)
2. [ReAct、Agent 与 Workflow 的区别](/13-ai-agent/agent-architecture)
3. [Function Call、MCP、Skill](/13-ai-agent/tool-calling)
4. [记忆与上下文压缩](/13-ai-agent/memory-context)
5. [幻觉控制与评测](/13-ai-agent/hallucination-eval)
6. [AI 编程的使用和验收](/13-ai-agent/ai-coding)

你的简历上有 Agent 项目，这一块要准备到能被深挖的程度。

## 结论三：场景题比背诵题多，追问更深

单纯的「HashMap put 流程」少了，更多是放在场景里问：

- **高并发写**：[秒杀与防超卖](/11-distributed/seckill)、优惠券限领、红包、抢票
- **稳定性**：[限流](/11-distributed/rate-limiting)、[熔断降级](/11-distributed/circuit-breaker)、[幂等](/11-distributed/idempotency)（重复支付、429 重试重复扣费）
- **海量数据**：[有限内存去重、Top K、找重复数](/11-distributed/massive-data)
- **线上排查**：[接口变慢、502](/11-distributed/online-troubleshooting)、[OOM 和 CPU 100%](/04-jvm/troubleshooting)
- **系统设计**：[排行榜、点赞、Feed 流](/11-distributed/leaderboard)、通知平台、带过期时间的缓存

## 结论四：新考点

- [JDK 21 虚拟线程](/03-concurrency/virtual-threads)（字节、腾讯音乐、腾讯云、老虎国际都问过）
- [ZGC](/04-jvm/gc-algorithms)（阿里中间件问到了染色指针的位布局）
- [SSE 与 WebSocket](/09-network/sse-websocket)（因为大模型流式输出）
- [Go 与 Java 的区别](/12-go/go-vs-java)、[GMP](/12-go/gmp)（字节、腾讯）

## 手撕代码

几乎每场技术面都有 1–2 道题，难度以 Hot 100 的中等题为主。近两年出现最多的（链接到算法库）：

| 题目 | 出现情况 |
|---|---|
| [146. LRU 缓存](https://bingqin2.github.io/algo-notes/13-design/lc146)（含并发版、过期时间） | 最多，字节、美团、腾讯、阿里、小红书、小米都有 |
| [链表系列](https://bingqin2.github.io/algo-notes/04-linked-list/)：反转、K 个一组、重排、区间反转 | 美团尤其多 |
| [198. 打家劫舍](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc198)、[200. 岛屿数量](https://bingqin2.github.io/algo-notes/09-graph/lc200) | 字节各 4 次 |
| [3. 无重复字符的最长子串](https://bingqin2.github.io/algo-notes/02-sliding-window/lc3)、[179. 最大数](https://bingqin2.github.io/algo-notes/01-array-two-pointers/lc179) | 字节各 3 次 |
| [Top K 系列](https://bingqin2.github.io/algo-notes/06-heap-topk/) | 美团 3 次，字节有流式 Top K |
| [手写组件](https://bingqin2.github.io/algo-notes/13-design/)：限流器、线程池、交替打印、singleflight | 腾讯、阿里、京东、字节 |
