# fixing-metadata (`ibelick/ui-skills/fixing-metadata`)

## comments

- user: 独立开发者, category: 坑, comment: 我把 og:image 写成相对路径, 链接发到群里卡片一直没图。改成 https 开头的完整地址立刻正常, 别偷懒写 /images/xx.png。
- user: 前端新手, category: 注意, comment: 别在 localhost 就让它验证分享卡片, 社交平台抓不到本地地址。先部署到线上或临时域名, 再逐项核对才作数。
- user: SEO 顾问, category: 妙用, comment: 我用它扫老站, 它按优先级先揪出两页 canonical 重复和 noindex 缺失, 再补标题描述。先修致命项再锦上添花, 顺序很对。
- user: 后端老兵, category: 注意, comment: 它只改 head 里的元信息, 不会重构你的代码或迁移框架。Next.js 项目它顺着现有 metadata API 写, 不会强推自己那套。
- user: 营销运营, category: 坑, comment: 我想让搜索结果带五星评分, 它直接拒绝了——评分必须页面上真实可见, 不能凭空编 JSON-LD, 假结构化数据会被惩罚。
- user: 内容站站长, category: 启发, comment: 我以前爱往标题堆关键词, 现在改成每页 title、description、canonical、og:url 四处一致, 长尾词排名反而稳了。
