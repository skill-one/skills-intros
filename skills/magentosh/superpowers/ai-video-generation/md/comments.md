# ai-video-generation (`magentosh/superpowers/ai-video-generation`)

## comments

- user: 第一次用的新手, category: 坑, comment: 直接跑 belt 报 command not found,原来是 CLI 没装。先 npx skills add belt-sh/cli 装好,再 belt login 登录,这两步走完才能生成第一条视频。
- user: 预算敏感的自由职业者, category: 坑, comment: 图便宜选了没标音频的 WAN-T2V,出来是无声的,白跑一遍。要带声音直接选 Veo 3 / Seedance 2.0 / P-Video;另外单段都只有几秒,长片分段生成后用 media-merger 拼。
- user: 电商详情页美工, category: 注意, comment: 图生视频只认 image_url,我贴本地文件路径直接报错。把图先传到可公开访问的图床,拿链接再跑,一次就过,产品图动效都这么出。
- user: 短视频账号运营, category: 妙用, comment: 系列片最愁主角换脸。用 Seedance 2.0 传同一张定妆照作 reference_image,每集人物长相一致,还自带同步音频,不用一集集抽卡碰运气。
- user: 后期剪辑外包, category: 妙用, comment: AI 素材没声音?HunyuanVideo Foley 按提示词补脚步、环境音,Topaz 升画质,再用 media-merger 加 fade 拼成片,小单子全程没开剪辑软件。
- user: 后端老兵, category: 启发, comment: 每步都是命令行,我把 text-to-speech 配音 → OmniHuman 1.5 口播 → media-merger 拼接写成脚本,此后每期只改文案和提示词,一条命令出整支口播视频。
