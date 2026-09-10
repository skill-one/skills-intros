# golang-samber-mo (`samber/cc-skills-golang/golang-samber-mo`)

## comments

- user: 写了八年 CRUD 的后端, category: 妙用, comment: 把模型里的 sql.NullString 全换成 mo.Option[string]：Scan 直接收，不用来回倒 .String/.Valid，还顺手区分了 NULL 和空串。
- user: 从 Rust 转来的人, category: 坑, comment: 照 Rust 习惯写 Ok(raw).Map(parse) 想把 []byte 变自定义类型，编译直接报错——直接方法不能改类型参数，得用 result 子包的 Map 或 Pipe。
- user: 第一次用的新手, category: 坑, comment: 在 mo.Do 外面用了 MustGet，一个 None 直接 panic 打挂接口。教训：MustGet 只在 Do 块里写，其他地方一律 OrElse 给默认值。
- user: 写 API 网关的后端, category: 注意, comment: 别把字段无脑换 Option[string]：它区分「没填」和「空串」。备注这种空串合法的字段用 Option，调用方要多解一层，语义反而拧了。
- user: 带 Go 团队的 tech lead, category: 启发, comment: 我们组定了规矩：一端是错误用 Result，两条路都合法（如缓存 vs 新数据）才用 Either。之前混用，review 时总有人问 Left 是不是报错。
- user: 给团队写公共库的, category: 妙用, comment: mo.Fold 一个写法通吃 Option/Result/Either，我给三种类型统一写了个取值打日志的助手函数，不用各维护一份。
