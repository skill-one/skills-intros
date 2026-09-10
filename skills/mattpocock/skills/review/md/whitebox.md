# review (`mattpocock/skills/review`)

## whitebox

- 锚定起点: 生成 `git diff <锚点>...HEAD`(三点号, 对 merge-base 比较)与 commit 清单, 并校验锚点可解析、diff 非空, 失败即在此终止。
- 找规格源: 按 commit 内 issue 引用 → 用户传入路径 → docs/、specs/、.scratch/ 下 PRD 的顺序定位原始需求, 都没有就问用户。
- 找规范源: 扫出 CODING_STANDARDS.md、CONTRIBUTING.md 等仓库文档, 叠加内置的 12 条 Fowler 坏味道基线。
- 并行审查: 单条消息同时派发两个 general-purpose 子代理, 各自按 brief 独立产出 Standards 与 Spec 报告(限 400 词)。
- 汇总: 原样并排呈现两份报告(## Standards / ## Spec), 末尾各轴一行小结, 不跨轴合并或排名。

- 双轴上下文隔离: Standards 与 Spec 各跑在独立子代理里(经 Agent 工具的 general-purpose 类型), 防止互相污染; 本体只聚合、不改写不重排——因为一轴可能通过而另一轴失败, 合并会让一方掩盖另一方。
- diff 口径固定: 一次性捕获三点号 diff(对 merge-base)与 `git log <锚点>..HEAD --oneline`, 并前置校验 `git rev-parse`; 坏 ref 或空 diff 在派发前失败, 而不是死在子代理里。
- 校验规则分层: 文档标准违反=硬违规(须引用文件+具体条目); Fowler 基线=只是判断参考; 仓库文档可压制基线, 工具已强制的一律跳过。外部依赖: git 与 issue tracker(按 docs/agents/issue-tracker.md 约定取 issue), 不依赖特定模型 API 或第三方库。
