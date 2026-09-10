# gsap (`heygen-com/hyperframes/gsap`)

## comments

- user: 第一次用的新手, category: 坑, comment: 键名和 data-composition-id 对不上时不报错, 画面直接静止。我空查半小时才发现多了个空格, 两边要一字不差, 直接复制 ID 最稳。
- user: 从网页动效转做视频的前端, category: 坑, comment: 照网页习惯写 repeat: -1 做循环背景, 定长视频里没法渲染。改成有限次: 每圈 2s、视频 10s 就 repeat: 4, 改完一次过。
- user: 写交互原型的全栈, category: 坑, comment: 在 fetch 回调里才建时间线, 渲染时元素全停在初始位置。必须同步创建并挂上 window.__timelines, 异步数据要先写死。
- user: 做开场动画的短视频作者, category: 妙用, comment: stagger 写 {amount: 0.3, from: 'center'}, 一排字自动从中间向两侧展开, 不用手排 delay; 配 back.out(1.7) 回弹, 开场质感立现。
- user: 动效工程师, category: 注意, comment: 同一属性被后面的 from() 接手时记得 immediateRender: false, 否则起始帧闪跳。网页上肉眼难察觉, 逐帧渲染会完整录进视频。
- user: 维护多客户项目的前端负责人, category: 启发, comment: 以前全靠 delay 串动画, 客户改节奏就要全部重算秒数。换 timeline + addLabel 后只挪标签位置, 把时间点声明出来比手算好维护太多。
