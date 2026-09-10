# redesign-existing-projects (`leonxlnx/taste-skill/redesign-existing-projects`)

## comments

- user: 独立开发者, category: 妙用, comment: 只让它跑修复优先级前三步: 换字体、清配色、补悬停态, 一个下午落地页就像换了个产品. 没必要一口吞下整套改造, 前三步占大半效果.
- user: 前端组长, category: 妙用, comment: 我把它当 review 清单用: 不让它改码, 只扫同事的新页面, 一轮就揪出全篇 Inter、无 focus 态、死链 #. 不动手也白得一次设计审查.
- user: 第一次用的新手, category: 坑, comment: 开口就说"全面升级", 一次改了两千多行, 不敢合并只能回滚. 后来限定"这轮只动字体和间距", diff 三百行当天过审. 务必小步分轮.
- user: 后端转全栈, category: 注意, comment: 它不迁移框架, 我想把原生 CSS 换 Tailwind, 它只在原样式上改, 这是规矩. 改完还要验证功能, 项目得能本地跑, 先把启动命令给它.
- user: 接外包的设计师, category: 注意, comment: 没真实图片时它会用 picsum 占位图, 交付客户前先把品牌素材给它, 不然首页挂随机照片. 品牌色和字体也要提前声明, 免得被换掉.
- user: SaaS 资深前端, category: 启发, comment: 审计把紫渐变、三栏卡片、Lucide 图标列为 AI 指纹, 对照自家官网三条全中. 现在写新页面前先用这份清单自查, 源头避免比返修省事.
