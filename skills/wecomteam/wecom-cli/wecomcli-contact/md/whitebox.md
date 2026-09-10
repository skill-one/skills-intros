# wecomcli-contact (`wecomteam/wecom-cli/wecomcli-contact`)

## whitebox

- 前置检查：任何 wecom-cli 命令执行前，先完成 wecomcli-shared 技能的公共前置检查。
- 提取用户请求中的搜索关键词（姓名/拼音/英文名/别名）；若缺失且无法从上下文推断，则追问，不猜默认值。
- 把关键词打包成 JSON 参数（默认不传 search_mode），执行 `wecom-cli contact users search --json '<JSON 参数>'`。
- 解析返回 JSON：users 数组（userid/name/alias/position/departments 等）及 hint 限制提示。
- 按接口返回的原始顺序展示结果，每个关键词最多展示前 5 位；超过 5 位时告知可要求『查看更多』，hint 非空时说明仅返回了部分结果。

- 外部依赖：CLI 二进制 `wecom-cli`（requires.bins 声明），子命令 `contact users search`，参数以 JSON 字符串经 --json 传入。
- 模糊匹配与模式切换：keywords 数组最多 10 个、彼此 OR 关系，可命中姓名/拼音/英文名/别名；默认返回最相关候选，仅当用户明确要完整名单时才显式传 search_mode="list"（不受 5 位展示上限约束）。
- 输出约束：严格保持接口返回 users 数组原始顺序，不得重排；同一关键词候选超 5 位只展示前 5 位；hint 字段非空时必须向用户披露结果受限。
