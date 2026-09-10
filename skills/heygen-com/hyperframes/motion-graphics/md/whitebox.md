# motion-graphics (`heygen-com/hyperframes/motion-graphics`)

## whitebox

- Init: 用 `npx hyperframes init` 在 `videos/<project-name>/` 生成项目骨架 (hyperframes.json), 后续所有产物都落在这个目录。
- Plan: Director 子代理先裁决"要不要搜素材", 再定类别 (表单类 kinetic-type/stat/charts/logo-reveal/lower-thirds/maps, 或搜索驱动类 webpage/news/tweet/asset-fusion), 产出 shot-plan.json 草稿。
- Source (条件步): asset_needs 非空时用 media-use resolve 检索/生成素材并冻结到 assets/ (图像生成依赖 GEMINI_API_KEY, 缺 key 则降级为免素材); 纯文字/数据类直接跳过。
- Design→Build: Director Part 2 围绕素材定稿 shot-plan.json (catalog 块 + 布局 + 动效节拍), Builder 子代理 reuse-first 组装 compositions/index.html — 优先 `hyperframes add` 套现成块, 只手写缺口。
- Verify→Render: lint / check / snapshot 三道门, 人工检视 proof 快照; 通过后问用户"预览还是渲染", 获明确确认后 `hyperframes render` 输出 MP4。

- 子代理流水线、文件即接口: 每阶段派发一个 subagent, prompt = 整份 agent 指南 (agents/director.md / builder.md / finalize.md) + dispatch 上下文 (SKILL_DIR / PROJECT_DIR / shot-plan 的 JSON Schema); 阶段间只靠磁盘产物交接 (shot-plan.json → assets/ → compositions/index.html), 按断点表可从任意状态续跑。
- 确定性动画契约: 产物 HTML 是暂停的 GSAP 时间轴, 挂在 window.__timelines, 配 class="clip" + 稳定 id, tl.seek(0) 可归零重放 — 保证渲染器可逐帧确定性出片; 动效词汇集中在 references/motion-vocabulary.md, 映射到 hyperframes-animation 规则/蓝图。
- 校验与渲染管线: lint→check→snapshot (--at 指定开场 / 招牌动作 / 结尾 hold 三个 proof 时刻) 任一失败则派 finalize 修复子代理原地修一轮、只重跑失败的 gate, 禁止改时长掩盖缺陷; 渲染由 hyperframes CLI 基于确定性时间轴完成 (可开 GPU), 输出 MP4 或 webm/mov 透明 overlay; 系统依赖 node + ffmpeg。
