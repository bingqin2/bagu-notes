# 美团

> 样本约 50 条后端面经（2026-03 至 2026-11），业务线包括核心本地商业、小象超市、食杂零售、AI 后端。

## 风格

- **场景题最多**：一面就可能有「40 问」式的场景追问：资金链路、binlog 对账、MQ 乱序、灰度、降级限流。
- **Java 栈**：八股以 Java 并发、MySQL、Redis、MQ 为主。
- **手撕以链表为主**：重排、K 个一组、区间反转都出现过多次；LRU 会追问泛型和过期时间。
- **AI 后端岗**很多：Agent/RAG 项目的业务价值、召回指标、Skill 设计。

## 八股与场景题

| 近两年问过的题 | 知识库条目 |
|---|---|
| 缓存一致性、双写顺序、Caffeine + Redis 多级缓存 | [缓存与数据库一致性](../07-redis/cache-consistency) |
| 缓存击穿、穿透、布隆过滤器 | [穿透、击穿、雪崩](../07-redis/cache-problems) |
| Redis 分布式锁、Redisson 续期 | [分布式锁](../07-redis/distributed-lock) |
| Redis Bitmap、ZSet、LFU、一主多从、Lua 并发 | [数据结构](../07-redis/data-structures)、[过期与淘汰](../07-redis/expiration-eviction)、[高可用](../07-redis/ha-cluster)、[Lua](../07-redis/lua-atomic) |
| 隔离级别、幻读、MVCC、聚簇索引 | [隔离级别](../06-mysql/transaction-isolation)、[MVCC](../06-mysql/mvcc)、[索引类型](../06-mysql/index-types) |
| 慢查询、索引失效、MySQL 日志顺序、binlog 模式 | [慢 SQL](../06-mysql/slow-sql)、[索引失效](../06-mysql/index-failure)、[三大日志](../06-mysql/logs) |
| 分库分表、跨片分页、分片键、主从同步 | [分库分表与主从](../06-mysql/sharding)、[深分页](../06-mysql/deep-pagination) |
| 线程池核心参数与创建流程、Future | [线程池](../03-concurrency/thread-pool)、[CompletableFuture](../03-concurrency/completablefuture) |
| synchronized 锁对象与锁升级、volatile、悲观锁乐观锁 | [synchronized](../03-concurrency/synchronized)、[JMM 与 volatile](../03-concurrency/volatile-jmm)、[CAS](../03-concurrency/cas-aba) |
| ThreadLocal、Bean 作用域 | [ThreadLocal](../03-concurrency/threadlocal)、[Bean 生命周期](../05-spring/bean-lifecycle) |
| HashMap 线程安全、头插与尾插、容器体系 | [HashMap 线程安全](../02-collection/hashmap-thread-safety)、[HashMap](../02-collection/hashmap) |
| G1 与 CMS、JVM GC 排查 | [GC](../04-jvm/gc-algorithms)、[线上排查](../04-jvm/troubleshooting) |
| Spring 循环依赖、设计模式 | [循环依赖](../05-spring/circular-dependency)、[设计模式](../05-spring/design-patterns) |
| Kafka 顺序消费、分区键、MQ 乱序 | [顺序消息](../08-mq/ordering) |
| 消息不丢、消息去重、死信、RabbitMQ 选型 | [不丢失](../08-mq/reliability)、[幂等](../08-mq/idempotency)、[选型](../08-mq/selection)、[堆积](../08-mq/backlog) |
| 支付幂等、支付回调到库存扣减的幂等链路 | [接口幂等](../11-distributed/idempotency)、[分布式事务](../11-distributed/distributed-transaction) |
| 秒杀库存、Redis 预扣库存、Kafka 异步下单、优惠券防超发 | [秒杀与防超卖](../11-distributed/seckill) |
| 令牌桶、熔断降级、CAP | [限流](../11-distributed/rate-limiting)、[熔断](../11-distributed/circuit-breaker)、[CAP](../11-distributed/cap-base) |
| 接口超时排查、系统容量 | [线上排查](../11-distributed/online-troubleshooting) |
| Raft、注册中心脑裂与选主 | [CAP 与 BASE](../11-distributed/cap-base) |
| epoll 触发模式、TCP 拥塞控制、TCP 半连接全连接队列、零拷贝 | [IO 多路复用](../10-os/io-multiplexing)、[TCP 可靠传输](../09-network/tcp-reliability)、[三次握手](../09-network/tcp-handshake)、[零拷贝](../10-os/zero-copy) |
| SSE 与跨语言通信、HTTP 流式接口 | [SSE 与 WebSocket](../09-network/sse-websocket) |
| Go 的 GMP 与 defer、Go 与 Java 差异 | [GMP](../12-go/gmp)、[Go 与 Java](../12-go/go-vs-java) |
| RAG 召回指标、向量数据库选型、双向量召回 | [RAG](../13-ai-agent/rag)、[切块与检索](../13-ai-agent/chunking-retrieval) |
| ReAct 与 Plan-Execute、多 Agent 拆分与超时重试降级、断点续跑 | [Agent 架构](../13-ai-agent/agent-architecture) |
| Skill 与 Workflow、多 Skill 路由、MCP 装配 | [工具调用、MCP 与 Skill](../13-ai-agent/tool-calling) |
| 意图识别评测、幻觉防控 | [幻觉与评测](../13-ai-agent/hallucination-eval) |
| AI Coding SOP、和 AI 的协作方式 | [AI 编程](../13-ai-agent/ai-coding) |

## 手撕（出现过的题）

| 题目 | 次数 |
|---|---|
| [143. 重排链表 / 链表交错重排](https://github.com/bingqin2/algo-notes/blob/main/docs/04-linked-list/lc143.md) | 3 |
| [25. K 个一组翻转链表](https://github.com/bingqin2/algo-notes/blob/main/docs/04-linked-list/lc25.md) | 2 |
| [146. LRU（追问泛型、过期时间）](https://github.com/bingqin2/algo-notes/blob/main/docs/13-design/lc146.md) | 2 |
| [88. 合并有序数组](https://github.com/bingqin2/algo-notes/blob/main/docs/01-array-two-pointers/lc88.md) | 2 |
| [347. 前 K 高频元素 / 692. 前 K 高频单词](https://github.com/bingqin2/algo-notes/blob/main/docs/06-heap-topk/lc347.md) | 3 |
| [92. 区间反转链表](https://github.com/bingqin2/algo-notes/blob/main/docs/04-linked-list/lc92.md)、[206. 反转链表](https://github.com/bingqin2/algo-notes/blob/main/docs/04-linked-list/lc206.md)、[19. 倒数第 N 个](https://github.com/bingqin2/algo-notes/blob/main/docs/04-linked-list/lc19.md) | 各 1 |
| [11. 盛最多水的容器](https://github.com/bingqin2/algo-notes/blob/main/docs/01-array-two-pointers/lc11.md)、[54. 螺旋矩阵](https://github.com/bingqin2/algo-notes/blob/main/docs/01-array-two-pointers/lc54.md) | 各 1 |
| [322. 零钱兑换](https://github.com/bingqin2/algo-notes/blob/main/docs/11-dynamic-programming/lc322.md)、[394. 字符串解码](https://github.com/bingqin2/algo-notes/blob/main/docs/05-stack-monotonic/lc394.md) | 各 1 |
| [525. 01 数组最长连续子数组](https://github.com/bingqin2/algo-notes/blob/main/docs/07-hash-prefix-sum/lc525.md)、[滑动窗口](https://github.com/bingqin2/algo-notes/blob/main/docs/02-sliding-window/index.md) | 各 1 |
| [快排](https://github.com/bingqin2/algo-notes/blob/main/docs/00-sorting/quick-sort.md) | 1 |
| SQL：按课程平均分排序 | 1 |
