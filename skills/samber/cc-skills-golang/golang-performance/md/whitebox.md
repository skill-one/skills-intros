# golang-performance (`samber/cc-skills-golang/golang-performance`)

## whitebox

- 判定触发模式: 架构评审 (并行派 3 个子代理分查内存布局、I/O 并发、算法与缓存)、单函数热点评审 (顺序执行), 或瓶颈已被 profiling 定位的优化模式。
- 先排除外部瓶颈: 用 fgprof / goroutine profile 查 off-CPU 与 I/O 等待, 若瓶颈在 DB 或外部 API, 转去优化那边而不是改 Go 代码。
- 定义指标并测基线: go test -bench -benchmem -count=6, 报告存入 /tmp/report-1.txt。
- 按 pprof 信号查决策树选中对应的优化模式, 一次只改一处并附注释说明为何更快。
- benchstat 对比前后报告确认统计显著, 结果贴进 commit (perf(scope): ...), 再回到测基线处理下一个瓶颈。

- 决策树路由: pprof 信号 (alloc_objects 高 / 函数独占 CPU / GC 占比高 / goroutine 阻塞在 I/O) 直接映射到专项参考文档 (memory / cpu / runtime / io-networking / caching), 拒绝无 profiling 凭直觉优化。
- benchstat 统计对比 (外部工具, go install golang.org/x/perf/cmd/benchstat@latest): -count=6 多次采样判定提升是否显著, /tmp/report-*.txt 全部保留作审计链。
- 竞争方案隔离验证: 多个候选优化各自放进独立 worktree (隔离工作目录) 由子代理并行实现, 再用 benchstat 择优; 运行依赖 go、pprof、fgprof、staticcheck / fieldalignment / golangci-lint 等外部工具。
