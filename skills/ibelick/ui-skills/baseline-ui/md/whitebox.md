# baseline-ui (`ibelick/ui-skills/baseline-ui`)

## whitebox

- 接收 `/baseline-ui` 触发: 带文件参数 = 审查模式; 不带参数 = 将约束集应用于本会话后续所有 UI 工作
- 加载 skill.md 内置的九类约束清单 (Stack / Components / Interaction / Animation / Typography / Layout / Performance / Design)
- 审查模式: 逐条比对待审文件, 定位违规处并引用确切代码行/片段
- 按固定格式输出每条问题: 违规原文引用 → 为何要紧 (一句话) → 代码级具体修复建议
- 结束 — 审查只输出报告和修复建议, 不自动重写文件

- 清单驱动审查: 对照固定约束表逐条核验, 每条约束带 MUST (强制) / SHOULD (建议) / NEVER (禁止) 级别, 结论可推导可复现, 非自由发挥的审美意见
- 固定输出协议: 违规必须引用原文 + 一句话影响 + 代码级修复建议, 杜绝空泛描述
- 约束锚定具体工具链: Tailwind CSS 默认值, cn 工具 (clsx + tailwind-merge), motion/react 动画, tw-animate-css 进场微动画, 无障碍原语库 (Base UI / React Aria / Radix)
