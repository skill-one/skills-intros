# caveman-review (`juliusbrussee/caveman/caveman-review`)

## whitebox

- 接收触发词 + 待审 diff / PR 代码
- 扫 diff, 定位问题行, 抓准确行号和符号名
- 每条发现压缩成一行: `L<行号>: <问题>. <修法>.`, 混合严重度时加 🔴/🟡/🔵/❓ 前缀
- 直接输出成可粘贴进 PR 的评论, 不写修复代码、不 approve、不跑 linter

- 行号锚定: 每条必须带精确行号 (多文件用 `file:L行号:`) + 反引号包住的具体函数/变量名, 禁止模糊表述; 修法必须具体 (如 `withBackoff(3)`), 不允许 "consider refactoring"
- Auto-Clarity 降档开关: 遇到三类情况——安全漏洞 (CVE 级)、架构分歧、面向新人的 onboarding——临时切回完整段落讲清 why, 其余恢复极简; 说 "stop caveman-review" 即整体退回啰嗦模式
- 零外部依赖: 纯 prompt 层行为, 不调用任何外部工具/库/模型 API——明确不跑 linter、不执行代码; 噪音过滤靠内置丢弃规则 (删寒暄、删铺垫、删复述代码、删含糊措辞, 拿不准的标 ❓ q)
