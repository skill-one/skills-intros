# ponytail-audit (`dietrichgebert/ponytail/ponytail-audit`)

## whitebox

- 触发词命中 ("audit this codebase"/"find bloat"/"ponytail-audit" 等) 即进入全仓审计模式
- 遍历整个代码库 (不是 diff), 按固定模式清单找过度工程: 标准库已有却手写的、单实现接口、只有一个产品的工厂、纯转发的 wrapper、单导出文件、死掉的 flag/配置
- 把发现归入五个标签: delete / stdlib / native / yagni / shrink
- 按砍掉量排序 (最大刀在前), 每条发现输出一行: 标签 + 砍什么 + 替代方案 + [路径]
- 结尾给总计: net: -N 行, -M 个依赖; 无可砍则输出 "Lean already. Ship."

- 模式指纹匹配: 全靠 skill.md 内置的过度工程特征清单做检索 (依赖冗余、单调用方层、只委托的包装、死配置、手搓标准库), 无任何外部工具/库/模型 API 依赖
- 标签即处方: 每类发现绑定固定动作建议 — stdlib/native 必须点名具体函数/平台特性, shrink 必须给出更短写法, delete 对应'什么都不替代'
- 一次性 + 范围护栏: 只管过度工程与复杂度, 正确性/安全/性能明确排除 (导向常规 review); 只报不改, 不动手修; 说 "stop ponytail-audit" 即退出
