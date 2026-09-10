# golang-performance (`samber/cc-skills-golang/golang-performance`)

## comments

- user: 第一次用的新手, category: 注意, comment: 别直接喊"帮我变快",它要先看基准数据。先跑 go test -bench -benchmem 把结果贴给它。它坚持一次只改一处,别催它一口气改完。
- user: 后端老兵, category: 妙用, comment: 上线前让它做架构级体检,内存/IO/算法三路并行扫。真扫出我用默认 http.Client,连接池才 2,高并发下反复建连。
- user: 运维老哥, category: 坑, comment: 没装 benchstat 就开跑,基准测完到对比那步才报错,白跑一轮。先装:go install golang.org/x/perf/cmd/benchstat@latest
- user: SRE 值班, category: 注意, comment: 想学写 benchmark、用 pprof 排查,它会把你引到另两个技能。它只管"瓶颈定位后选哪种优化"。带着结论来,见效最快。
- user: 技术负责人, category: 启发, comment: 它要求每笔 perf 提交都附 benchstat 前后对比,commit 里直接写明快了多少。现在组里没人敢凭感觉合"优化"代码了。
- user: 小厂全栈, category: 妙用, comment: 两个优化方案打架时,让它分 worktree 各做一版再对比。它特意提醒并行跑基准会抢 CPU 污染数据,最后必须串行测,少走弯路。
