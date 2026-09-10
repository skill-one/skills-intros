# gsap-core (`greensock/gsap-skills/gsap-core`)

## comments

- user: 第一次用的新手, category: 坑, comment: 照 CSS 习惯把 duration 写成 500,以为是毫秒,结果元素飘了近十分钟才停。这库单位是秒,写 0.5 才是半秒。
- user: React 中后台开发者, category: 坑, comment: 同一元素同一属性叠两个 from(),第二个没加 immediateRender:false,起始值被它抢改,前面那个动画看着像失效。
- user: 电商站交互前端, category: 注意, comment: 上手前没人告诉我 overwrite 默认 false:快速来回 hover 时新旧动画同时抢,元素发抖。加 overwrite:'auto' 只结束冲突属性就顺了。
- user: 从 CSS 动画转来的前端, category: 妙用, comment: 淡出别用 opacity,换 autoAlpha:为 0 时自动补 visibility:hidden,透明层不再挡住下层按钮的点击。
- user: 独立做作品集站的全栈, category: 妙用, comment: 列表入场一行 stagger:{each:0.08, from:'center'},就有从中间向两边散开的效果,不用手算每个元素的 delay。
- user: 关注无障碍的设计师, category: 启发, comment: 以前只在桌面端调动画,直到想到大幅运动会转晕前庭障碍用户。matchMedia 里判一下 prefers-reduced-motion,命中就 duration:0 跳过。
