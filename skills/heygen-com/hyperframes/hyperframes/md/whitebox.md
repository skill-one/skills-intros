# hyperframes (`heygen-com/hyperframes/hyperframes`)

## whitebox

- 判定项目状态: 存在 BRIEF.md → 直接执行其指定的工作流; 现有项目只做指定操作; 全新创建 → 进入意图访谈
- 意图访谈 (references/intent-interview.md): 通过提问确认主题、需求与偏好, 最终落盘 BRIEF.md —— 它是唯一被下游读取的路由产物
- 一次性路由: 按交付物匹配 §2 的 9 级优先级表 (slideshow/captions/music-to-video/general-video 等), 只读被选中路由的 route 文件; 匹配不上则继续顺延路由
- 安装并进入工作流: npx hyperframes skills update <workflow-name>, 再按需加载领域技能 (/hyperframes-core 动画/音频/CLI 等)
- 按契约编写 HTML 合成 (用 data-* 属性声明时序), 经 CLI 校验 (check) 后渲染输出视频

- HTML 即视频: 合成是一个 HTML 文件, DOM 用 data-* 属性 (data-start / data-duration / data-media-start) 声明时序与轨道布局, 动画运行时可 seek, 媒体播放权由框架接管
- 状态机 + 单次路由: 先过项目状态表 (BRIEF.md / 现有项目编辑 / Remotion 移植等短路规则), 不命中才走路由表; 路由只发生一次, 之后一律从 BRIEF.md 取答案, 不再重开访谈
- 惰性技能加载 + npx hyperframes CLI 工具链: 领域技能按需加载; 渲染前用 upgrade --check 探测版本 pin、用 check 校验合成; 动画可用 GSAP / CSS / Anime.js / WAAPI / FLIP, 另有 Figma 资产接入 (skill.md 未提及任何模型 API 依赖)
