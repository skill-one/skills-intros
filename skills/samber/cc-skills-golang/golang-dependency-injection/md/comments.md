# golang-dependency-injection (`samber/cc-skills-golang/golang-dependency-injection`)

## comments

- user: 第一次用的新手, category: 坑, comment: 项目才8个服务就上了fx, 花两天学框架不如手写构造函数. 先看决策表: <10个服务手动注入就够, main.go二十行能看完整依赖图.
- user: 后端老兵, category: 妙用, comment: 把接口从实现方挪到消费方后, mock只需实现service真正用到的方法. 以前对着15个方法的DB层硬写假实现, 现在只写2个.
- user: 老项目维护者, category: 注意, comment: 重构老仓库先用它的多agent扫描, 一次找出全局变量/init()注入/服务定位器问题并出迁移方案. 我手查了一周才发现有这功能.
- user: 测试工程师, category: 妙用, comment: 集成测试用容器克隆: 整个injector只把支付网关换成mock, 其余全真. 不用连staging跑全链路, 本地几分钟跑完.
- user: 技术负责人, category: 启发, comment: "依赖图保持浅"成了我review的硬标准. 以前放行过A->B->C->D的链, 现在要求service直接依赖repo和config, 代码好测多了.
- user: 务实派工程师, category: 注意, comment: 指南明说不含各库完整API, 示例签名可能过时. 我照抄wire示例, 版本更新后编译报错, 去官方文档才对上.
