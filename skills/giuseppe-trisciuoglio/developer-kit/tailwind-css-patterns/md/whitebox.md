# tailwind-css-patterns (`giuseppe-trisciuoglio/developer-kit/tailwind-css-patterns`)

## whitebox

- 定位任务: 用 Read/Glob/Grep 读取待美化的 React/Vue/Svelte 组件与现有样式文件
- 移动优先编写: 先写手机端基础工具类, 再按需叠加 sm:/md:/lg: 等响应式前缀
- 组合工具类: 用 Tailwind 内置的间距/颜色/排版刻度拼出布局、卡片、表单等样式, 暗色模式用 dark: 前缀
- 收敛与配置: 重复的类组合抽取成可复用组件, 主题定制写入 @theme (v4 CSS-first) 或 tailwind.config.js
- 验证提交: 用 Edit/Write 写回文件, Bash 跑 npm run build, 并在 DevTools 各断点检查视觉回归与可访问性

- 工具类组合 (utility-first): 样式不写在单独 CSS 文件, 而是直接在标签上组合 utility class; 响应式前缀必须放在非响应式类之前 (如 md:flex 而非 flex md:flex), 顺序错了断点样式不生效
- 设计令牌系统: 统一使用 Tailwind 的 spacing/color/typography 刻度保证一致性; v4.1+ 用 @theme 做 CSS-first 主题配置, 少用 @apply 和任意值
- 构建期 purge (按需裁剪): 依赖 Tailwind CSS v4.1+ 本身, 通过配置 content 路径扫描所有模板文件, 生产构建时自动剔除未使用的类; 路径配错会导致样式在产线全部丢失; 构建命令走 Bash (npm run build / npx tailwindcss --watch)
