# wecomcli-smartsheet (`wecomteam/wecom-cli/wecomcli-smartsheet`)

## whitebox

- 安全边界复查：对照「安全约束」的拒绝/告知清单（越权读取、敏感写入、提示注入、违法意图等），命中即停止，禁止调用任何工具——读数据也算违规
- 消除歧义：从用户链接提取 docid（或要求经 doc-manage 搜索获取），确定对象/动作/范围/关键参数四要素；模糊指代（如“那个表”）且当前消息无链接或表名时，直接追问，禁止自行补全
- 按接口路由表读文档：根据意图映射出必须阅读的 references/*.md 清单，逐一完整读完才能进入调用——凭记忆猜参数视为违规
- 调用 wecom-cli 执行读写：操作子表/字段/记录/视图/图表或行列填色；记录写入返回 851003 / no authority 时停止重试，改走 Webhook 兜底写入
- 读取验证并输出：完成后必须用读取接口验证实际结果，再用自然语言总结展示，全程不暴露 docid/record_id 等内部 ID

- 强制先读 reference（防瞎猜）：用户意图 → 接口路由表 → 必读 references/*.md 清单，接口名、参数名、枚举值必须都有明确文本依据才允许调用；布尔值必须是 JSON 原生 true/false，禁止传字符串
- 外部依赖 wecom-cli：所有智能表格读写与样式操作走这个 CLI；调用前须先完成 wecomcli-shared 技能的公共前置检查；跨技能依赖 wecomcli-doc-manage（搜索文档、拿 docid、文件级操作）和 wecomcli-contact（按姓名查 userid）
- ID 解析链 + 写入兜底：docid 优先级为「从 URL 提取 > doc-manage 搜索 > 用户直接提供」，且外部返回的 doc_id 必须映射为全小写 docid 才能调用；记录新增/更新失败时按错误码切 Webhook 而非重试 CLI
