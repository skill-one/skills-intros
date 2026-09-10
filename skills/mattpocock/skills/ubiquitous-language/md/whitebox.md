# ubiquitous-language (`mattpocock/skills/ubiquitous-language`)

## whitebox

- 扫描当前对话全文，提取领域相关的名词、动词和概念
- 识别术语问题：同词异义（歧义）、异词同义（同义词）、模糊或过载的词
- 给出带有倾向性的规范术语表（每个概念只留一个最佳词，其余列为禁用别名）
- 将术语表写入工作目录下的 UBIQUITOUS_LANGUAGE.md，使用固定模板（分组表格 + 关系 + 示例对话 + 歧义标记）
- 在对话中内联输出一份摘要

- 模板化输出：严格按预设结构生成 —— 按领域自然分组的多张 markdown 表格（Term / Definition / Aliases to avoid）、Relationships（含基数关系）、Dev 与领域专家的示例对话（3~5 轮）、Flagged ambiguities
- 术语策展规则：定义一句话内、只说「是什么」不说「做什么」；过滤非领域词（类名、数组/函数等通用编程概念不收录）；多词同义时果断定夺并封禁别名
- 可重入（re-run）机制：再次触发时先读已有 UBIQUITOUS_LANGUAGE.md，合并新术语、演进旧定义、重新标记新歧义、重写示例对话
- 无外部依赖：不调用任何外部工具、库或模型 API，仅读写本地文件；且 disable-model-invocation: true，只能由用户显式触发
