# better-typography (`jakubkrehel/skills/better-typography`)

## whitebox

- 读取渲染后的页面而非扫代码——换行错乱、孤字、截断只在真实内容长度下才暴露
- 按 skill.md 清单逐项核对: 字体加载与合成、层级递减、行高/字距/行宽、换行策略、等宽数字、截断兜底、标点与字号底线
- 越界问题分诊转交: 文案措辞、语义标题、空间 RTL 布局、对比度测量分别归属四个相邻技能, 本技能不越权
- 用项目现有样式系统写修复, 采用清单中的精确值, 而非看起来相近的等价写法
- 校验后按严重度输出报告表, 有 HIGH 判 Block、否则 Approve; 无发现则声明 'No actionable typography findings'

- 双路校验 (依赖外部工具: 浏览器): 有浏览器时调整视口宽度, 在真实内容长度下捕捉换行/孤字/截断; 无浏览器时退化为核对声明值——每级标题的计算 size/weight 是否递减、line-height 与行宽、截断规则对照真实字符串长度; 跑不了的检查一律标 'Not verified'
- 转换原则: 修复写入项目样式系统 (如 Tailwind, 映射表在 css-cheat-sheet.md), 且优先用 CSS 属性而非原始 tag (font-weight: 650 而非 "wght" 650; font-variant-numeric: tabular-nums 而非 "tnum" 1), 仅定制轴等无属性可用的场景才写 raw tag; 严格采用清单精确值, 拒绝习惯性等价值
- 分诊与报告协议: 职责边界硬编码——措辞→better-writing、语义标题结构→better-accessibility、RTL 空间布局→better-layout、对比度测量→better-colors; 发现按 HIGH/MEDIUM/LOW 定级, 一个根因一行列出全部出现位置 (path:line + Before/After/Why), 结论只有 Block/Approve 二值, 不 Approve 未检查的范围
