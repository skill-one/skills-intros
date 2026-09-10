# ponytail-review (`dietrichgebert/ponytail/ponytail-review`)

## comments

- user: 后端老兵, category: 妙用, comment: 妙在替换方案直接给全名：moment.js 换 Intl.DateTimeFormat，照抄即删，不用查文档。一下午清掉老项目三百行。
- user: 第一次用的新手, category: 坑, comment: 我拿它找崩溃 bug，结果回我 'Lean already. Ship.'。它只管删冗余，正确性、安全、性能一概不管。抓 bug 请开普通 review。
- user: 独立接活的自由开发者, category: 注意, comment: 只列清单不动手改。先看结尾 net 行数：小于 20 行我当场改，大工程攒周末。改完文件行号会漂移，要重新定位。
- user: 技术负责人, category: 启发, comment: yagni 标签改了团队规矩：以前手痒就写 AbstractX 单实现，现在 inline 到第二个调用者出现。评审直接甩标签，少吵一半。
- user: 前端工程师, category: 妙用, comment: 提 PR 前先自查：stdlib / native 类先改掉，人类 reviewer 就只聊业务逻辑。评审从两小时缩到四十分钟，真事。
- user: 测试工程师, category: 注意, comment: 别指望它帮你砍测试：单个冒烟测试和 assert 是它认的底线，永不标记。测试瘦身得走别的路。
