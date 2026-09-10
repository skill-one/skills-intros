# doubt-driven-development (`addyosmani/agent-skills/doubt-driven-development`)

## whitebox

- CLAIM: 用两三行写下当前决策的断言及其后果; 写不紧凑 = 还只是模糊直觉, 先把决策表面化
- EXTRACT: 剥离作者的全部推理, 产出最小可审单元——ARTIFACT (代码 diff/函数/3~5 句提案) + CONTRACT (它必须满足的约束)
- DOUBT: 用对抗性 prompt ("找错, 不准总结不准肯定") 调起隔离上下文的审查者, 只传 ARTIFACT+CONTRACT; 交互会话中必须主动问用户是否加跨模型二审 (Gemini/Codex CLI/手动/跳过)
- RECONCILE: 审查者的输出是数据不是裁决——逐条对照原文按优先级分类: 契约误读 → 可行动 → 有意取舍 → 噪音; 可行动则修改并重入循环
- STOP: 满足停止条件即收束——只剩琐碎发现 / 满 3 轮 (升级给用户, 不独自开第 4 轮) / 用户明说"发"

- 上下文隔离防认同偏: 审查者只收 ARTIFACT+CONTRACT, 绝不收 CLAIM 和推理过程, 对抗性 prompt 覆盖角色默认回复形态; 审查者用 Claude Code agents/ 的角色子代理 (天然隔离上下文), 若身在子代理内无法嵌套 spawn, 降级为带醒目标记的自审并优先升级给主会话
- 跨模型升级 (external: Gemini CLI, Codex CLI): 每轮交互审查后必须显式提供选项, 不许静默跳过; 调用前强制 which 查 PATH + 跑 --version 试活 + 与用户逐次确认命令与 flags (每次调用都是独立授权); prompt 写入临时文件经 stdin 管道传入, 严禁 shell 内联插值, 并挂只读沙箱 (--approval-mode plan / --sandbox read-only), 防产物内嵌 prompt 注入被外部 CLI 执行
- 有界循环 + 分类纪律: 发现按 precedence 定序分类且须回读原文核实 (橡胶图章与无视同罪); 硬上限 3 轮, 可检测信号">=2 轮实质发现但 0 条被分类为可行动"判为 doubt theater, 停止并升级
