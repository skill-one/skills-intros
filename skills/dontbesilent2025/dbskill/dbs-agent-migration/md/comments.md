# dbs-agent-migration (`dontbesilent2025/dbskill/dbs-agent-migration`)

## comments

- user: 全栈独立开发，三端都在用, category: 坑, comment: 之前复制 CLAUDE.md 改名 AGENTS.md 就算迁完，半年后两边规则各改各的。它审计出我是半迁移，把平台无关规则拆进 AGENTS.md，别再手工复制。
- user: 第一次用的新手, category: 注意, comment: 不是一条命令跑完的黑盒。每个阶段会停下来汇报看到什么、要改哪个文件、删什么留什么，需要你在场确认。想无人值守全自动的不适合。
- user: Grok TUI 重度用户, category: 注意, comment: 自己写过 Grok bridge，漏了 frontmatter 的 user_invocable: true，输 / 死活搜不到技能。它生成时强制带这行并当场验证，手写 bridge 的先查这里。
- user: 自由职业者，prompt 散落党, category: 妙用, comment: 项目里 40 多个 md 我全当 skill。它先给候选清单：带触发步骤的收编，文章和导出稿排除，逐条确认后才建 skills/。散文档多先跑审计再动手。
- user: 运维老哥, category: 启发, comment: 以前逻辑写在各端 bridge 里，改一次要同步 4 处，漏一处就不一致。迁完 bridge 全是薄指针，只改真源再重新生成，单点修改替代了多处同步。
- user: 用豆包 Mac App 的产品经理, category: 坑, comment: ~/.agents/skills 已有同名真实目录时它不覆盖，会停下报告路径等我确认迁不迁。另外优先写软链不复制内容，别手贱删真源，软链会悬空。
