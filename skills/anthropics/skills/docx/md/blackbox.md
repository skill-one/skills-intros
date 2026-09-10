# docx (`anthropics/skills/docx`)

## blackbox

**function**: 帮你直接生成、修改或提取 Word (.docx) 文档——你给文字和要求, 我还你一份能打开就用的 Word 文件。

- input: 一段会议纪要文字 + 要求: 做成带标题层级、目录、页码的正式文档, output: 排版完成的 .docx 文件, 可直接在 Word/WPS 里打开并继续编辑
- input: 一份合同 .docx + 指令: 「把所有'甲方'改成 'XX公司', 改动用修订模式标出来」, output: 带修订痕迹 (改了哪、改成什么一目了然, 对方可逐条接受或拒绝) 的新 .docx
- input: 一份几十页的 .docx 报告, 说一句「把内容给我」, output: 提取出的全部文字内容, 可按章节结构整理好交还
