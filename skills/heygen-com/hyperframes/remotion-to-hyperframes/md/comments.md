# remotion-to-hyperframes (`heygen-com/hyperframes/remotion-to-hyperframes`)

## comments

- user: 前端组长, category: 坑, comment: 项目里有子组件用 useState+useEffect 驱动动画,lint 一跑直接拦下拒绝翻译。先跑 lint 再决定要不要迁,别急着动手。
- user: 第一次用的新手, category: 坑, comment: 我说「照我 Remotion 视频再做一个」,结果被带去全新制作,源码根本没翻。想迁移必须明说「移植/迁移」这类字眼。
- user: 独立开发者, category: 妙用, comment: 我把 SSIM 分数当迁移验收指标,低于阈值不放行;哪几帧偏了跑 frame_strip 一看便知,定位超快。
- user: 后端老兵, category: 注意, comment: 对比渲染前,先在 remotion.config.ts 里把图片格式设为 png、色彩空间设 bt709,否则 diff 全是编码差异,翻译背黑锅。
- user: 动效设计师, category: 启发, comment: lint 的 blocker 清单点醒我:靠运行时状态驱动的动画,天然不适合逐帧渲染。以后写动画尽量做成纯时间函数。
- user: 全栈工程师, category: 妙用, comment: 源码里一堆 @remotion/lambda 云渲染配置,本想手删,结果它只算警告、其余照翻,丢弃项都记在 TRANSLATION_NOTES.md。
