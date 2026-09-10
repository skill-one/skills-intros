# golang-lint (`samber/cc-skills-golang/golang-lint`)

## comments

- user: 接手祖传项目的后端, category: 妙用, comment: 第一次全量跑报了 7000+ 条差点弃疗。后来在 .golangci.yml 里设 issues.new-from-rev: HEAD~1 只查新改动,老代码按模块慢慢清,三天就全绿了。
- user: 从 v1 升上来的新手, category: 坑, comment: 升到 v2 后配置一直报格式错,我照报错手改 YAML 改了一下午越改越乱。其实先跑一条 golangci-lint migrate 就能自动转好,再微调即可。
- user: 被 nolint 坑过的 Tech Lead, category: 妙用, comment: 代码里全是光秃秃的 //nolint,半年后没人记得当时为什么压警告。开了 nolintlint 后强制写 //nolint:errcheck // 理由,review 时少吵一半架。
- user: 吃过连接池亏的后端, category: 坑, comment: 循环里开连接被 sqlclosecheck 报,嫌烦直接 nolint 压掉,两周后线上连接池耗尽。gosec/bodyclose/sqlclosecheck 这类千万别压,补上 close 才是正解。
- user: 管大仓库的运维老哥, category: 注意, comment: 仓库一大全量 lint 慢到像卡死。把生成的 pb.go 目录加进 linters.exclusions.paths,再调低 run.concurrency 防内存爆,速度立刻恢复正常。
- user: 赶功能的后端, category: 启发, comment: 以前见报错就改,同类错照犯。学会先看行尾括号里的 linter 名、查清它在查什么,才明白怎么系统性避免一整类问题——lint 是老师,不是门卫。
