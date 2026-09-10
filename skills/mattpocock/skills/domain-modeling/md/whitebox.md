# domain-modeling (`mattpocock/skills/domain-modeling`)

## whitebox

- 读取仓库术语基线: 根目录 CONTEXT.md (若存在 CONTEXT-MAP.md, 则按映射定位各子上下文, 如 src/ordering/CONTEXT.md)
- 对话中遇到与术语表冲突或含糊的词, 立即向用户指出矛盾并提议唯一的规范术语
- 用具体场景和边界案例对概念关系做压力测试, 同时与代码交叉验证——用户说法与代码行为矛盾时摆到桌面上
- 术语一经敲定, 当场更新 CONTEXT.md (不存在则现场创建), 逐条即时写入, 不攒批
- 若某决策同时满足三条 ADR 标准, 才提议写 ADR 到 docs/adr/, 否则跳过

- 文件结构约定: 单上下文 = 根目录 CONTEXT.md + docs/adr/ (ADR 按序号命名如 0001-xxx.md); 多上下文 = 根目录 CONTEXT-MAP.md 作为索引指向各子目录; 两种结构决定我读哪里、写哪里
- 惰性建文件: 只在有内容可写的那一刻才创建 CONTEXT.md 或 docs/adr/, 绝不预建空壳——第一个术语敲定才建术语表, 第一个合格 ADR 才建目录
- 双重质量闸门: CONTEXT.md 严格限定为纯术语表, 禁止混入实现细节/规格/暂存内容; ADR 有触发过滤器, 须同时满足 '难以逆转 + 未来读者会困惑 + 真实权衡' 三条才提议
- 唯一外部依赖: 本地格式规范文件 CONTEXT-FORMAT.md 与 ADR-FORMAT.md (skill 引用的写作模板), 无任何外部 API/库/模型调用
