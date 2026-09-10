# mediabunny (`remotion-dev/skills/mediabunny`)

## comments

- user: 做视频上传的前端, category: 妙用, comment: 用户传视频前,我直接在浏览器里读出时长和宽高做校验,超时长当场拦截,不用传到服务器再打回,省一整轮上传流量。
- user: 第一次用的新手, category: 坑, comment: 我在 Node 脚本里装完包直接跑,报错起不来——它是浏览器端库,得在网页环境里用,别拿到后端脚本里折腾。
- user: 全栈老哥, category: 注意, comment: 读时长不用真的播放视频,别再走 new Video() 等 loadedmetadata 那套老路,直接读元数据更快,还少一堆兼容坑。
- user: Remotion 使用者, category: 妙用, comment: 合成前先用它读素材宽高,发现竖屏素材混进来就提前提示,不然渲染完才发现画面被裁,重渲一次半小时没了。
- user: 音视频工具站站长, category: 注意, comment: 音频时长、视频时长、视频尺寸是三份独立指南,先确认要哪个再翻,我曾在音频文档里翻半天找视频尺寸。
- user: 独立开发者, category: 启发, comment: 以前文件元数据校验全靠后端,现在浏览器就能拿到时长和分辨率,我把上传前的校验全挪到前端了,接口只留兜底。
