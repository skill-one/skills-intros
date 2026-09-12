# momentic-explore-prompt (`momentic-ai/skills/momentic-explore-prompt`)

## whitebox

- 第一步:遍历仓库收集事实(不凭记忆写)——列出被测应用、测试运行时应访问的 URL、登录模块的 name+id、各应用的测试保存目录、被 gitignore 的一次性测试目录。
- 第二步:交叉验证关键事实——用 momentic.config.yaml 的 environments[].baseUrl 和运行 explore 的 CI 工作流确认真实运行 URL(而非本地开发服务器 URL),再补充仓库特有的 quirk(如跨运行持久的数据)。
- 第三步:把真实值填进占位符模板,生成 explore-prompt.md——简洁祈使句 markdown,固定五节:应用与目标 URL、diff→应用映射、测试存放规则(HARD RULE 标注)、一次性测试规则、quirk 清单。
- 第四步:交给 Momentic CLI 消费——用户执行 momentic ai explore diff/latest --prompt-file ./explore-prompt.md,文件内容被追加到 explore agent 的 system prompt,agent 据此自动识别变更路径并生成测试。

- 事实采集靠读仓库,不靠模型记忆:URL 以『测试运行时实际访问的地址』为准(查 momentic.config.yaml 与 CI workflow,排除本地 dev-server 地址);一次性目录以 .gitignore 实际忽略的路径为准;登录模块必须同时记录 name 和 id 以便精确引用。
- 模板实例化 + 路径硬约束:基于只含占位符的骨架填充仓库真实值;路径约束统一写成 HARD RULE: 强调句式——这是 explore agent 最常见、代价最高的失败点(存错目录、丢掉强制前缀、junk-* 命名不算 junk 目录)。
- 指令叠加消费机制:--prompt 和 --prompt-file 均可重复传入,按传入顺序全部追加(叠加而非覆盖),且只要传了任一个就会替换项目的云端自定义 prompt;文件刻意不写通用 Momentic 行为——那部分由 momentic-test skill 承担。外部依赖:Momententic CLI(momentic ai explore diff / momentic ai explore latest),skill 本身不调用其他库或模型 API。
