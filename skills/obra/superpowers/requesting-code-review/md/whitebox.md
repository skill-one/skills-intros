# requesting-code-review (`obra/superpowers/requesting-code-review`)

## whitebox

- 用 git 取两个提交号 (SHA): 基线 BASE_SHA 和当前 HEAD_SHA, 圈定待审查的改动范围
- 按 code-reviewer.md 模板填四个占位符: 改动描述、需求/计划来源、两个 SHA
- 派发一个 general-purpose 子代理执行审查
- 收到反馈后按严重度处理: Critical 立即修, Important 修完才继续, Minor 记下待办
- 若审查者结论有误, 拿代码/测试等技术依据反驳

- 上下文隔离: 审查全程发生在子代理自己的上下文里, 只有发现的问题返回主会话, 主代理的 context window 不被 diff 消耗
- 精确上下文注入: 只给审查者精心构造的四项信息 (描述/需求/SHA对), 永不传主会话历史, 让评估聚焦工作成果而非思考过程
- 外部依赖: git 命令 (rev-parse/log 获取 SHA、定位 diff 范围), general-purpose 子代理, code-reviewer.md 评审模板
