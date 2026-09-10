# vercel-react-view-transitions (`vercel-labs/agent-skills/vercel-react-view-transitions`)

## blackbox

**function**: 给你的 React / Next.js 网站加上"原生 App 手感"的页面切换动画——不用装任何第三方动画库, 老浏览器上自动不播动画但功能照常。

- input: 一个 React 项目代码 + 一句需求: 「列表页点进详情页太生硬, 想要手机 App 那种前进/后退的滑动效果」, output: 改好的代码文件: 点列表卡片从右侧滑入详情页, 点返回从左侧滑回列表, 动画方向自动跟随导航方向
- input: 商品卡片组件和详情页组件的代码, output: 改好的代码: 点击缩略图时, 图片原地平滑放大"长成"详情页大图, 而不是两页各跳各的
- input: 一个带加载骨架屏的页面代码, output: 改好的代码: 数据加载完成时, 骨架屏平滑淡出、真实内容淡入, 不再瞬间闪变
- input: 一个带"排序"按钮的列表页代码, output: 改好的代码: 点击排序后, 每个列表项各自滑动到新位置, 而不是整页瞬间重排
- input: 「这个动画在我的 Safari 上不动」+ 出问题的代码, output: 说明原因 + 修好的代码, 并保证不支持的浏览器自动降级: 没有动画, 但页面功能完全正常
