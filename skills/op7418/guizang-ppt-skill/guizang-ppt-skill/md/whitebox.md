# guizang-ppt-skill (`op7418/guizang-ppt-skill/guizang-ppt-skill`)

## whitebox

- 需求澄清: 按 7 问清单对齐风格 A/B (电子杂志 / 瑞士国际主义)、受众、时长、素材、主题色, 用户没大纲就用"叙事弧"模板搭骨架。
- 拷贝模板: 复制所选风格模板 (assets/template.html 或 template-swiss.html) 为 index.html, 建同级 images/ 目录, grep 清掉全部 "[必填]" 占位符。
- 类名预检 (最关键一步): 先 Read 模板的 <style> 块, 确认本次要用的每个布局类名 (如 .h-hero / .kpi-hero) 都有定义, 缺失就补进模板, 不 inline 重写。
- 填充内容: 粘贴现成布局骨架 (风格 A 10 种 / 风格 B 登记版式 S01-S22) 后只改文案与图片路径, 按明暗主题节奏规则排布, 并同步生成按 data-slide-id 存储的演讲备注 (SPEAKER_NOTES)。
- 校验交付: 运行 validate-swiss-deck.mjs / validate-presenter-mode.mjs 等 Node 脚本, 再打开浏览器逐页视觉核对, 按输出的测量 px 分档微调后重跑。

- 单文件自包含架构: CSS、WebGL shader 背景、键盘/滚轮/触屏翻页 JS、演讲者视图与观众屏同步全部预置在模板内, 生成时只填 <!-- SLIDES_HERE --> 占位符和 SPEAKER_NOTES; 换主题色 = 整体替换 :root CSS 变量块, 且只允许 5 套 (杂志风) / 4 套 (瑞士风) 预设色板, 拒绝自定义 hex。
- 脚本化校验闭环: validate-swiss-deck.mjs 先做静态结构检查 (data-layout 登记版式、主题节奏), 环境可解析 Playwright 时再做真实渲染测量 (溢出 M1 / 底部空白 / 导航安全线 / 标题间距 M2), 超出按 1-40px → 160px+ 分档阶梯修正后重跑; validate-presenter-mode.mjs 校验页面 ID 唯一且稳定、备注与页面不错位、总时长 ≤ 目标 90%。
- 外部依赖: git 用于启动前上游更新检查 (检测到更新先询问、用户确认才 pull --ff-only); 校验脚本基于 Node.js, 渲染测量依赖 Playwright; Lucide 图标、Motion One 动效、Web 字体走 CDN 且本地 + CDN 双保险; Codex 环境下可选调 GPT-M 2.0 生成/再设计配图, 按槽位比例落到 images/ 并遵守 {页号}-{语义} 命名。
