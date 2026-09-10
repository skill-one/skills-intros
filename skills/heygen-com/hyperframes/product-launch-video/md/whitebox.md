# product-launch-video (`heygen-com/hyperframes/product-launch-video`)

## whitebox

- Step 0 初始化: 读取/锁定 brief 写入 BRIEF.md, `npx hyperframes init` 创建项目 → `hyperframes.json`, 展示登录状态 (决定用 HeyGen 云端还是本地离线引擎)
- Step 1 抓取: `npx hyperframes capture <产品URL>` 抓站 → 截图、品牌色/字体 tokens.json、可见文本、素材清单 asset-descriptions.md (可选视觉模型自动写图注); 抓取失败是硬停, 不伪造素材
- Step 2-3 设计+剧本: `build-frame.mjs --preset` 用品牌 tokens 生成设计系统 frame.md; 写分镜 STORYBOARD.md 和旁白 SCRIPT.md, 用户审核通过才放行
- Step 3.1-4 音频+视觉细节: 后台跑 audio.mjs 生成旁白、字级时间轴、按 mood 检索 BGM → audio_meta.json; 同时给每帧补时间轴镜头序列与运动细节 (跨帧元素写 handoff 数值契约)
- Step 5-6 出片: 每帧派一个 sub-agent 生成 compositions/frames/NN-*.html + index.html, 最后装配渲染 → renders/video.mp4

- 门控流水线: 8 步严格按序, 每步有硬 gate — 文件存在性检查、capture 结果 `ok:true` 且无 BLOCKED.md、脚本 exit 0、用户审批 (Step 0/3/6 三个用户门控); gate 不过即停, 不降级续跑
- 确定性设计转换: build-frame.mjs 把选定预设的 FRAME.md 按角色 (ink/canvas/accents) remix 到抓取的品牌 tokens 上 (颜色按角色映射、字体替换、复制字幕皮肤), 自校验映射失败 exit 1 — 脚本确定性执行, 不手改设计规格
- 时间轴驱动装配: 旁白经 HeyGen TTS API (离线回退 Kokoro 本地引擎) 产出字级 word timings, BGM 按分镜 music 字段从 HeyGen 音乐库检索 (检索而非生成); 跨帧元素用 handoff_out/handoff_in 的数值契约约束并行 sub-agent 的接缝一致, 最终按 audio_meta.json 时间轴装配渲染 mp4。依赖: HyperFrames CLI (npx hyperframes)、HeyGen Audio API、Kokoro、可选视觉模型 (Gemini/Google/OpenRouter) 做素材图注
