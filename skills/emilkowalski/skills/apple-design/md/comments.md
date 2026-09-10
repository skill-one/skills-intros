# apple-design (`emilkowalski/skills/apple-design`)

## comments

- user: 维护公司组件库五年的前端, category: 坑, comment: 抽屉手势原先用 CSS transition 收尾,动画一半被抓就瞬移。换成 spring 且从元素实时位置起步,中途可抓可反向,今年最值的一次重构。
- user: 第一次写拖拽手势的新手, category: 坑, comment: 我曾给所有动画加 bounce,以为弹跳=高级。其实只有甩动释放才配弹,菜单淡入也弹很廉价。现在默认无弹,手势带惯性才给一点。
- user: 独立开发者,全栈一人包, category: 妙用, comment: 把指南里的动量投影公式抄进我的轮播:用释放速度算出「会滑到哪」再吸附最近档位,松手像真被扔出去,比就近吸附高一档,十行代码。
- user: 设计转代码的工程师, category: 妙用, comment: 把菜单 transform-origin 锚到触发按钮、从原点长出,再配毛玻璃和亮顶边,同事以为买了 iOS 组件库。就两行 CSS,来源一目了然。
- user: 负责无障碍验收的前端, category: 注意, comment: 别只写 prefers-reduced-motion。补上 reduced-transparency(玻璃转实底)和 prefers-contrast(实底加描边)才过验收,低视力用户读不清半透明卡片。
- user: 交互设计老油条, category: 启发, comment: 以前把动画当播完即弃的脚本,现在每个动效先问:用户中途伸手抓它会怎样?答不上来就重做。这个提问习惯比任何参数都值钱。
