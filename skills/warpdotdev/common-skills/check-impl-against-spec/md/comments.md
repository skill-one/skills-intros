# check-impl-against-spec (`warpdotdev/common-skills/check-impl-against-spec`)

## comments

- user: 后端老兵, category: 妙用, comment: 最值的是抓计划外改动:spec 只让改登录模块,PR 却顺手重构了整个目录,人眼容易漏,它直接标为重要问题。
- user: 第一次当 reviewer 的新手, category: 坑, comment: 我以为是自动发到 GitHub 的,守着 PR 等半天——其实只写进 review.json,得自己手动贴上去,差点漏发。
- user: 技术负责人, category: 注意, comment: spec_context.md 写得越具体它越准。我没写迁移步骤,它就不会查这块——没写的它不猜,别指望它读心。
- user: 十年评审老手, category: 妙用, comment: 实现和 spec 对得上时它一句不夸,review.json 里全是真问题。这种「沉默即合格」的评审噪音最少。
- user: 开源项目维护者, category: 注意, comment: 命名、文件组织这类小差异它故意不报,只认实质性偏差。想统一代码风格别靠它,那是 lint 的活。
- user: 兼职评审的产品经理, category: 启发, comment: 它逼我把验收标准和必做的验证步骤提前写进 spec——没写进文档的要求,实现漏了也查无依据。
