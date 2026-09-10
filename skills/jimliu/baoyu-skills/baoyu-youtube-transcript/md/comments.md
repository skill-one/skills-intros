# baoyu-youtube-transcript (`jimliu/baoyu-skills/baoyu-youtube-transcript`)

## comments

- user: 第一次用的新手, category: 坑, comment: 直接把链接粘进终端没加引号，zsh 报 no matches found。链接里的 ? 会被当通配符，整个 URL 用单引号包住就正常了。
- user: 视频剪辑师, category: 妙用, comment: 先跑默认格式拉字幕，数据就缓存了；再补 --format srt 秒出文件不用重新下载，SRT 直接拖进剪辑软件当字幕底稿。
- user: 英语播客听众, category: 注意, comment: 中文视频默认按英文找，会报 No transcript found。先 --list 看有哪些语言，再用 --languages zh 指定，别瞎猜。
- user: 后端老兵, category: 妙用, comment: 一口气批量跑了几十个视频 ID，中途被 bot detected 拦住，设 YOUTUBE_TRANSCRIPT_COOKIES_FROM_BROWSER=chrome 后全部跑通。
- user: 研究生, category: 启发, comment: 访谈视频用 --chapters --speakers，出来就是带人名的分章稿，引用时按时间戳回原视频核对，比反复拖进度条快太多。
- user: 自媒体运营, category: 注意, comment: --chapters 只认博主写在视频简介里的时间戳，简介没写就不会自动分段。挑视频前先翻一眼简介有没有章节。
