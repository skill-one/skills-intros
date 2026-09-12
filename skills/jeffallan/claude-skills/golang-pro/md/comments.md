# golang-pro (`jeffallan/claude-skills/golang-pro`)

## comments

- user: 十年Java转Go的后端, category: 妙用, comment: 老代码里裸开的goroutine退不出来，让它重构后全挂上context超时取消，上线俩月没再报协程泄漏。
- user: 第一次用的新手, category: 坑, comment: 没装 golangci-lint 就让它走完整流程，卡在 lint 那步报 command not found。先 go install 装好再开工。
- user: 赶产品的独立开发者, category: 注意, comment: 默认交付接口+实现+测试三件套，还追80%覆盖率。赶demo直接说「先跳过测试」，不然一堆_test文件要清理。
- user: 运维老哥, category: 妙用, comment: 把CPU飙高时的pprof火焰图丢给它，能指出具体热点函数，还顺手写benchmark对比改前改后，省我自己翻文档。
- user: 维护祖传系统的老Go, category: 注意, comment: 老项目还在Go 1.16，直接要泛型代码编译不过。开工前先报自己的Go版本，它会换成兼容写法。
- user: 测试转开发的妹纸, category: 启发, comment: 看到它测试必带 -race 跑，才反应过来我们CI不开race检测的「全绿」照样藏着并发bug，已经照搬进CI了。
