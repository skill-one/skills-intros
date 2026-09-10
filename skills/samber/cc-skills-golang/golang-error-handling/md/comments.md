# golang-error-handling (`samber/cc-skills-golang/golang-error-handling`)

## comments

- user: 后端老兵, category: 妙用, comment: 拿 audit 模式并行扫了祖传项目，揪出十几处既打日志又返回的重复记录——正是我们日志量翻倍的元凶。
- user: 第一次用的新手, category: 坑, comment: 我用 %v 包错误，下游 errors.Is 判断预定义错误永远匹配不上，查了一下午，换 %w 就好了。
- user: 老项目维护者, category: 注意, comment: 先看 go.mod 再动手：errors.AsType 要 Go 1.26+，slog 要 1.21+，老项目老实用 errors.As。
- user: 运维老哥, category: 注意, comment: 订单号别拼进日志文本，放进结构化字段。消息固定后，同类错误在聚合平台归成一组，告警不炸了。
- user: 接口开发, category: 坑, comment: 我曾把 err.Error() 原样返给前端，用户看到数据库报错还带表名。现在细节只进日志，对外翻译成人话。
- user: 技术负责人, category: 启发, comment: 以前迷信多打日志图保险，同一错误在平台上重复三次。现在要么处理要么上抛，日志干净，责任一目了然。
