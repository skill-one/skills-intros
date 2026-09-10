# general-video (`heygen-com/hyperframes/general-video`)

## whitebox

- 先自检技能版本 (npx hyperframes skills update general-video),再按项目状态表分流: 有 BRIEF.md 就读它,已有 hyperframes.json/STORYBOARD 则续作,全新项目先跑 /hyperframes 定意图并 init 目录。
- 从 BRIEF 契约解析运行形态三字段: flow (谁主导)、storyboard (评审面开关)、mode (由契约推导,不问用户),automation 模式还需一句话声明所选路线。
- 按条件渐进式加载 references 后,依依赖序执行: 规划 (viewer arc/节奏/时长驱动, 多场景写入 STORYBOARD.md 的 Frame 块) → 可选评审 → 备齐素材 (音频尽早, 真实配音时长覆盖估算) → 逐场景构建。
- 组装: 挂载场景/媒体/转场/字幕/音频;校验: npx hyperframes lint 快速反馈,最终 gate 是 npx hyperframes check (内含 lint, 不重复跑)。
- checks 全过后才打开 Studio 最终预览请用户批准,批准后才渲染并验证渲染产物;多场景还需回看 animation-map。

- 状态机分流 + 确定性渲染契约: 项目状态表取第一匹配行执行 (specific edit 不重开 discovery);每个合成 HTML 用 class="clip" 标记计时元素,在 window.__timelines 注册唯一 paused、可 seek 的时间线;禁止渲染期网络请求、时钟、未播种随机数,保证可复现。
- 渐进式披露 + 依赖序: 不靠记忆,条件命中才读对应 reference (任何动效必读 /hyperframes-animation, 任何媒体必读 /media-use, companion 首个 plan 前必读 story-spine/house-style/capability-menu);构建按 plan→review→resolve→build→merge→assemble→verify 顺序,跳过无输入的阶段。
- 规模化时分发并行: 超过 ~6 短场景才值得分发;用 frame-packets.mjs 把每场景的 storyboard 块+blueprint+规则配方打成独立 packet,子代理每包 2-3 场景、单波全发,只读 packet 和设计真相文件,产出 compositions/<frame_id>.html + motion.json sidecar,由主上下文合并时长与出入场向量;外部依赖: npx hyperframes CLI (init/lint/check/auth status)、node 脚本 (prefs/recipe/animation-map.mjs)、Figma URL 强制走 /figma 适配、媒体走 /media-use 的 provider 解析。
