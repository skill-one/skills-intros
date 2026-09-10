# design-system (`nextlevelbuilder/ui-ux-pro-max-skill/design-system`)

## blackbox

**function**: 把你的品牌规范 (颜色、字体、间距) 整理成一套统一的设计变量, 并据此产出风格一致的前端样式文件和网页版演示幻灯片 (像 PPT, 用浏览器放映)。

- input: 一段品牌信息, 如「主色 #2563EB, 点缀色 #FF6B6B, 标题字体 Space Grotesk」, 或一份品牌手册文档, output: 一份可直接引入项目的样式变量文件 (CSS + JSON), 之后全站写 var(--color-primary) 就能统一配色, 换主题只改一处
- input: 一句话需求, 如「帮我做一份 10 页的投资人路演稿」, output: 一个在浏览器里打开即可翻页放映的 HTML 幻灯片文件, 含品牌配色、数据图表、动画和进度条, 可用键盘方向键翻页
- input: 你的前端代码目录路径, 如 src/, output: 一份「体检报告」, 逐条指出哪些页面写死了颜色和字号、各自应该替换成哪个设计变量
- input: 一个组件名, 如 button (按钮), output: 一张规格表, 列出该组件在默认 / 悬停 / 按下 / 禁用四种状态下各自的背景、文字、边框和阴影取值
