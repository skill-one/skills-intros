# ast-grep (`ast-grep/agent-skill/ast-grep`)

## whitebox

- 理解查询: 从自然语言需求中确认目标代码结构、语言、边界条件 (需要时向用户追问澄清)
- 造样例: 写一段代表目标结构的最小代码, 存为临时测试文件
- 写规则: 把结构翻译成 YAML 规则——简单结构用 pattern, 复杂结构用 kind + has/inside, 逻辑组合用 all/any/not
- 测试规则: 用 ast-grep CLI (scan --rule, 或 --inline-rules + --stdin 免建文件) 对样例验证; 不中则化简规则、补 stopBy: end、用 --debug-query 查看 AST 排查
- 全库搜索: 规则验证通过后, 用 scan (复杂规则) 或 run --pattern (简单匹配) 扫描真实代码库, 可加 --json 输出结构化结果

- AST 结构匹配 (核心解析): 依赖外部工具 ast-grep CLI 把代码解析成语法树, 按语法结构而非文本匹配; $VAR / $$$ 元变量捕获任意名称、参数列表、代码块
- YAML 规则引擎 (表达复杂查询): pattern (直接匹配) → kind (节点类型) → inside/has 关系规则 (沿语法树搜索, 必配 stopBy: end 遍历到子树末尾防漏配) → all/any/not 组合, 逐层叠加
- 调试与校验回路: 规则不匹配时用 --debug-query=cst|ast|pattern dump 语法树, 核对 kind 值与元变量识别; 规则复杂用规则文件、快速迭代用内联规则; shell 中元变量 $ 须转义为 \$
