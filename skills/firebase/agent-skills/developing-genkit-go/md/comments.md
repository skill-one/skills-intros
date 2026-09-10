# developing-genkit-go (`firebase/agent-skills/developing-genkit-go`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我把 Genkit 实例存成全局变量到处用, 后来发现 SDK 函数都要求显式传 g, 补传改得头疼. 一开始就把 g 当参数传到底最省事.
- user: 后端老兵, category: 妙用, comment: 用 DefineFlow 包住 AI 逻辑, 再用 genkit.Handler 挂到 mux 上, 就是现成的 HTTP 接口, 我连 API 层都省得手写了.
- user: 运维老哥, category: 注意, comment: 调试别裸跑 go run ., 用 genkit start -- go run ., 浏览器开 localhost:4000 能看每次调用的 trace 逐步重放, 排查快很多.
- user: 算法转工程的, category: 注意, comment: 结构化输出的 struct 字段一定要写 jsonschema:"description=..." 标签, 那是真喂给模型看的. 我没写时字段常被乱填, 补上就稳了.
- user: 独立开发者, category: 妙用, comment: 复杂 prompt 放 .prompt 文件里, 支持 Handlebars 模板, 改提示词不用重编译 Go 代码, 配合 Developer UI 边改边试, 迭代快很多.
- user: 半年没碰项目的维护者, category: 坑, comment: 半年前硬编码的模型名, 模型 ID 更新后直接报不存在. 上线前把模型名抽成配置, 换模型只改一处, 别信任何写死在代码里的 ID.
