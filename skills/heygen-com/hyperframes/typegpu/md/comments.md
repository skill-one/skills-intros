# typegpu (`heygen-com/hyperframes/typegpu`)

## comments

- user: 第一次用的新手, category: 坑, comment: 把字幕的 GSAP tween 写在 await 初始化之后, 时间轴读不到, 动画全程不动。挪到任何 await 之前同步注册就正常了。
- user: 短视频混剪作者, category: 坑, comment: video 直接喂 GPU 纹理, 浏览器预览没问题, 一进渲染模式 copyExternalImageToTexture 就报错。用 FFmpeg 先抽关键帧成 PNG 再加载, 出片才稳。
- user: 图形老手, category: 妙用, comment: 从 Three.js 转来, 习惯 requestAnimationFrame 自绘。改成只听 hf-seek、用 e.detail.time 重绘后, 拖进度条 GPU 帧和字幕逐帧对齐, 一帧都不错位。
- user: 做粒子开场特效的, category: 注意, comment: 默认 alphaMode: opaque 会把下面的 HTML 视频全盖住。粒子叠层要用 premultiplied, alpha=0 处自动透明, 才透得出底下的画面。
- user: UI 动效设计师转前端, category: 妙用, comment: 单 pass 高斯怎么调都糊不出磨砂感。先渲一张 1/6 分辨率小纹理, 合成时双线性放大当磨砂内部, 全分辨率留给锐边和色散, 玻璃质感一次到位。
- user: 批量出片的渲染运维, category: 注意, comment: 粒子初速用了 Math.random(), 每次 seek 位置都变, 帧间乱跳。换固定种子 PRNG; submit 后记得 await onSubmittedWorkDone, 免得截到黑帧。
