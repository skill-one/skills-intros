# improve (`shadcn/improve/improve`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我张口就说「帮我把这个 bug 修了」,结果它只给一份计划文档,差点以为没用。后来才懂它绝不改业务代码,该说 execute 计划名,让别的模型照计划去执行。
- user: 全栈独立开发者, category: 妙用, comment: 已经知道要改什么时,用 `plan 我要XXX` 跳过整个审计,它查完直接产出连代码摘录都内联好的计划,丢给便宜模型一次跑通——贵模型出图,便宜模型施工。
- user: 后端老兵, category: 妙用, comment: 合并前对分支跑 branch 审计最好用:只查改动文件及其直接调用方,问题分成「本分支引入 / 历史遗留」两类,不会拿祖传债来恶心你的 PR。
- user: 接手遗留项目的工程师, category: 妙用, comment: 我把 plans/README.md 当技术债看板:过阵子代码变了就跑 reconcile,做完的标 DONE、漂移的刷新,被否掉的建议进 rejected 区,下次审计不会重复翻出来。
- user: 管着公网服务器的运维, category: 注意, comment: --issues 会把计划发成 GitHub issue,公开仓库等于漏洞细节全网可见,给攻击者递地图。安全问题我一律不发布,走私有渠道。
- user: 开源项目维护者, category: 注意, comment: 它报出密钥泄露时只给文件行号和类型,绝不复述密钥值。别以为它漏了,是故意的——你要做的是立刻去轮换那个 key。
