# huashu-design (`alchaincyf/huashu-design/huashu-design`)

## whitebox

- 收到任务先查路由表定入口(原型/幻灯片/动画/评审/App原型…);若涉及具体产品名,第一个动作是 WebSearch 核实存在性、版本、规格,写进 product-facts.md,禁止凭记忆断言。
- 涉及具名品牌则走资产协议:一次问全资产清单→搜官方渠道取 logo/产品图/UI 截图(svgl→simpleicons→favicon 三级兜底)→验证后固化为 brand-spec.md。
- 任何新视觉设计必过三方向硬门:写 ≥500 字设计 spec → 并行 spawn 3 个互不参考的 subagent,分别按秒数轮盘随机风格、真实获奖案例迁移、顶级设计师人格,各产出一版真实 HTML 初稿并截图。
- 三张截图摆给用户,展示后停止回合等用户选(可混合);选定后写入 direction-approved.md,回标准流程:答 form 推导五问 → 写带 assumptions/placeholder 的 HTML 尽早 show → 用户点头后才填内容迭代。
- 验证交付:Playwright 截图自检 + 控制台报错归零;动画默认经 HyperFrames/渲染管线导出带 BGM+SFX 的 MP4,而非纯画面。

- 三方向生成机制(反同质化核心):3 个 subagent 只共享同一份 spec、互不参考,逻辑互补——🎲 date +%S 取秒数 %20+1 从 60 风格库随机抽、🏆 WebSearch 核实真实获奖标杆(Awwwards 等)再拆解迁移、🧠 假设预算无上限选最契合的设计师/工作室;硬校验:三版布局骨架必须结构性互异,design-demos/ 下 <3 个 .html 即判定偷懒,补齐才放行。
- 资产强制校验机制:设计里出现任何可识别的产品名,官方 logo 就是必需资产,取不到 = 🛑 STOP 补齐(仅允许降级为标注「logo 待补」继续);单文件交付物中图片必须 base64 内嵌防裂图;内容必需的真图先取(如 Wikimedia/Unsplash/官方渠道,scripts/fetch_images.py)再设计,禁止边设计边用色块糊弄。
- 验证与导出管线(外部依赖集中处):WebSearch API(事实+标杆核实)、Playwright CLI(截图与 3 项点击测试、pageerror=0)、Node/npm 的 HyperFrames 后端(动画渲染,五门审计 npm run check)、内置 Python/Shell 脚本(取图、导 PDF、render-video.js → verify-video.sh 硬校验 → convert-formats.sh → add-music.sh 加 BGM,配 37 个预制 SFX mp3);生图仅在用户确认有生图能力时走 nano-banana-pro。
