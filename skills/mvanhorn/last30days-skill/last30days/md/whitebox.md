# last30days (`mvanhorn/last30days-skill/last30days`)

## whitebox

- 自检安装路径 (Step 0): 确认 SKILL.md 不是来自过期 clone, 锁定本次运行的 SKILL_DIR
- 调用 Python 引擎: 以 SKILL_DIR 为基目录运行 scripts/last30days.py "{topic}", 带预检 flags (--emit=compact 等), 从 env 读 API keys
- 引擎抓取多源: 拉取 Reddit / X / YouTube / TikTok / HN / Polymarket / GitHub / web 近 30 天的帖子与互动数据
- 引擎评分聚类: 输出 Ranked Evidence Clusters + emoji-tree footer 的 compact stdout
- 模型合成: 按 LAWs 把证据块转写成 'What I learned:' 散文, badge 置于首行, footer 逐字透传

- Python 引擎 (scripts/last30days.py, 依赖 python3/node): 负责抓取、评分、聚类; 数据源靠可选 env API keys, 主用 SCRAPECREATORS_API_KEY, 另有 X_BEARER_TOKEN, APIFY, BRAVE, PERPLEXITY 等
- 输出契约锚点 (防即兴发挥): 强制 badge 首行 + 11 条 LAW - 禁自拟标题/章节头/em-dash, 禁尾部 Sources 块, 证据块只读不输出, footer 必须原样透传
- 路径与健康检查: 引擎路径直接取 '刚 Read 的 SKILL.md 所在目录' 防止走旧副本; doctor 预检配置, source_status / doctor --postmortem 区分'该源没数据'和'该源坏了'
