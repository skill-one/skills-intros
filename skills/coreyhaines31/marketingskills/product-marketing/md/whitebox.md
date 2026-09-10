# product-marketing (`coreyhaines31/marketingskills/product-marketing`)

## whitebox

- 检查 `.agents/product-marketing.md` 是否已存在, 同时探测旧位置 (`.claude/`、旧文件名 `product-marketing-context.md`), 发现旧文件则提议迁移到规范路径
- 文档不存在时提供两种模式: 从代码库自动起草 (推荐) 或对话式从零逐节收集
- 收集信息: auto-draft 模式通读 README、落地页、营销文案、package.json、既有文档后起草全部章节, 交用户审阅纠错; 从零模式一次只问一节, 确认后再推进, 并推动用户提供客户原话
- 按固定 12 节模板 (Product Overview → Goals) 生成完整文档
- 设置版本号 (新文档 v1) 并追加 ISO 日期格式的 Changelog 条目, 保存到 `.agents/product-marketing.md`, 告知其他 marketing skill 将自动引用此上下文

- 双模式信息抽取: 默认走 auto-draft —— 把代码库资产 (README / 落地页 / package.json / docs) 当作事实来源推断 12 个章节, 用户只需纠错补漏; 收集时强制索取客户逐字原话 (verbatim), 因为原话比润色过的描述更能反映真实心智
- 纯文件读写, 零外部依赖: 不调用任何外部工具、库或模型 API, 输入靠读仓库文件, 输出是单个 Markdown 文件; 唯一的文件系统兼容逻辑是探测旧安装位置并提供迁移
- 版本 + Changelog 纸质痕迹: 每次实质性保存版本号 +1, Changelog 新条目 prepend 到顶部 (newest first), 条目须写清改了哪些章节及原因; 仅纯 typo 修复不升版本不记条目 —— 因为该文档是所有下游 marketing skill 的共享上下文, 变更历史必须可追溯
