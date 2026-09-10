# design-system (`nextlevelbuilder/ui-ux-pro-max-skill/design-system`)

## comments

- user: 前端老兵, category: 妙用, comment: 全站只引 semantic 层变量、别写死 hex，后来加暗色主题，我只改 semantic 一层定义就整体切换，validate 零报错。
- user: 第一次用的新手, category: 坑, comment: 在项目根直接跑 scripts/generate-tokens.cjs 报不存在，路径相对 skill 目录，要用基目录拼全路径，工作目录保持在项目根。
- user: 创业公司产品经理, category: 妙用, comment: 搜 CTA 页时加 --context --position 9 --prev-emotion frustration，它按情绪弧线推荐收尾版式，不用自己拍脑袋选布局。
- user: 独立开发者, category: 注意, comment: 先备好 docs/brand-guidelines.md 和 assets/design-tokens.json 再生成，我空跑了一次，出来全是默认色，返工才对齐品牌。
- user: 后端兼职画页面, category: 注意, comment: 图表别用 CSS 画柱状，必须 Chart.js——我省事 CSS 画的，slide-token-validator 直接打回，改完才过。
- user: 设计转开发, category: 启发, comment: 三层 token 让我看懂老项目 CSS 为什么越改越乱：同一个蓝散落十几处。现在先定语义层再写组件，改动只剩一处。
