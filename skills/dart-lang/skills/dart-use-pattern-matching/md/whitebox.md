# dart-use-pattern-matching (`dart-lang/skills/dart-use-pattern-matching`)

## whitebox

- 识别待评估的数据结构 (JSON、Record、类、Enum)，这决定一切选型。
- 按产出物选开关构造：产值用 switch 表达式，执行副作用用 switch 语句。
- 定义具体模式 (Object/Map/List/Record)，用变量模式 (var x、:var y) 抽取字段；写不成模式的逻辑挂 `when` 守卫。
- 未覆盖的分支用通配符 `_` 或 `default` 收尾 (非 sealed 场景)。
- 跑 `dart analyze` 做穷尽性校验，按报错补齐缺失子类型的 Object 模式或加 `_`。

- 条件映射式模式选型：数据结构直接决定模式种类——JSON 校验+解构用 Map/List 模式一步完成；多返回值用 Record 模式解构；密封类家族 (代数数据类型) 用 Object 模式配 `sealed`；数值范围用关系模式 (>=、<=) 组合 &&；多分支共享逻辑用 ||（两侧须绑定完全相同的变量集）；忽略值用 `_` 或 rest 元素 `...`。
- Switch 双轨语义：表达式侧每个 case 只能是单个表达式、无隐式跌落、必须穷尽；语句侧空 case 跌落到下一 case，非空 case 隐式 break（不写 break 关键字）。
- 穷尽性由编译器背书：依赖 Dart 的 `sealed` 修饰符 + `dart analyze`（Dart SDK 自带静态分析器，无第三方库），报错形如 "The type 'X' is not exhaustively matched"。skill 运行时模型为 models/gemini-3.1-pro-preview，除此之外无外部 API 依赖。
