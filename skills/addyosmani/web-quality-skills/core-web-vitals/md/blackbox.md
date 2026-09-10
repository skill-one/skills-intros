# core-web-vitals (`addyosmani/web-quality-skills/core-web-vitals`)

## blackbox

**function**: 帮你诊断网页「加载慢、点了没反应、内容乱跳」的问题, 并给出能落地的优化改法, 让 Google 核心体验指标 (LCP 加载速度 / INP 响应速度 / CLS 视觉稳定性) 达标。

- input: 一个网站的网址 (例如 https://你的商店.com), output: 一份体验指标报告: 三项核心指标各是多少、哪项不达标、最慢/最跳的是页面上的哪个具体元素
- input: 「首页打开时, 图片先占一半屏、过两秒又跳下来」这样的现象描述 + 网址, output: 定位到引发跳动的那张图片/横幅, 以及修复后的代码 (如补上宽高占位、预加载主图)
- input: 一段页面代码 (HTML / React / Vue 组件均可), output: 逐处标出会导致加载慢、点击卡顿、内容跳版的写法, 并直接给出改好的代码
