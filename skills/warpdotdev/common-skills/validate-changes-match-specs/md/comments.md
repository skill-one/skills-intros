# validate-changes-match-specs (`warpdotdev/common-skills/validate-changes-match-specs`)

## comments

- user: 安全岗出身的老后端, category: 妙用, comment: 发现代码里有个 spec 没覆盖的越权风险, 它没忽略, 而是标成 security amendment 建议补进 SECURITY.md。现在碰 auth 的 PR 我都先跑它。
- user: 第一次用的新手, category: 坑, comment: 以为它能照 diff 自动生成 spec, 结果仓库里没有 specs/ 目录, 它直接停下说没东西可验证。它只做比对, 得先自己写好 spec 再跑。
- user: 一人接单的全栈, category: 妙用, comment: 7 个 mismatch 选了批量模式: 逐条决策, 最后一次性改完统一验证。报告自带 spec 路径和代码路径, 我直接贴进 PR 描述当评审记录。
- user: 带教新人的 Tech Lead, category: 注意, comment: 它不会静默改代码, 每个差异都会问你: 改实现还是改 spec。想保持现状就选 acknowledge 不改, 你的理由会保留进最终总结, 正好当决策记录。
- user: 常被 reviewer 追问的在职开发, category: 妙用, comment: 我在 review 评论里回了"已修复"却漏改代码, 它对照我的回复把这处不一致抓了出来, 免得被 reviewer 再打回。提醒: 它不替你发评论, 回复草稿要你批准后才发。
- user: 运维老哥, category: 注意, comment: 改完它会优先跑仓库既有的测试/校验命令, 跑不了会明说哪些没验证, 不会假装全绿。看总结别只数 mismatch, 未验证清单也得过一眼。
