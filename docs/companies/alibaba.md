# 阿里

> 样本约 20 条后端面经（2025-04 至 2026-10），包括 Java 中间件、千问技术部、阿里云、高德、虎鲸文娱。样本比另外三家少，结论参考性弱一些。

## 风格

- **项目深挖 + 原理深度**：JavaGuide 的总结也是「阿里更看重项目、基础理论和理解深度」。中间件岗会问到 ZGC 染色指针这种细节。
- **Java 并发和 JVM** 出现最多；场景题以秒杀、分库分表、分布式事务为主。
- 有些轮次**没有手撕**，有手撕时多是 LRU、限流器、多线程顺序打印这类实现题。
- **Agent** 设计问得不少：执行循环、重新规划、上下文溢出、多 Agent 冲突。

## 八股与场景题

| 近两年问过的题 | 知识库条目 |
|---|---|
| ZGC 染色指针、多重映射、GC 调优 | [GC 与 ZGC](../04-jvm/gc-algorithms) |
| JVM、类加载 | [内存区域](../04-jvm/memory-areas)、[类加载](../04-jvm/class-loading) |
| HashMap 与并发容器、ConcurrentHashMap 与 CAS ABA | [HashMap](../02-collection/hashmap)、[ConcurrentHashMap](../02-collection/concurrenthashmap)、[CAS](../03-concurrency/cas-aba) |
| AQS、ThreadLocal、线程池参数 | [AQS](../03-concurrency/aqs-reentrantlock)、[ThreadLocal](../03-concurrency/threadlocal)、[线程池](../03-concurrency/thread-pool) |
| 异常体系、线程安全的集合 | [异常](../01-java-basic/exception)、[CopyOnWrite](../02-collection/copyonwrite) |
| Spring 自动配置、Bean 生命周期 | [Spring Boot](../05-spring/springboot)、[Bean 生命周期](../05-spring/bean-lifecycle) |
| MySQL 索引、隔离级别 | [索引类型](../06-mysql/index-types)、[隔离级别](../06-mysql/transaction-isolation) |
| Redis 高可用、缓存一致性、RedLock、跳表 | [高可用](../07-redis/ha-cluster)、[缓存一致性](../07-redis/cache-consistency)、[分布式锁](../07-redis/distributed-lock)、[数据结构](../07-redis/data-structures) |
| 缓存穿透 | [穿透、击穿、雪崩](../07-redis/cache-problems) |
| Kafka 投递与幂等、重复消费、并发消费丢消息、Kafka 与延迟队列 | [不丢失](../08-mq/reliability)、[幂等](../08-mq/idempotency)、[堆积与延迟队列](../08-mq/backlog) |
| 百万 QPS 秒杀、超卖、防刷 | [秒杀与防超卖](../11-distributed/seckill) |
| 分库分表、订单表分片、高并发写 | [分库分表](../06-mysql/sharding) |
| 分布式事务、支付幂等 | [分布式事务](../11-distributed/distributed-transaction)、[接口幂等](../11-distributed/idempotency) |
| 积分抽奖设计、指标聚合 | [排行榜与 Feed 流](../11-distributed/leaderboard)、[海量数据题](../11-distributed/massive-data) |
| DDD、微服务、K8s | [熔断与服务治理](../11-distributed/circuit-breaker) |
| HTTPS、浏览器请求全过程、操作系统内存 | [HTTPS](../09-network/https)、[输入 URL 到页面](../09-network/url-to-page)、[虚拟内存](../10-os/memory) |
| Agent 执行循环、ReAct 与 Plan、重新规划、中断恢复、多 Agent 冲突 | [Agent 架构](../13-ai-agent/agent-architecture) |
| MCP 工具、Agent 网关 | [工具调用、MCP 与 Skill](../13-ai-agent/tool-calling) |
| 短期/长期记忆、上下文溢出 | [记忆与上下文](../13-ai-agent/memory-context) |
| Skill 评测、幻觉防控、模型成本与准确率取舍 | [幻觉与评测](../13-ai-agent/hallucination-eval) |

## 手撕（出现过的题）

| 题目 | 次数 |
|---|---|
| [146. LRU](https://bingqin2.github.io/algo-notes/13-design/lc146) | 1 |
| [线程安全的滑动窗口限流器](https://bingqin2.github.io/algo-notes/13-design/rate-limiter) | 1 |
| [多线程顺序打印](https://bingqin2.github.io/algo-notes/13-design/producer-consumer) | 1 |
| [39. 组合总和](https://bingqin2.github.io/algo-notes/10-backtracking/lc39) | 1 |
| 笔试：[236. 树上 LCA](https://bingqin2.github.io/algo-notes/08-binary-tree/lc236)、[括号序列修复](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc20)、最大公约数 | 各 1 |
