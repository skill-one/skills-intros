# ponytail-review (`dietrichgebert/ponytail/ponytail-review`)

## whitebox

- 触发词匹配 ("review for over-engineering" / "what can we delete" / "/ponytail-review" 等), 进入过度工程专项 review 模式
- 读取 diff, 只扫一类问题: 不必要的复杂度 (重造标准库轮子、多余依赖、投机抽象、死代码/死灵活性)
- 每条发现输出固定一行 `L<line>: <tag> <what>. <replacement>.`, tag 从 delete/stdlib/native/yagni/shrink 五选一
- 收尾输出唯一指标 `net: -<N> lines possible.`; 若无可删项则输出 `Lean already. Ship.` 并停止
- 全程只列清单不动手改, 修复留给用户或正常 review 流程

- 五标签分类法, 每个标签强制绑定"替代物"约束: delete=直接删 (无替代), stdlib=命名标准库函数替代, native=命名平台原生特性替代, yagni=单一实现的抽象/没人设的配置 (内联它), shrink=给出更短的等价写法; 多文件 diff 前缀改为 `<file>:L<line>`
- 范围闸门: 正确性 bug、安全漏洞、性能一律显式出界, 路由到普通 review pass 而非本流程; smoke test 或 assert 自检属 ponytail 最低配置, 永不标记删除; 退出条款: "stop ponytail-review"/"normal mode" 恢复冗长 review 风格
- 零外部依赖: 不调用任何外部工具/库/模型 API, 解析、分类、评分全靠 skill 内置规则完成 (评分公式即净删行数)
