# review-pr (`warpdotdev/common-skills/review-pr`)

## comments

- user: 后端老兵, category: 妙用, comment: 把 spec_context.md 一起放进目录,它会逐条对照需求文档找实现偏差,还当正式 concern 写进结果,比肉眼对 diff 靠谱。
- user: 第一次接自动 review 的新手, category: 坑, comment: 以为它会像机器人一样直接评论到 GitHub,结果跑完只生成 review.json,没发任何东西。发布要自己来,别原地等它发言。
- user: 开源维护者, category: 注意, comment: 必须喂带 [NEW:n] 行标注的 pr_diff.txt。我直接贴了裸 git diff,它定位不了行号,意见全堆进正文,没法钉在代码行上。
- user: 平台工程师, category: 妙用, comment: verdict 只有 APPROVE/REJECT 两个值,直接拿它当流水线合并门禁。发布前先跑自带校验脚本,它报错会自己修,脏数据进不了库。
- user: 带五人小组的 tech lead, category: 启发, comment: 它每条建议必须能精确替换到某几行,连缩进都得对齐。反观我平时「这里可以重构」式 review,连行号说不清,对作者等于噪音。
- user: 独立开发者, category: 注意, comment: 它从不直接动 GitHub,正好让我发布前人工筛一遍、压掉小毛病。V0 初版它只把重试超时当未来建议,不会拿这些卡你合并。
