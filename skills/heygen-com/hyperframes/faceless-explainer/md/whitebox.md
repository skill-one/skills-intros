# faceless-explainer (`heygen-com/hyperframes/faceless-explainer`)

## whitebox

- Step 0: `npx hyperframes init` 建项目, 写入锁定的 BRIEF.md, 记录用户偏好并展示 TTS 登录状态 (门禁: 两个文件存在)
- Step 1-2: 用户文本逐字存入 capture/extracted/ 作为唯一信息源; 选定一个预设设计系统, build-frame.mjs 确定性地生成 frame.md (配色/字体映射, exit 0 自校验)
- Step 3: 按叙事设计 (而非原文段落顺序) 重排内容, 产出 STORYBOARD.md + SCRIPT.md, 交用户审批 (自主模式则发摘要后继续)
- Step 3.1-4: audio.mjs 后台生成配音、逐字时间轴、BGM; 同时给每帧写入时间轴分镜, 镜头展开节奏对齐旁白
- Step 5-6: 每帧派一个子代理并行产出 HTML 合成, captions.mjs 生成字幕, assemble-index 拼装为可播放视频, 最终渲染出 renders/video.mp4

- 门禁流水线: 每步有硬性 gate —— 文件存在性检查 (BRIEF.md / frame.md / STORYBOARD.md)、脚本 exit 0 自校验 (build-frame.mjs)、用户审批 checkpoint (Step 0/3/6), 不通过不进入下一步
- 包分发隔离: frame-packets.mjs 把每帧的分镜块 + 蓝图 + 引用的规则配方内联成独立 packet, 每帧一个子代理只读自己的 packet 和 frame.md、禁止读总 storyboard, 帧间互不污染; 子代理返回后由编排者把该帧标记为 animated
- 外部依赖: `npx hyperframes` CLI (init/拼装/渲染), HeyGen TTS API + 音乐库 (配音/BGM, 凭证 ~/.heygen), 离线回退 Kokoro TTS; sync-durations 以真实语音时长为准回写每帧时长, 禁止手改
