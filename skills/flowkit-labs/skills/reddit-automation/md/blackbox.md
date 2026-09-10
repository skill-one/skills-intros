# reddit-automation (`flowkit-labs/skills/reddit-automation`)

## blackbox

**function**: 帮你在 Reddit 上找到真正需要你产品的帖子,并起草诚实、可直接发布的回复草稿(由你人工审核后粘贴发布)。

- input: 一句话产品介绍 + 你的目标客户是谁 + 5~15 个目标 subreddit 名称, output: 一份精选清单:3 条最值得回复的 Reddit 帖子,每条附一句「为什么你能帮上这个人」的判断
- input: 一条 Reddit 帖子链接(比如有人在问「有没有 XX 这类工具的替代品?」), output: 一段 25~55 词、像同行分享真实经验的英文回复草稿;若顺带提到你的产品,会在同一句里如实标注利益关系
- input: 几条你收集到的 Reddit 帖子链接, output: 逐条给出「值得回 / 不值得回」的判断,并只为值得回的帖子附上回复草稿
