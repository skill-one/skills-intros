# baoyu-markdown-to-html (`jimliu/baoyu-skills/baoyu-markdown-to-html`)

## whitebox

- 读入 Markdown, 检测是否含中文 (CJK); 若有且 baoyu-format-markdown 技能可用, 先询问是否用它修复格式 (加粗标记/CJK 间距等)
- 确定主题: 用户显式指定 → 本技能 EXTEND.md 的 default_theme → baoyu-post-to-wechat 的 EXTEND.md (跨技能回退) → 都没有才询问用户
- 确定引用模式: 默认关闭, 仅当用户明确要求 (「微信外链转底部引用」或 --cite) 才开启
- 执行转换: bun (无则 npx -y bun) 运行 scripts/main.ts <markdown_file> --theme <theme> [--cite], 生成带内联 CSS 的 HTML
- 读取 stdout 的 JSON 结果, 汇报输出 HTML 路径; 若旧 HTML 存在则提及时间戳备份

- 转换核心是单个 TypeScript 入口 scripts/main.ts: 解析 Markdown 与 YAML frontmatter (title/author/description, 缺失时回退首个 H1/H2 或文件名), 输出内联 CSS 的 HTML, 与源文件同目录同名 (.md → .html); 已存在则先备份为 .html.bak-YYYYMMDDHHMMSS。运行依赖 bun 或 npx。
- Mermaid 渲染: ```mermaid 代码块经 headless Chrome (CDP 协议, 需系统装有 Chrome/Chromium/Edge) 渲染为本地 PNG, 缓存于 imgs/.mermaid-cache/mermaid-<hash>.png; 缓存键含代码+主题+缩放+宽度+背景+mermaid 版本; Chrome 不可用时降级为 <pre class="mermaid"> 原文, 转换仍算成功。
- 主题即内联 CSS (default/grace/simple/modern 四套, 可叠 --color 等参数); --cite 开启时普通外链改为编号上标并汇总为文末「引用链接」节, mp.weixin.qq.com 链接保持原位, 链接文本等于 URL 的裸链接也保持内联。
