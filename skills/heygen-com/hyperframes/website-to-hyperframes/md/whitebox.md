# website-to-hyperframes (`heygen-com/hyperframes/website-to-hyperframes`)

## whitebox

- Step 0: 抓取用户给的 URL, 提取品牌/产品/资产数据, 先打印策略优先的站点摘要 (产品做什么、给谁用、品牌语气)
- Step 1: 写 DESIGN.md 品牌速查表 (配色、字体、组件风格), 作为后续所有构建的视觉基准
- Step 2+3: 与用户对齐视频类型/时长/格式/信息与叙事弧 → 产出 STORYBOARD.md + SCRIPT.md, 用户批准后才继续
- Step 4: 用 TTS 生成配音 → 转录出带时间戳的 transcript → 按真实语音时长回写各节拍 (beat) 的时长
- Step 5+6: 构建 index.html + compositions/beat-N.html, 逐拍审查 + lint/validate/快照全部通过后, 交付 localhost Studio 项目 URL (MP4 仅在用户明确要求时渲染)

- 工件门控流水线: 每步的产出物 (站点摘要 → DESIGN.md → STORYBOARD.md/SCRIPT.md → narration.wav+transcript.json → 合成 HTML) 是下一步的前置条件; 💬 标记的用户偏好门 (TTS 提供商、音乐、字幕等) 在自主模式下由 agent 代决, 但验证类门 (资产逐个 USE/SKIP 审计、逐拍 HTML 全文通读、DoD 清单) 任何模式下不可跳过
- 外部依赖: TTS 三选一 (HeyGen TTS / ElevenLabs / Kokoro) 生成语音; hyperframes CLI (npx hyperframes lint / validate / snapshot) 做校验与快照; 最终交付 localhost Studio 项目; 另有子 agent 在 Step 5 对每拍跑 lint+snapshot 后汇报
- 验证闭环: 主 agent 对照 DESIGN.md 与 STORYBOARD.md 自上而下通读每个 beat HTML; 最终 gate 要求 lint+validate 零错误, 快照数量按 max(beats×3, ceil(时长秒/2)) 缩放并逐张审看, 收尾必须附「What I did NOT verify」诚实披露
