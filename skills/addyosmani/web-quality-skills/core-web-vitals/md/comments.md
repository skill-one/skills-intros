# core-web-vitals (`addyosmani/web-quality-skills/core-web-vitals`)

## comments

- user: 独立站长, category: 坑, comment: 改完看 PageSpeed 涨分就交差, 结果 CrUX 一个月没动——实验室分数即时变, 真实用户数据要等新访问慢慢攒。
- user: 接外包的前端, category: 注意, comment: 只给源码不给网址时, 它只能从代码推测可能原因, 不会下结论. 想拿到真实诊断, 先备一个能打开的链接。
- user: 电商站技术, category: 妙用, comment: 用预渲染后列表→详情页秒开. 记得把结账、退出登录页从规则里排除, 否则会被提前整页加载, 白烧用户流量。
- user: 被版面跳动折磨过的设计师, category: 启发, comment: 页面老跳, 我反复改会跳的那块内容, 没用; 查出是上方广告没预留高度把它挤下去. 跳的元素常是受害者, 不是元凶。
- user: 替前端背锅的后端, category: 注意, comment: 指标按第 75 百分位算——最差那 25% 访问超标, 整体就不及格. 别只优化快设备, 先查清慢的那批用户在用什么。
- user: Next.js 新手, category: 坑, comment: 给首图同时加 preload 和 img 以为双保险, 实测没变快. 后来懂了: preload 只在图片被浏览器发现太晚时才有用, 乱加反而抢带宽。
