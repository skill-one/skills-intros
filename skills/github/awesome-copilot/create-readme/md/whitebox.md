# create-readme (`github/awesome-copilot/create-readme`)

## whitebox

- 通读整个项目和工作区, 弄清项目是什么、怎么用
- 对照 4 个指定的优秀 README 范例, 确定结构、语气与内容风格
- 撰写 README.md: 完整、结构清晰、格式规范, 若找到项目 logo 则放在页眉
- 自查硬性约束: 不写 LICENSE/CONTRIBUTING/CHANGELOG 章节, emoji 克制
- 交付最终 README.md

- 范例驱动写作: 结构/语气/内容以 4 个 GitHub 开源项目 README 为蓝本 (serverless-chat-langchainjs、serverless-recipes-javascript、run-on-output、smoke), 从 raw.githubusercontent.com 拉取
- 格式规范: 强制使用 GFM (GitHub 风味 Markdown) 及 GitHub admonition 提示块语法 (> [!NOTE] 等)
- 内容过滤规则: LICENSE、CONTRIBUTING、CHANGELOG 等章节一律不写入 (由专属文件承担), 篇幅精简、emoji 不滥用
