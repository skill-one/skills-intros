# hyperframes-media (`heygen-com/hyperframes/hyperframes-media`)

## whitebox

- 先预检: 跑 `npx hyperframes auth status` 并把输出原样转述给用户; 未登录则停下, 等用户选登录 (auth login) 还是本地降级, 不擅自生成
- 把任务写成一份中立的 audio_request.json: lines[].id 关联回调用方的模型 (帧号/场景 id), 附 bgm.mode / provider / lang / speed
- 调唯一引擎 `node <skill>/scripts/audio.mjs --request … --out audio_meta.json`, 产物落盘 assets/voice|bgm|sfx
- 引擎按凭证开关自动选 provider 链完成 TTS/BGM/SFX; ElevenLabs/Kokoro 无原生词级时间戳时, 引擎自动串联 Whisper transcribe 补齐
- 产出 id 索引的 audio_meta.json (每句 path/duration_s/words), 下游字幕/动画按 {id,text,start,end} 扁平词数组消费

- 单引擎收敛: 不自研/不拷贝音频逻辑, 一切经 scripts/audio.mjs; --only tts,bgm,sfx 可分批跑并合并进已有 --out (如先 TTS+BGM, SFX 等出 cue 再补); BGM 本地生成是 detached 进程 (bgm_pending:true), 组装前跑 wait-bgm.mjs 等待
- 一把凭证开关 heygenCredential(): 有 HeyGen 凭证 → TTS 走 Starfish REST (原生词时间戳), BGM/SFX 走 /v3/audio/sounds 检索 (SFX min_score 0.4); 无 → TTS 链 ElevenLabs→Kokoro-82M 本地, BGM 链 Lyria→MusicGen 本地生成, SFX 落内置 21 文件库; 显式 bgm.mode=retrieve 是严格的 (无匹配即跳过, 不转生成)
- 词级对齐 + 产物纪律: HeyGen 原生返回词时间戳, 其余 provider 靠 Whisper (transcribe 必须显式 --model, 默认 small.en 会静默翻成英语) 补出 {id,text,start,end}; 字幕 HTML 视为生成产物 — 可复用皮肤源在 .hyperframes/caption-skin.html, 不直接编辑生成的 compositions/captions.html
