# gsap-utils (`greensock/gsap-skills/gsap-utils`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我照别人的写法给 random 省略末参想拿函数,结果直接返回了随机数。它是全库唯一例外,末位要传 true 才是函数形式。
- user: 后端转前端, category: 注意, comment: 把 '50%' 直接喂给 mapRange 想换算,拿到 NaN。它只算数字不带单位,先 parseFloat,或用 getUnit 确认单位再处理。
- user: React 组件库维护者, category: 坑, comment: 同页两个组件都有 .box,动画互相误伤。改用 q = selector(ref) 生成局部选择器,只搜本组件内部,串场立刻消失。
- user: 交互动效爱好者, category: 妙用, comment: 发现 interpolate 能当 lerp 用:interpolate(当前值, 目标值, 0.1) 每帧逼近目标,鼠标跟随缓动几行写完,不用引库。
- user: 写 H5 交互的设计师, category: 妙用, comment: tween 里直接写 x:'random(-100,100,5)',每个盒子各自随机还按 5 取整,配 stagger 一排各飞各的,省掉手写循环。
- user: 前端老兵, category: 注意, comment: 做无限轮播才发现:wrap(0,360) 的 max 取不到,360 会绕回 0。写闭环逻辑时把边界想清楚,别卡在终点值上。
