# check-impl-against-spec (`warpdotdev/common-skills/check-impl-against-spec`)

## whitebox

- 触发: 仅当 PR review 期间存在 spec_context.md 时才启动, 否则什么都不做。
- 提取承诺: 读 spec_context.md, 抽出必需行为 (产品 spec)、必需改动的文件/子系统 (技术 spec)、约束、要求的验证/迁移步骤。
- 对照实现: 把承诺逐项与 pr_diff.txt (带注释的 diff) 及工作区实际代码比对, pr_description.md 可补充范围/动机。
- 重要性判定: 保留 spec 意图的小幅实现调整放行; 只标记实质偏差 (缺行为、违背 spec 决策、超范围改动、缺验证/迁移)。
- 输出结果: 不建独立报告, 把结论折进 review.json — 宽泛漂移进 summary, 能对应 diff 变更行的偏差加 inline 评论, 实质偏差至少记 important。

- 双源比对: 以 spec_context.md 为基准, 对照 pr_diff.txt + 已检出的 PR 分支代码; 纯本地文件分析, 不依赖任何外部工具、库或模型 API。
- 意图保留过滤: 不要求 spec 逐字一一对应, 结果安全达成即算符合; 命名/结构/底层选型差异不 flag, 只有 material mismatch 才上报。
- 输出折叠: 发现全部并入已有 review.json (summary 放宽泛漂移, inline 仅限可挂到 diff 行的偏差), 不落盘独立文件, 不直接发 GitHub。
