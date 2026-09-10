# migrate-to-shoehorn (`mattpocock/skills/migrate-to-shoehorn`)

## comments

- user: 后端老兵, category: 妙用, comment: grep 那条命令我当测试体检用,还没迁移就先扫全库,十分钟摸清测试里的 `as` 债,顺手揪出好几个伪造 20 个字段的 Request。
- user: 第一次用的新手, category: 坑, comment: 故意填错类型(id 传数字)喂给 fromPartial,类型检查报错,还以为库坏了。错数据要走 fromAny,fromPartial 只收「少字段」不收「错字段」。
- user: 前端开发, category: 注意, comment: 测试里不是每个 `as` 都要改:`el as HTMLElement` 这种 DOM 断言不缺字段,硬换 fromPartial 编译不过。只改「传不完整数据」的断言。
- user: 测试工程师, category: 妙用, comment: 写参数校验的报错用例最爽:以前 `as unknown as` 双重断言看着心虚,现在 fromAny({ body: { id: 123 } }) 一行搞定,还保留字段自动补全。
- user: 技术组长, category: 启发, comment: 迁到一半才看清:测试要伪造 20 个字段,根子在函数收整个 Request。shoehorn 是止血,回头把入参拆小才是治本。
- user: 前端老兵, category: 注意, comment: 图省事把 fromPartial 写进了业务代码,被同事 review 直接打回:生产代码里少传字段是真 bug,这个库只能进测试文件。
