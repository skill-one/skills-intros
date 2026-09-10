# baoyu-markdown-to-html (`jimliu/baoyu-skills/baoyu-markdown-to-html`)

## blackbox

**function**: 把你的 Markdown 文章一键变成排版精美、可直接粘贴到微信公众号等平台的 HTML 文件。

- input: 一篇 Markdown 文章（article.md），并指定喜欢的风格，如「用 grace 主题」, output: 一个排版好的 HTML 文件：标题居中、代码高亮、表格和引用样式统一，复制后直接粘贴进公众号编辑器即可发布
- input: 一篇带外部链接的 Markdown 文章 + 一句「微信外链转底部引用」, output: HTML 文件：正文里的外部链接变成数字角标（如¹），所有链接集中列在文末「引用链接」处，符合公众号不允许外链的限制
- input: 含有 Mermaid 流程图代码块的 Markdown 文件, output: HTML 文件：流程图已自动生成图片嵌入文中，不依赖外部服务，离线也能正常显示
