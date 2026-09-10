# gsap-performance (`greensock/gsap-skills/gsap-performance`)

## comments

- user: 转行前端的新手, category: 坑, comment: 卡片入场我用 left/top 写，手机上明显掉帧。改成 x/y 就顺了——定位和宽高属性每次都触发重排，transform 只走合成层。
- user: 大屏可视化前端, category: 坑, comment: 图省事给整页几百个元素都加了 will-change，内存暴涨反而更卡。只给真正在动的十几个加，立刻恢复正常。
- user: 官网动效开发者, category: 妙用, comment: 鼠标跟随原来每次 mousemove 新建 tween，动两下就卡。换 quickTo 复用同一个补间，x/y 各一行，丝滑不掉帧。
- user: 独立开发者, category: 妙用, comment: 几十项列表进场，原来手动给每项排 delay，生成一堆 tween。改成一个 stagger 参数，代码短一半，开销也小。
- user: SPA 维护老哥, category: 注意, comment: 切路由前记得 kill 旧页面的 tween 和 ScrollTrigger，不然它们一直在后台跑，逛几轮页面就越来越卡，我吃过这亏。
- user: 移动端 H5 开发, category: 注意, comment: 低端安卓实测：scrub 设成 1 滚动跟手很多；refresh() 只在内容加载完调一次，别绑在 resize 上每次都刷。
