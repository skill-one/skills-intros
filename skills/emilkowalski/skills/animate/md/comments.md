# animate (`emilkowalski/skills/animate`)

## comments

- user: 刚接手前端的后端老兵, category: 坑, comment: 让给 ⌘K 命令面板加开合动画, 被它直接拒绝。我不服, 自己手写了一版, 天天开关几十次很快嫌烦。高频操作听它的: 不动画才是对的, 它还给了瞬时切换的替代方案。
- user: React Native 移动端开发, category: 注意, comment: 它不覆盖 RN/Expo, 我拿它写 App 转场, 被指去用 animate-expo。想审查整个项目已有动效也另有 improve-animations, 它只管从零新建一个。先对准场景再进来。
- user: 接外包的独立开发者, category: 妙用, comment: 开局直接报组件名最省事: 'toast 进出场动画', 它从现成配方起步而不是空白文件。组件本体它不手搓, 会推我用现成组件库, 连下拉菜单的键盘焦点都替我省了。
- user: 前端架构师, category: 启发, comment: 它让我先问'这东西一天被触发几次'再谈缓动曲线。现在我评审动效代码第一句都看频率——命令面板这类一天上百次的不该有动画, 这个顺序比任何参数都值钱。
- user: 关注无障碍的前端, category: 注意, comment: 减少动态 (reduced-motion) 和触屏 hover 误触发的处理默认随代码一起给, 不用催。但它的标准是'变轻不归零', 会保留淡入; 若验收要求完全静止, 要一开始就明说。
- user: UI 设计负责人, category: 妙用, comment: 它给结论附一行理由, 我直接贴进设计评审: '高频操作别动''UI 动画不超 300ms', 比吵半小时管用。它从不开选项菜单, 替我拍板, 省了来回拉扯。
