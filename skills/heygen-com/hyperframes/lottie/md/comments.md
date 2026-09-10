# lottie (`heygen-com/hyperframes/lottie`)

## comments

- user: AE动效设计师, category: 坑, comment: 我把 LottieFiles 的在线链接直接填进 path, 浏览器预览正常, 渲染出来动画却是空的。下载 JSON 放进 assets/ 用本地路径就好了。
- user: 前端新手, category: 坑, comment: 忘了写 autoplay: false, 播放器自己开跑, 帧时间全对不上。改 false 并 push 进 window.__hfLottie, 才被逐帧对齐。
- user: 从Remotion迁移来的工程师, category: 妙用, comment: 之前 Remotion 里的 Lottie JSON 直接复用, 改成本地 path 再注册到 window.__hfLottie, 半小时就迁移完一个片头。
- user: 后端老兵, category: 注意, comment: 渲染前先跑 npx hyperframes lint 和 validate, 我就是靠 validate 才发现有个动画没注册上, 不然成片平白缺一层。
- user: UI设计师, category: 坑, comment: AE 里某个蒙版效果导出 JSON 后不生效, 我开浏览器先预览才发现掉效果, 换成受支持的写法重新导出才过。
- user: 短视频创作者, category: 妙用, comment: 背景、图标、彩带三个动画都 push 进同一个 window.__hfLottie, 全被 seek 到同一时间点, 多层同步一行对时代码都不用写。
