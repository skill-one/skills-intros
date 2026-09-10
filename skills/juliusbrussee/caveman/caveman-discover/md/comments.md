# caveman-discover (`juliusbrussee/caveman/caveman-discover`)

## comments

- user: 后端老兵, category: 妙用, comment: 顺着入口点盘点, 翻出一个没人记得的凌晨摘要定时任务, 一直在烧 token. 标完账单按任务拆行, 当月就找到成本大头.
- user: 第一次用的新手, category: 坑, comment: slug 写成 SupportReply, 网关回 400 cave_invalid_request_header. 只收小写字母数字和 _-, 改成 support-reply 就过了.
- user: 运维老哥, category: 注意, comment: 定时任务标完别急着刷面板: 排程要等下次真正触发才出现在 workflows 页. 我当晚以为没生效, 第二天凌晨 digest 才冒出来.
- user: 独立开发者, category: 注意, comment: 它只标走 Caveman 网关的调用, 没接网关的会列进报告 not wired 一栏, 接线是另一个 setup 技能的活. 先看那栏, 别以为标完就全覆盖.
- user: AI 平台工程负责人, category: 启发, comment: 改名会切断花费历史, 所以它先提案后动手很关键: 表格我先过一遍, purpose 不明的标 review 不瞎编. 比我以前拍脑袋命名稳得多.
- user: 开源仓库维护者, category: 妙用, comment: 我们三个任务共用一个 llm.ts, 它把标签打在各自调用方而不是 helper 里, 花费才分得开. 我自己标肯定一把全塞 helper, 全混一桶.
