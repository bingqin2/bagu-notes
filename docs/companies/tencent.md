# 腾讯

> 样本约 40 条后端/后台面经（2025-09 至 2026-10），事业群包括 WXG（微信）、IEG（游戏）、TEG、CSIG（腾讯云）、PCG（QQ、视频）。

## 风格

- **计算机基础最深**：操作系统和网络会一路追问（epoll ET/LT、TIME_WAIT 与 MSL、零拷贝、C10K、overcommit、键盘输入到屏幕显示）。
- **语言**：后台岗很多用 C++ 或 Go，Java 岗也会问 Go 与 Java 的区别。
- **手撕**：偏「实现题」：字符串压缩解压、交替打印、IP 转整数、限流器、快速幂取模、大数乘法。
- **WXG** 项目深挖极深，可能整场不问八股；**AI** 问题集中在 Agent 上下文、Skill 按需加载。

## 八股与场景题

| 近两年问过的题 | 知识库条目 |
|---|---|
| JMM、volatile 与 synchronized | [JMM 与 volatile](../03-concurrency/volatile-jmm)、[synchronized](../03-concurrency/synchronized) |
| HashMap 红黑树、ConcurrentHashMap、带锁 Map 的 read/dirty 设计 | [HashMap](../02-collection/hashmap)、[ConcurrentHashMap](../02-collection/concurrenthashmap)、[Go map 与 sync.Map](../12-go/map-slice) |
| 线程池参数与拒绝策略、Future 异常 | [线程池](../03-concurrency/thread-pool)、[线程池实战](../03-concurrency/thread-pool-practice) |
| 线上 OOM / Full GC 排查 | [线上排查](../04-jvm/troubleshooting) |
| JDK 21 虚拟线程与 GC | [虚拟线程](../03-concurrency/virtual-threads)、[GC](../04-jvm/gc-algorithms) |
| B+ 树、索引失效、索引下推、InnoDB 加锁 | [索引结构](../06-mysql/index-structure)、[索引失效](../06-mysql/index-failure)、[索引类型](../06-mysql/index-types)、[锁](../06-mysql/locks) |
| 深分页慢查询、缓存双写与 binlog 同步 | [深分页](../06-mysql/deep-pagination)、[缓存一致性](../07-redis/cache-consistency) |
| Redis 数据类型与跳表、Lua、Cluster 故障转移 | [数据结构](../07-redis/data-structures)、[Lua](../07-redis/lua-atomic)、[高可用](../07-redis/ha-cluster) |
| 本地缓存与 Redis 同步、冷热 key 预热、single-flight | [缓存一致性](../07-redis/cache-consistency)、[大 key 热 key](../07-redis/big-hot-key)、[击穿](../07-redis/cache-problems) |
| Kafka 投递与重复消费、至少一次语义 | [不丢失](../08-mq/reliability)、[幂等](../08-mq/idempotency) |
| 限流器（固定/滑动窗口）、热点限流器内存优化 | [限流算法](../11-distributed/rate-limiting) |
| 10 亿 QQ 号找唯一数、QQ 号去重 | [海量数据题](../11-distributed/massive-data) |
| 负载均衡、服务发现与注册中心高可用、RPC 框架设计 | [熔断与服务治理](../11-distributed/circuit-breaker)、[CAP](../11-distributed/cap-base) |
| 微信扫码支付断网、支付流程 | [接口幂等](../11-distributed/idempotency)、[分布式事务](../11-distributed/distributed-transaction) |
| TCP 三次握手四次挥手、TIME_WAIT、对端断电感知、粘包 | [三次握手四次挥手](../09-network/tcp-handshake)、[TCP 与 UDP](../09-network/tcp-udp) |
| QUIC、KCP、HTTP 长短连接、HTTPS | [HTTP](../09-network/http)、[HTTPS](../09-network/https) |
| WebSocket 认证 | [SSE 与 WebSocket](../09-network/sse-websocket) |
| epoll ET/LT、IO 多路复用、零拷贝、C10K | [IO 多路复用](../10-os/io-multiplexing)、[零拷贝](../10-os/zero-copy) |
| 内存申请与 OOM、overcommit、进程与协程 | [虚拟内存](../10-os/memory)、[进程线程协程](../10-os/process-thread) |
| 原码反码补码、键盘输入到屏幕显示 | [用户态与内核态](../10-os/scheduling)、[输入 URL 到页面](../09-network/url-to-page) |
| Go map 并发安全、Channel 的无锁思想、Go 与 Java | [map 与 slice](../12-go/map-slice)、[channel](../12-go/channel)、[Go 与 Java](../12-go/go-vs-java) |
| RAG 与混合检索 | [RAG](../13-ai-agent/rag)、[切块与检索](../13-ai-agent/chunking-retrieval) |
| Skill 按需加载、Prefix Cache、上下文压缩、长 Tool Result | [工具调用与 Skill](../13-ai-agent/tool-calling)、[记忆与上下文](../13-ai-agent/memory-context) |
| Agent Loop、Agent 评测、行为漂移 | [Agent 架构](../13-ai-agent/agent-architecture)、[幻觉与评测](../13-ai-agent/hallucination-eval) |
| AI 代码的验收与合入 | [AI 编程](../13-ai-agent/ai-coding) |

## 手撕（出现过的题）

| 题目 | 次数 |
|---|---|
| [字符串压缩与解压 / 394. 字符串解码](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc394) | 2 |
| [交替打印奇偶](https://bingqin2.github.io/algo-notes/13-design/producer-consumer) | 2 |
| [6. Z 字形](https://bingqin2.github.io/algo-notes/01-array-two-pointers/lc6) | 2 |
| [50. 快速幂取模](https://bingqin2.github.io/algo-notes/14-string-math/lc50) | 2 |
| [20. 有效括号](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc20) | 2 |
| [IP 转整数 / IP+端口打包](https://bingqin2.github.io/algo-notes/14-string-math/ip-to-int) | 2 |
| [146. LRU（含分布式缓存）](https://bingqin2.github.io/algo-notes/13-design/lc146) | 3 |
| [限流器](https://bingqin2.github.io/algo-notes/13-design/rate-limiter) | 1 |
| [92. 区间反转](https://bingqin2.github.io/algo-notes/04-linked-list/lc92)、[141. 判环](https://bingqin2.github.io/algo-notes/04-linked-list/lc141) | 各 1 |
| [23. N 个升序数组合并](https://bingqin2.github.io/algo-notes/04-linked-list/lc23) | 1 |
| [124. 二叉树最大路径和](https://bingqin2.github.io/algo-notes/08-binary-tree/lc124) | 1 |
| [207. 课程表（输出全部拓扑序）](https://bingqin2.github.io/algo-notes/09-graph/lc207) | 1 |
| [239. 滑动窗口最大值](https://bingqin2.github.io/algo-notes/02-sliding-window/lc239)、[739. 每日温度](https://bingqin2.github.io/algo-notes/05-stack-monotonic/lc739)、[56. 合并区间](https://bingqin2.github.io/algo-notes/12-greedy-interval/lc56) | 各 1 |
| [415. 字符串相加 / 43. 大数乘法](https://bingqin2.github.io/algo-notes/14-string-math/lc415) | 2 |
| [原地归并排序](https://bingqin2.github.io/algo-notes/00-sorting/merge-sort)、[快排与堆排序](https://bingqin2.github.io/algo-notes/00-sorting/quick-sort) | 各 1 |
| [704. 二分边界](https://bingqin2.github.io/algo-notes/03-binary-search/lc704) | 1 |
