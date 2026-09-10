# safe-refactor (`juliusbrussee/caveman/safe-refactor`)

## comments

- user: 后端老兵, category: 妙用, comment: 让它一次只挪一个模块地重构老订单逻辑, 每步测试全绿, diff 小到评审秒过。
- user: 第一次重构的新手, category: 坑, comment: 我把新功能和重构混在一次提交, 出问题分不清是哪步的锅。后来拆开: 功能归功能, 重构只动结构不动行为。
- user: 测试工程师, category: 注意, comment: 动手前先确认「拿什么证明行为没变」(同一套测试/同样输出)。没先定验证标准, 改完就无法自证清白。
- user: 祖传代码维护者, category: 妙用, comment: 中间每步都能编译能跑是关键: 重构到一半被叫去救火, 我直接停在建好的半截上合并, 一点不慌。
- user: 技术负责人, category: 启发, comment: 它不让我顺手加新依赖, 逼我问自己: 是正确性需要还是图省事? 重构提交从此不夹带私货。
- user: 修过线上事故的人, category: 注意, comment: 我有次把报错文案改成「更合理」的, 监控正则全失配。接口、报错、顺序别悄悄动, 要动先声明。
