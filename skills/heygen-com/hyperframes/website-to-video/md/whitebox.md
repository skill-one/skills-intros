# website-to-video (`heygen-com/hyperframes/website-to-video`)

## whitebox

- Step 0: 抓取目标网站, 提取品牌与产品信息 (策略优先), 并运行 npx hyperframes auth status 确认语音/配乐引擎的登录状态
- Step 1-2: 写 DESIGN.md 品牌速查表 (色板/字体/do's & don'ts), 再与用户锁定视频类型、时长、格式、核心信息与叙事弧
- Step 3-4: 产出 STORYBOARD.md + SCRIPT.md 并获用户批准; 若需旁白则选 TTS 生成 narration.wav, 转录后回填每个 beat 的真实时长
- Step 5: 构建 index.html + compositions/beat-N.html, 子代理对每个 beat 跑 hyperframes lint + snapshot, 主代理对照 DESIGN.md 和 STORYBOARD.md 逐行通读校验
- Step 6: 跑 npx hyperframes check 零错误后交付 localhost Studio 项目链接; 仅在用户明确要求时才渲染 MP4

- 工件门控链: 7 步各产出一个工件, 前一步工件是后一步的准入条件; 💬 用户偏好类门 (选 TTS/配音/音乐等) 在自主模式下可跳过, 但质量验证门 (资产审计、逐 beat 通读、DoD 清单、诚实披露) 任何模式不可跳过
- 品牌优先而非截图拼接: 抓取物是品牌工具箱 — design-styles.json 提供精确计算值喂给 DESIGN.md, 视频由 storyboard 的 beat 映射为 HTML 合成来构建; 子代理构建, 主代理用结构化证据块逐 beat 验收
- 外部依赖: HyperFrames CLI (npx hyperframes lint/snapshot/check + Studio 本地预览服务器) 为主执行环境; 旁白走 HeyGen / ElevenLabs / Kokoro 三选一 TTS; 媒体素材经 /media-use 查 HeyGen 目录; figma.com 链接先走 /figma 技能做资产导出与品牌 token 绑定, 再进入本流程
