# audit-website (`squirrelscan/skills/audit-website`)

## whitebox

- 对目标站运行 `squirrel audit <URL> --format llm` 做第一轮快速扫描 (quick 模式, 默认 25 页), 拿到紧凑报告: 健康分、等级、按严重度排序的问题
- 向用户展示报告并列出可修复项, 经用户确认后才开始改代码
- 用 Grep/Glob/Read 把每条问题定位到源码中对应的模板/组件/内容文件
- 按批次用 Edit 应用修复, 每批后验证项目仍可构建、现有检查通过
- 用 `--refresh` 重新审计并展示前后分数对比; 未达分数目标则回到定位修复步骤迭代, 直到达标或只剩需人工判断的问题

- 扫描全部依赖外部 `squirrel` CLI (需在 PATH 中): 覆盖 SEO/性能/安全/技术/内容/无障碍等 20 类共 260+ 条规则; `--format llm` 输出省 token 的紧凑 XML/文本混合报告; 审计结果本地缓存, 可用 `squirrel report <audit-id>` 免重爬重新生成报告
- 问题→源码映射的迭代修复环: 报告中每条 finding 定位到具体文件后 Edit 批量修改; 优先级按 error 优先, 其次 rank (1-10) 高的 warning; 每批修复后跑构建做回归验证
- 分数闭环与人工兜底: 用 `squirrel report --diff <baseline-id>` 对比基线证明改善; 需要人拍板的问题 (如死链是删是换) 标记出来交用户决定而非擅自猜测; 最终签核前用 `-C full` (500 页) 全量爬取确认
