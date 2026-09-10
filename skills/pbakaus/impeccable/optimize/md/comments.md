# optimize (`pbakaus/impeccable/optimize`)

## comments

- user: 五年前端老鸟, category: 妙用, comment: 别一上来就说"帮我优化", 先把 Lighthouse 报告和卡顿场景贴给它. 它先找最大瓶颈再动手, 我以为是图片拖慢, 实际是段 JS 长任务.
- user: 第一次做官网的新手, category: 坑, comment: 我给全站图片都加了懒加载, 结果首屏大图反而更慢. 懒加载只该给屏幕外的图, 首屏大图必须直接加载.
- user: 接私活的独立开发者, category: 注意, comment: 在我电脑 Chrome 上测全是绿, 客户手机却还是卡. 一定模拟慢速 3G 加低端机再测一遍, 分数能差一半.
- user: 转岗半年的前端, category: 坑, comment: 照网上帖子给所有动画元素都加了 will-change, 内存暴涨反而更卡. 只给确认卡顿的那一两个元素加.
- user: 产品经理转前端, category: 启发, comment: 以前凭感觉优化, 改两天图片只快 0.3 秒. 先测数据、先修最大瓶颈, 一下午就见效. 优化排序比技巧更重要.
- user: 独立维护电商站的老哥, category: 注意, comment: 图片没占位, 加载时页面往下跳, 用户总点错下单按钮. 给图容器写 aspect-ratio 预留空间就稳了.
