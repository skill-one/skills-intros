# remotion-multimedia (`remotion-dev/skills/remotion-multimedia`)

## comments

- user: 前端上传组件负责人, category: 妙用, comment: 我在上传前就先读视频时长和宽高,不合规的文件当场拦截,不再等传完被后端打回,省下一整轮重传流量。
- user: 第一次用的新手, category: 坑, comment: 我以为是全能视频库,后来才发现它只管读元信息(时长、宽高),剪辑、转码、播放都不行,需求别放错位置。
- user: 后端老兵, category: 启发, comment: 以前时长和分辨率都得后端解析存储,现在前端拿到文件瞬间就能读,我把校验逻辑整个前移,后端只剩兜底。
- user: 做过 CLI 工具的运维老哥, category: 注意, comment: 它只能在浏览器里跑,我想写个本地脚本批量扫文件夹,不行;批量场景得开网页逐个选文件,或另想办法。
- user: 全栈独立开发者, category: 妙用, comment: 用户一选完文件我立刻读宽高,先把播放器容器尺寸摆好再加载视频,页面不再跳动,横竖屏混排也不乱了。
- user: 前端实习生, category: 注意, comment: 音频时长、视频时长、视频宽高是三份独立指南,我一开始只翻了一份以为缺功能,其实该分开各看各的。
