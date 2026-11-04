# 字节跳动

> 样本约 90 条后端面经（2026-03 至 2026-11 为主），业务线包括中国交易与广告、抖音电商、抖音生活服务、TikTok、飞书、头条等。

## 风格

- **手撕最重**：几乎每轮 1–2 道，以 Hot 100 中等题为主，偶尔有非 Hot 100 的题。写不出来基本就挂。
- **八股**：Redis 和 MySQL 出现最多，其次是并发、MQ、网络。
- **AI**：RAG 和 Agent 问得非常多，包括 Agent 与 Workflow、MCP、Skill、Agent 评测。
- **Go**：广告、交易部分团队用 Go，会问 GMP 和 Go 的 GC。

## 八股与场景题

| 近两年问过的题 | 知识库条目 |
|---|---|
| 缓存一致性、Cache Aside、双写 | [缓存与数据库一致性](../07-redis/cache-consistency) |
| Redis 分布式锁、Lua 原子性、锁续期、RedLock 的局限 | [分布式锁](../07-redis/distributed-lock) |
| 布隆过滤器、缓存穿透 | [穿透、击穿、雪崩](../07-redis/cache-problems) |
| Redis 持久化、主从复制 | [持久化](../07-redis/persistence)、[高可用](../07-redis/ha-cluster) |
| Redis 大 key、热 key | [大 key 与热 key](../07-redis/big-hot-key) |
| Redis 单线程、ZSet 跳表、淘汰策略 | [为什么快](../07-redis/why-fast)、[数据结构](../07-redis/data-structures)、[过期与淘汰](../07-redis/expiration-eviction) |
| B+ 树、联合索引、覆盖索引、回表 | [索引结构](../06-mysql/index-structure)、[索引类型](../06-mysql/index-types) |
| 隔离级别、幻读、间隙锁、MVCC | [隔离级别](../06-mysql/transaction-isolation)、[MVCC](../06-mysql/mvcc)、[锁](../06-mysql/locks) |
| binlog、redo log 两阶段提交 | [三大日志](../06-mysql/logs) |
| 慢查询、索引失效、深分页 | [慢 SQL](../06-mysql/slow-sql)、[索引失效](../06-mysql/index-failure)、[深分页](../06-mysql/deep-pagination) |
| 线程池、CompletableFuture、synchronized、CAS、AQS | [线程池](../03-concurrency/thread-pool)、[CompletableFuture](../03-concurrency/completablefuture)、[synchronized](../03-concurrency/synchronized)、[CAS](../03-concurrency/cas-aba)、[AQS](../03-concurrency/aqs-reentrantlock) |
| ThreadLocal 实现与隔离 | [ThreadLocal](../03-concurrency/threadlocal) |
| 虚拟线程、JDK 新特性 | [虚拟线程](../03-concurrency/virtual-threads)、[JDK 新特性](../01-java-basic/jdk-new-features) |
| HashMap 为什么容量是 2 的幂、红黑树 | [HashMap](../02-collection/hashmap) |
| JVM 内存、GC、G1 | [内存区域](../04-jvm/memory-areas)、[GC](../04-jvm/gc-algorithms) |
| 懒汉单例的漏洞 | [volatile 与 DCL](../03-concurrency/volatile-jmm) |
| Kafka 可靠性、offset、Rebalance、消息积压 | [不丢失](../08-mq/reliability)、[Kafka 原理](../08-mq/kafka-internals)、[堆积](../08-mq/backlog) |
| 恰好一次、幂等消费、充值幂等 | [幂等](../08-mq/idempotency)、[接口幂等](../11-distributed/idempotency) |
| 令牌桶、滑动窗口、按 RPM/TPM 限流 | [限流算法](../11-distributed/rate-limiting) |
| 秒杀、优惠券限领、抢票、红包 | [秒杀与防超卖](../11-distributed/seckill) |
| 分布式事务、2PC、Saga | [分布式事务](../11-distributed/distributed-transaction) |
| 强一致与最终一致、CAP、Nacos | [CAP 与 BASE](../11-distributed/cap-base) |
| 点赞排行榜、直播评论、Feed 流推拉 | [排行榜与 Feed 流](../11-distributed/leaderboard) |
| 10 GB 文件找行号、日志 Top 10 IP | [海量数据题](../11-distributed/massive-data) |
| 429 重试导致重复扣费 | [接口幂等](../11-distributed/idempotency) |
| TCP 四次挥手、HTTP 演进、SSE 与 WebSocket | [三次握手四次挥手](../09-network/tcp-handshake)、[HTTP](../09-network/http)、[SSE 与 WebSocket](../09-network/sse-websocket) |
| 进程/线程/协程、内核态与用户态 | [进程线程协程](../10-os/process-thread)、[用户态与内核态](../10-os/scheduling) |
| GMP、Go GC | [GMP](../12-go/gmp)、[Go 与 Java](../12-go/go-vs-java) |
| RAG 切块、多知识库融合、召回评估 | [RAG](../13-ai-agent/rag)、[切块与检索](../13-ai-agent/chunking-retrieval) |
| Agent 与 Workflow、Plan-Execute-Replan、ReAct 伪代码 | [Agent 架构](../13-ai-agent/agent-architecture) |
| Tool 与 Skill、MCP | [工具调用、MCP 与 Skill](../13-ai-agent/tool-calling) |
| Agent 评测、幻觉控制 | [幻觉与评测](../13-ai-agent/hallucination-eval) |
| AI Coding 实践 | [AI 编程](../13-ai-agent/ai-coding) |

## 手撕（出现过的题）

| 题目 | 次数 |
|---|---|
| [198. 打家劫舍（含变体）](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc198) | 4 |
| [200. 岛屿数量](https://bingqin2.github.io/algo-notes/09-graph/lc200) | 4 |
| [146. LRU（含并发版）](https://bingqin2.github.io/algo-notes/13-design/lc146) | 3 |
| [3. 无重复字符的最长子串](https://bingqin2.github.io/algo-notes/02-sliding-window/lc3) | 3 |
| [25. K 个一组翻转链表](https://bingqin2.github.io/algo-notes/04-linked-list/lc25) | 3 |
| [179. 最大数](https://bingqin2.github.io/algo-notes/01-array-two-pointers/lc179) | 3 |
| [31. 下一个排列](https://bingqin2.github.io/algo-notes/01-array-two-pointers/lc31) | 2 |
| [112. 路径总和](https://bingqin2.github.io/algo-notes/08-binary-tree/lc112) | 2 |
| [300. 最长递增子序列（要求 O(n log n)）](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc300) | 2 |
| [5. 最长回文子串](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc5) | 2 |
| [102. 层序遍历 / 199. 右视图](https://bingqin2.github.io/algo-notes/08-binary-tree/lc102) | 2 |
| [53. 最大子数组和 / 152. 乘积最大](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc53) | 3 |
| [207. 课程表 / 有向图判环、循环依赖检测](https://bingqin2.github.io/algo-notes/09-graph/lc207) | 2 |
| [155. 最小栈](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc155)、[232. 用栈实现队列](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc232) | 各 1 |
| [253. 会议室 II](https://bingqin2.github.io/algo-notes/12-greedy-interval/lc253)、[22. 括号生成](https://bingqin2.github.io/algo-notes/10-backtracking/lc22)、[33. 搜索旋转数组](https://bingqin2.github.io/algo-notes/03-binary-search/lc33) | 各 1 |
| [236. 最近公共祖先](https://bingqin2.github.io/algo-notes/08-binary-tree/lc236)、[572. 另一棵树的子树](https://bingqin2.github.io/algo-notes/08-binary-tree/lc572) | 各 1 |
| [224. 基本计算器](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc224)、[32. 最长有效括号](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc32) | 各 1 |
| [46. 全排列](https://bingqin2.github.io/algo-notes/10-backtracking/lc46)、[131. 分割回文串](https://bingqin2.github.io/algo-notes/10-backtracking/lc131)、[60. 排列序列](https://bingqin2.github.io/algo-notes/10-backtracking/lc60) | 各 1 |
| [62. 不同路径](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc62)、[121. 股票](https://bingqin2.github.io/algo-notes/11-dynamic-programming/lc121) | 各 1 |
| [470. Rand7 实现 Rand10](https://bingqin2.github.io/algo-notes/14-string-math/lc470)、[384. 洗牌](https://bingqin2.github.io/algo-notes/14-string-math/lc384) | 各 1 |
| [singleflight](https://bingqin2.github.io/algo-notes/13-design/singleflight)、[流式 Top K](https://bingqin2.github.io/algo-notes/06-heap-topk/stream-topk) | 各 1 |
| [206. 反转链表](https://bingqin2.github.io/algo-notes/04-linked-list/lc206)、[19. 倒数第 N 个](https://bingqin2.github.io/algo-notes/04-linked-list/lc19)、[21. 合并有序链表](https://bingqin2.github.io/algo-notes/04-linked-list/lc21) | 各 1 |
