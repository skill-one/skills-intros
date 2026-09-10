# anysearch (`anysearch-ai/anysearch-skill/anysearch`)

## comments

- user: 行业研究员, category: 妙用, comment: 查电力价格这类行业题,我先让 AI 跑 get_sub_domains 看有没有对口子领域,走垂直搜索拿到的结果直接对口,不再是一堆 SEO 水文。
- user: 第一次用的新手, category: 坑, comment: 把年报 PDF 链接丢给 extract,直接报不支持——PDF、Word、图片都读不了。后来先搜出 HTML 版公告页再提取,一次就成。
- user: 运维老哥, category: 坑, comment: 在精简服务器上用 sh 跑 .sh 版 CLI 直接语法报错,必须 bash,还得装 jq 和 curl。发现机器有 python3 就换 py 版,只差 pip 装个 requests。
- user: 炒股散户, category: 坑, comment: 查股票漏传必填参数,后端直接校验报错。照 get_sub_domains 返回把 required 全带上,没值的留空(cn_code=),一次就通。
- user: 律所助理, category: 注意, comment: 搜索词会原样发到 AnySearch 服务器。我有次把客户项目代号写进查询,后怕,现在公开信息用通用词搜,涉密细节不进搜索框。
- user: 自媒体写手, category: 妙用, comment: 写稿前把 3 个不同角度的关键词一次 batch_search,每条限 3 条结果,一轮拿齐素材;拿不准算不算专业题,就 1 条通用+多条垂直混着搜。
