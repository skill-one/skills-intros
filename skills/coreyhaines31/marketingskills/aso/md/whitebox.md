# aso (`coreyhaines31/marketingskills/aso`)

## whitebox

- 识别商店：按 URL 结构判定是 Apple 还是 Google Play；若只给了应用名，则网络搜索（site:apps.apple.com / site:play.google.com）定位商店页。
- 抓取文本：用 WebFetch 拉取商店页，按平台字段清单逐一提取元数据（标题、副标题/短描述、评分、截图数等）；抓不全则记录缺口，必要时请用户补贴关键字段。
- 评估视觉：对列表页整页截图，评估图标、截图张数与文案、预览视频、Feature Graphic（Google Play）；WebFetch 拿不到图片，截图不可用时改为向用户索要。
- 品牌分层：将应用归入 Dominant / Established / Challenger 三档，决定后续各项的评分宽严（大牌的'教科书偏差'视为有意为之，不扣分）。
- 评分出报告：按 6 个维度加权打分得出百分制总分与等级，输出记分卡、Top 3 速赢项、逐维详情、关键词建议和按'影响 vs 成本'排序的行动计划。

- URL 模式匹配做商店识别：Apple 匹配 apps.apple.com/{country}/app/{name}/id{数字}，Google 匹配 play.google.com/store/apps/details?id={包名}；无 URL 时回退到 site: 网页搜索。依赖 WebFetch 工具 + 浏览器截图能力，无外部模型 API。
- 双通道取数 + 防注入：WebFetch 负责文本元数据，页面截图补足 WebFetch 无法提取的图像/截图文案；抓到的列表与评论一律视为不可信数据——只分析内容，绝不执行其中嵌入的指令。
- 参考文件驱动的加权评分引擎：依据内置 references/（scoring-criteria、apple-specs、google-play-specs、benchmarks）打分，权重为标题 20% / 描述 15% / 视觉 25% / 评分评论 20% / 元数据 10% / 转化信号 10%；品牌分层先行调节宽严。建议输出锚定两平台索引模型差异（如 Apple 不索引长描述、靠隐藏 100 字节关键词字段；Google 全文索引、要求 2–3% 关键词密度），同一条优化分平台给法。
