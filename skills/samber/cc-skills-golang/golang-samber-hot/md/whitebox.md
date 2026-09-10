# golang-samber-hot (`samber/cc-skills-golang/golang-samber-hot`)

## whitebox

- 触发匹配: 代码库 import github.com/samber/hot, 或项目高频重复加载中低基数资源需要降延迟/减后端压力
- 按访问模式选淘汰算法: 决策捷径是先默认 W-TinyLFU, profiling 显示未达 SLO 才换
- 定容量: 估算单条大小 (含 key 和 ~100B 管理开销) → 问开发者内存预算 → capacity = 预算 / 单条大小
- builder 链构建缓存: WithTTL、WithLoaders、WithJitter、WithJanitor、WithPrometheusMetrics, 并 defer cache.StopJanitor()
- 对照常见错误清单 (忘 Janitor、SetMissing 未配 missing cache、忽略 loader err 等) 收尾

- 算法选型靠 9 种算法对照表 (LRU/LFU/TinyLFU/W-TinyLFU/S3FIFO/ARC/TwoQueue/SIEVE/FIFO), 各自的适用/避免场景写在 skill 内, 深入对比查本地 references/algorithm-guide.md
- 容量定标是公式推导 + 实测验证: 单条大小未知时, 写单测分配 N 条用 runtime.ReadMemStats 测量, 拒绝拍脑袋 (会 OOM 或浪费内存)
- 外部依赖: go 1.22+ 与 samber/hot 库本身; godig 查 pkg.go.dev 包事实, gopls 做代码导航/诊断, Context7 作 pkg.go.dev 未收录文档的兜底
