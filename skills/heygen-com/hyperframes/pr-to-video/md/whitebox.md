# pr-to-video (`heygen-com/hyperframes/pr-to-video`)

## whitebox

- Setup (Step 0): 解析 PR 引用 → npx hyperframes init 建项目, 写 BRIEF.md 锁定需求, 确认 HeyGen 登录或离线降级
- Ingest (Step 1): fetch-pr.mjs 调 gh 拉 PR 元数据和 diff, ingest.mjs 离线转成 tokens/文案/贡献者名单, 顺带下载贡献者头像
- 设计+剧本 (Step 2-3): 应用 code-editorial 视觉预设生成 frame.md, 写分镜 STORYBOARD.md 和配音稿 SCRIPT.md, 用户审核通过才继续
- 音频+视觉 (Step 3.1-4): 后台跑 audio.mjs 生成旁白/词级时间戳/BGM, 同时给每帧补写时间轴镜头序列并选定 code-* 代码块
- 建帧+渲染 (Step 5-6): 把每帧时长同步到真实配音, 并行派发 frame worker 产出 HTML 组合帧, 最终渲染成 renders/video.mp4

- 确定性摄取链: fetch-pr.mjs 走 gh CLI 并用分页 gh api 补全大 PR 的文件列表 (防 ~100 条截断), 输出 capture/pr.json + diff.patch; ingest.mjs 纯离线转换出 tokens.json (colors 为空 → 采用 code-editorial 调色板)、visible-text.txt、people.json (过滤 bot, 头像映射 assets/<login>.png); gh 认证/404/私有仓库时 exit 1 直接终止, 绝不编造 PR 内容
- 时长以配音为准: 旁白用 HeyGen TTS API (已登录) 或本地 Kokoro 引擎 (am_/af_ 前缀音色), 输出词级时间戳; sync-durations 机械地把每帧时长对齐真实语音时长并禁止手改; BGM 从 HeyGen 曲库检索 (retrieval, 非生成), SFX 同源获取
- 门禁 + 并行建帧: Step 0/3/6 是用户审核门 (自主模式降级为简报放行); Step 5 按 subagent-dispatch 规范打包 bounded packets 派发给并行 frame worker, 每帧只附 ≤12 行精确 diff 摘录 (### Source excerpt) 且工人被禁止重开完整 diff, 防止渲染与源码脱节
