# ckm:brand (`nextlevelbuilder/ui-ux-pro-max-skill/ckm:brand`)

## comments

- user: AI 内容运营, category: 妙用, comment: 我把 inject-brand-context.cjs --json 的输出直接贴给 AI 当写作前提, 出来的语气和品牌口径基本一致, 不用每次重新解释调性。
- user: 前端工程师, category: 坑, comment: 手改 design-tokens.css 想临时调色, 下次跑 sync 全被覆盖. 色值必须去 docs/brand-guidelines.md 改源头, 再跑 sync-brand-to-tokens.cjs。
- user: 第一次用的新手, category: 坑, comment: 新建品牌直接跑 sync 报找不到文件. 先拿 templates/brand-guidelines-starter.md 填好放到 docs/ 下, 再按顺序跑脚本就通了。
- user: 市场部对接外包的, category: 妙用, comment: 外包交图我先跑 extract-colors.cjs 对比品牌色板, 哪张色偏一目了然, 退回重做有数据撑腰, 不用肉眼来回吵。
- user: 后端老兵, category: 注意, comment: validate-asset.cjs 后面必须跟资源路径, 空跑没意义. 我固定收到设计资源就先验一遍命名和尺寸, 免得传上去再返工重传。
- user: 独立品牌设计师, category: 启发, comment: 把「logo 最小留白」「色值容差」这些我口头反复讲的规则写进 brand-guidelines.md 后, 团队能自查, 同类问题不再来找我拍板。
