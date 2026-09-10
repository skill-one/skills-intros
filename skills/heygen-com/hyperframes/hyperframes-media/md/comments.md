# hyperframes-media (`heygen-com/hyperframes/hyperframes-media`)

## comments

- user: 第一次做口播视频的新手, category: 坑, comment: 配了 HeyGen key 跑 `npx hyperframes tts`,出来还是本地 Kokoro 的声音——公开 CLI 会静默回退。要真 HeyGen 得走引擎的 heygen-tts.mjs。
- user: 做双语网课的老师, category: 坑, comment: 转写中文音频没传 --model,默认 small.en 把整段中文静默翻成英文,词级字幕全废。重跑显式指定模型才拿到中文时间轴。
- user: 后端老兵, category: 妙用, comment: 先 --only tts,bgm 拿音频时长定布局,SFX 等画面点位确定后再单独跑一次,自动合并进同一个 audio_meta.json,语音不用重生成。
- user: 独立开发者, category: 注意, comment: 出音频前先 `npx hyperframes auth status`,没登录它会给出注册指引和本地回退引擎清单,选完再继续。登录用 auth login 浏览器授权,key 别写进仓库 .env。
- user: 短视频剪辑, category: 妙用, comment: SFX 检索按文字相似度打分:query 写「glass shatter」稳中,写「dramatic sound」落空——而且没命中是静默跳过,回头数一下 audio_meta.json 里 sfx 条数。
- user: 赶工期的剪辑师, category: 坑, comment: 无凭证时 BGM 走本地生成,是后台任务,bgm_pending 为 true。我没等就去拼视频,BGM 空了;先跑 wait-bgm.mjs 再合成就好。
