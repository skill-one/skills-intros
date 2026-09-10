# vue-debug-guides (`vuejs-ai/skills/vue-debug-guides`)

## whitebox

- 接收一个 Vue 3 问题: 运行时错误、警告、异步失败或 SSR/水合(hydration)异常的描述。
- 在 skill.md 的症状索引中按分类 (响应式、侦听器、模板、Props、SSR 等约 27 类) 匹配症状描述。
- 定位索引条目指向的具体参考文档 (reference/xxx.md) 并读取。
- 依据该参考文档输出问题的成因诊断与修复方案。
- 若问题是开发规范/常见坑类而非调试类, 按索引指引转介给 `vue-best-practices` 技能。

- 症状→文档路由: skill.md 本身不含解法, 只是一张按主题分类的「症状 → 参考文档」对照表, 靠症状关键词命中对应条目。
- 分层加载: 每条索引指向 reference/ 目录下的独立 markdown 文档, 诊断与修复知识全部在文档内, 按需读取单条而非全量载入。
- 依赖极简: 不依赖任何外部工具、库或模型 API, 知识来源仅为本 skill 自带的 reference 文档; 唯一外部关联是同级技能 `vue-best-practices` (负责开发规范, 本 skill 只管调试)。
