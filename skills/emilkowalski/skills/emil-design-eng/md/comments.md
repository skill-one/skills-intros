# emil-design-eng (`emilkowalski/skills/emil-design-eng`)

## comments

- user: 前端新手, category: 坑, comment: 我把下拉菜单动画写成 ease-in,又慢又肉。换成 ease-out 同样 300ms,体感立刻变了——进场动画千万别用 ease-in。
- user: 独立开发者, category: 妙用, comment: 给所有按钮 :active 加了 scale(0.97),同事第二天就说"这应用手感变好了"。成本最低的打磨,一行 CSS 的事。
- user: React 老手, category: 坑, comment: 列表页用 Framer Motion 的 x/y 简写,页面加载时疯狂掉帧。换成完整 transform 字符串就顺了,主线程一忙差异就出来了。
- user: 设计师转码, category: 启发, comment: 以前动效全靠感觉加,现在先问"用户一天见几次":天天用的直接不加动画,反而显得快。频率决定要不要动。
- user: 全栈工程师, category: 注意, comment: 弹窗是例外:popover 从触发点展开,modal 保持居中。我统一设了 transform-origin,结果所有弹窗都从角落长出来,很怪。
- user: SaaS 产品前端, category: 妙用, comment: 用 clip-path 的 inset 做标签页高亮切换:复制一份 tab 列表再裁剪,颜色过渡完全无缝,逐个调 transition 根本比不了。
