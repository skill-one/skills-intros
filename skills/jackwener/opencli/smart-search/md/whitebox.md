# smart-search (`jackwener/opencli/smart-search`)

## whitebox

- 预检定位: 运行 `opencli list -f yaml`, 用 live registry 确认候选站点存在及其 strategy/browser/domain
- 路由决策: 按唯一主规则选源 — 用户指定了网站就直接用; 没指定则按语言/语境从 grok/doubao/gemini 三选一只用一个 AI 源
- 读取实时帮助: 依次执行 `opencli <site> -h` 与 `opencli <site> <command> -h`, 以实际输出确定子命令/参数/输出列, 不硬编码任何签名
- 执行搜索: 真正调用 `opencli <site> ...`, 立刻更新调用台账 (site/query/count/status), 并遵守频率上限
- 补充与汇报: AI 摘要不足时补 1-2 个专用源; 回答末尾强制追加『搜索摘要』(站点/查询词/次数/被跳过站点)

- 实时帮助防文档漂移: 所有命令参数、输出列、策略都以 `opencli ... -h` 现场输出为准, 绝不在文档里硬编码; 唯一外部依赖是 `opencli` CLI (封装各站点与 AI 模型 grok/doubao/gemini 的统一命令行入口)
- 单题预算台账: 预检与 -h 帮助不计次, 每次真实搜索调用计 1 次 (失败/超时/验证码也算), 硬限制为 AI 源每题 1 次、非 AI 源最多 2 次 (第 2 次需明确理由, 无第 3 次), 超限则记录『已跳过』并回退同类站点
- 查询词构造与止损: AI 源查询词 = 主题 + 目标 + 限定条件 (语言/地区/时间/平台), 拒绝裸关键词; 某 AI 源一旦执行过就不改写关键词追打, 信息缺口交由专用源补足而非反复调用
