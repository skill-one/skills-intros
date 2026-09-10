# firecrawl-website-design-clone (`firecrawl/firecrawl-workflows/firecrawl-website-design-clone`)

## blackbox

**function**: 把任意一个网址变成一份 AI 可直接照着做的设计说明书（DESIGN.md），用它复刻该网站风格或搭建风格一致的全新页面。

- input: 一个网址，如「https://linear.app，帮我提取它的设计风格」, output: 一份 DESIGN.md 设计说明书：主色/背景/文字等全部色值、字体与字号体系、间距与圆角规则、按钮和卡片等组件样式，顶部附带该站整页截图作为视觉基准
- input: 一个网址 + 一句「顺便照它帮我做个落地页」, output: 先得到设计说明书，再得到按该风格实现好的可运行网页代码
- input: 一个想模仿的竞品官网链接，如「照这个感觉给我做个新站」, output: 设计说明书中额外列出该站实际用到的图片素材清单（主图、产品图、插画）和文案语气规律，AI 据此搭出一个「神似」的新页面
