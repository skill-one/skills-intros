# golang-testing (`samber/cc-skills-golang/golang-testing`)

## comments

- user: 刚接手 Go 项目的新手, category: 坑, comment: 我在父测试里建了 assert.New(t) 给子测试共用，失败只报父测试挂、子测试全 PASS，定位不到哪条 case。改成每个 t.Run 里用自己的 t 新建一个。
- user: 写了八年 Go 的后端老兵, category: 妙用, comment: 超时类测试原来靠真 sleep，又慢又抖。换 synctest 后时间快进、结果可复现，5 秒的用例瞬间跑完。前提是 Go 1.25+，老版本没这个。
- user: 搭 CI 的运维, category: 注意, comment: gotests 得先 go install 装好，不然生成脚手架那步直接报找不到命令。另外 go test ./... 默认跳过带 integration 标签的用例，全绿不代表连库测试也跑了。
- user: 从 Java 转过来的开发, category: 启发, comment: 以前我盯着覆盖率数字凑测试。这里把 coverage 当找盲区的工具而非 KPI，我才懂测内部实现一重构就崩，测公开 API 行为才扛得住改动。
- user: 维护开源库的作者, category: 坑, comment: 我按函数名拆测试文件，checkout_test.go 散对三个源文件，IDE 跳转和覆盖对照全乱。改回 foo.go 对 foo_test.go 一一对应，导航和 review 都顺了。
- user: 做并发中间件的工程师, category: 妙用, comment: 在 TestMain 里加三行 goleak.VerifyTestMain，CI 当场揪出一个取消后没退出的 worker 协程，不用等线上偶发内存涨再回头查。有协程的包都值得加。
