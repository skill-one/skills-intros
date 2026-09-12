# dart-use-pattern-matching (`dart-lang/skills/dart-use-pattern-matching`)

## comments

- user: Flutter 独立开发者, category: 妙用, comment: 页面状态建成 sealed class 再配 switch 表达式, 后来加"重试中"状态, dart analyze 直接标出没处理的新分支, 线上再没漏判过状态。
- user: 从 Java 转来的新手, category: 坑, comment: 从别的语言带来习惯, 以为 case 会贯穿执行, 把两段逻辑放相邻 case 等它顺下去, 结果非空 case 隐式 break, 后半段压根没跑。
- user: 后端老兵, category: 注意, comment: Map 模式会忽略多余的 key, List 模式却要求长度完全一致 (除非补 ...), 校验外部数据前想清楚这点, 我默认两者都宽松吃过亏。
- user: 做 code review 的技术组长, category: 注意, comment: switch 表达式穷尽检查是真香, 但别习惯性补 _ 兜底——一旦加了, 新增子类型不再报错, 安全网直接失效, 我们组规则是尽量不写 _。
- user: 第一次用的新手, category: 坑, comment: 解构后端返回时用 ! 模式断言, 对方少传一个字段就运行时崩, 换成 ? 判空模式让它不匹配走 else, 再配提示文案才稳。
- user: 全栈老炮, category: 启发, comment: 以前满屏 if-else 判类型, 现在先把数据建成 sealed class 再 switch, 漏没漏分支编译器说了算, 连建模习惯都被带变了。
