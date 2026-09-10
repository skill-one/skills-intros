# changelog-video (`heygen-com/hyperframes/changelog-video`)

## whitebox

- 步骤0 从 skill 自带资产引导项目: 复制字体/BGM/背景视频/master-skeleton 骨架到项目目录, 再通读 build-spec 品牌规范 — 不可跳过
- 解析 changelog .md 并做编辑取舍: 按 45-60s 预算切主题, 每主题只留 1 个主可视化 + 最多 3 条口播项, 并按 visualization-registry 为每个主题选定可视化形式
- 写双层脚本: 按 lexicon.json 把技术词拆成 spoken (读音, 喂 TTS) / display (标准拼写, 进字幕) 两层, 存 script-tokens.json; 词典缺词则停下问用户
- 生成语音与字幕时间轴: 调 HeyGen TTS (Annie, 固定音色) 合成 VO 拿到逐词时间戳 vo-words.json, 再用 align-captions.mjs 把口语时间戳对齐回 display 拼写得到 captions.json
- 构建并过闸门: 在骨架内只填占位符与字幕 LINES, 依次跑 hyperframes check / seam-gate verify / 抽帧确认字幕可见, 全绿才交付; 用户不要求就不渲染

- 资产即品牌 (防跑偏机制): 品牌一致性不靠重写, 靠步骤 0 原样复制 skill 自带字体/BGM/背景 MP4/HTML 骨架, 场景内容只填脚手架占位符; 一旦发现自己在手写 @font-face、复用旧视频 index.html 或自制背景, 立即删除重建回正确脚手架
- 双层脚本 + 词典驱动: script-tokens.json 把每个技术词分为 spoken (音译形式, 只进 TTS 文本) 与 display (标准拼写, 只渲染字幕), VO 读口语、字幕显标准; 词典外词汇禁止猜测读音, 必须先问用户并回写 lexicon.json
- 音频即时钟 + 硬性校验门: HeyGen TTS 返回的 vo-words.json 逐词时间戳是所有节拍/切缝的唯一时间源, 缺时间戳时回退用 whisper 强制对齐 (字幕拼写仍取 display 层); 交付前必须全绿: hyperframes CLI 字幕区检查 (0 error) → seam-gate.mjs verify (0 fail) → 抽帧确认字幕在 spoken 区间可见。外部依赖: heygen CLI (TTS api), align-captions.mjs, openai-whisper (uvx), hyperframes CLI, seam-gate.mjs, ffmpeg
