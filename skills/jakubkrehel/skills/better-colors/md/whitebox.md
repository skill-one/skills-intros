# better-colors (`jakubkrehel/skills/better-colors`)

## whitebox

- 先读项目现有颜色 token 与记法 (hex/oklch), 一切输出沿用既有体系, 不引入第二套表示
- 用颜色库按角色生成/修复 ramp: 步长按感知亮度均匀、色相全程恒定、鲜活度中段峰值、两端不触及纯黑白
- 原色 (primitive) 按色相命名, 语义 token 按角色指向原色, 组件只引用语义层
- 对每对实际渲染的前景/背景 (不是页面背景) 计算对比度, 只报测得的精确值
- 按严重度 (HIGH/MEDIUM/LOW) 出表格报告, 未执行的验证项标 Not verified; 有 HIGH 则 Block, 否则 Approve

- 记法与生成: 优先复用项目记法, 仅新体系默认 oklch(); ramp 必须由颜色库计算而非目测 (skill 明确拒绝靠眼睛挑值)
- 对比度精确校验: 禁止报告未测量的对比度; 有浏览器时测真实渲染背景 (含透明度与下层图像) 的明暗两套主题, 无浏览器时从声明的 token 对直接计算
- token 双层结构 + 角色约束: primitive 与 semantic 分离是主题切换的接缝; 校验规则包括角色 token 不得按值挪用、色相差 ±15° 内视为同色、一个视图只允许一个填充主操作、P3 颜色必须先声明 sRGB 回退
