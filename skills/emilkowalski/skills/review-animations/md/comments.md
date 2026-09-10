# review-animations (`emilkowalski/skills/review-animations`)

## comments

- user: 前端 Tech Lead, category: 妙用, comment: 我把它的红线清单当提 PR 前自查表: 只贴 diff 里的动效代码, 拿到的表格能直接粘成评审意见, Block/Approve 正好当合入门禁。
- user: React 新手, category: 坑, comment: 我用 scale(0)+transition:all 写下拉菜单被连标三处硬伤, 别不服气, 照抄 After 列就能修; 但它只管动效, 混着问逻辑问题会被拒。
- user: 赶工上线的独立开发者, category: 注意, comment: 它默认挑刺, 我自认不错的 500ms 淡入也被拦。想要慢动效得先给理由, 「好看」不算理由, 高频元素更别指望加动画。
- user: 关注无障碍的前端, category: 妙用, comment: 它纠正我两个误区: reduced-motion 不是全删, 留 opacity 去位移; 触屏也会触发 hover, 得用 @media (hover:hover) 拦住。
- user: 后端老兵, category: 启发, comment: 「每个动画都得答为什么动」这句话影响了我的习惯, 现在删掉的比加的多; 键盘触发的一律不加, 高频操作直接砍成无感。
- user: UI 设计师, category: 注意, comment: 它审不了设计稿, 文字描述动效也没用, 必须贴真实 CSS/JSX。设计标注和代码不一致时, 它抓的是代码那一头。
