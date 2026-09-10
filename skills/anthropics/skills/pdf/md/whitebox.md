# pdf (`anthropics/skills/pdf`)

## whitebox

- 接到任务后，先按 SKILL.md 的任务清单归类：提取文本/表格、合并、拆分、旋转、加水印、生成 PDF、填表单、OCR
- 查 Quick Reference 的「任务→最佳工具」映射表，直接套用文档中现成的代码模板或 CLI 命令，无需从零设计
- 执行：Python 路线（pypdf / pdfplumber / reportlab）跑脚本，或命令行路线（qpdf / pdftk / pdftotext）跑命令
- 两个约定分支：填 PDF 表单必须先读 FORMS.md；高级特性（pypdfium2、pdf-lib 等）查 REFERENCE.md
- 产出结果：写出新 PDF 文件，或把提取出的文本/表格返回（表格可经 pandas 导出 Excel）

- 解析双库分工：pypdf 在文档结构层操作（页面增删/旋转/元数据/加密），pdfplumber 在内容层提取文本和表格；扫描件无文本层，走 OCR 链路：pdf2image 先逐页转图片，pytesseract 再识别。外部依赖：pypdf、pdfplumber、pandas、pytesseract、pdf2image
- 生成用 reportlab 双模式：Canvas 直接画（精确坐标），Platypus 用 Paragraph 堆排版流（自动分页）。硬约束：上下标必须用 <sub>/<super> 标签——内置字体缺 Unicode 上下标字形（₀²），直接写会渲染成黑块
- 命令行备选路径：qpdf（合并/拆分/旋转/解密）、pdftk（备用）、poppler-utils 的 pdftotext/pdfimages（提取文本/图片），纯 shell 完成，不依赖 Python
