# design-md (`google-labs-code/stitch-skills/design-md`)

## blackbox

**function**: 把你在 Stitch(Google 的 AI 界面设计工具)里的设计稿, 整理成一份人类和 AI 都能读懂的《设计语言说明书》(DESIGN.md 文件)

- input: 一个 Stitch 项目名称或链接, 如「Furniture Collection」, output: 一份 DESIGN.md 文件: 记录该项目的设计风格、颜色清单 (描述性名称 + 色号 + 用途)、字体规则、圆角/阴影质感和排版原则
- input: 项目 ID + 某个页面名, 如「看一下 Home 页」, output: 以该页面为样本提炼出的设计说明书, 用大白话描述细节, 如「深海蓝绿色 #294056, 用于主按钮」「药丸形状的按钮」「极轻的柔和阴影」
- input: 只说一句「帮我梳理我的 Stitch 项目设计语言, 以后生成新页面风格要一致」, output: 自动找到你的项目和页面, 生成完整 DESIGN.md; 之后把它喂给 AI 生成新界面, 风格就能和现有设计保持一致
