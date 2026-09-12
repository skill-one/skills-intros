# unocss (`antfu/skills/unocss`)

## blackbox

**function**: 帮你在前端项目里快速搞定样式: 从零配置原子化 CSS (一种把样式拆成小积木、直接写在 class 里的写法, Tailwind 就是这种风格), 到把你要的界面用一行行样式类写出来。

- input: 一个 Vite 或 Nuxt 前端项目, 说一句「帮我接上原子化 CSS」, output: 一份配好的 uno.config.ts 配置文件, 存进去后项目里就能直接写 class="flex p-4" 这类样式, 存盘即生效
- input: 一句界面需求, 如「做一个居中的登录卡片: 圆角、阴影、按钮悬停变色」, output: 可直接粘贴进页面的 HTML/JSX/Vue 代码, 所有样式都写好了, 浏览器里就是你要的样子
- input: 一段 class 又长又乱的现有代码, 如「hover:bg-blue-500 hover:text-white …」重复一大串, output: 精简改写后的同款代码, 效果不变但 class 更短更好读
- input: 「我要在页面里放图标, 但不想引一整套图标库」, output: 纯 class 用法的图标代码, 如 <div class="i-logos-vue" />, 无需额外图片文件
