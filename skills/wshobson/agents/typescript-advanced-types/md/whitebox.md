# typescript-advanced-types (`wshobson/agents/typescript-advanced-types`)

## whitebox

- 识别任务是否命中适用场景 (复杂类型逻辑 / 可复用类型工具 / 类型安全组件 / JS→TS 迁移等)
- 匹配 5 大核心能力之一: 泛型、条件类型、映射类型、模板字面量类型、工具类型
- 若导航级示例不够用, 再读 references/details.md 补充 Advanced Patterns 详细范例
- 按 Best Practices 落地代码 (unknown 优先于 any、strict 模式、const 断言), 并用 AssertEqual / ExpectError 做类型级测试验证
- 交付前过一遍 Common Pitfalls 与性能红线 (禁滥用 any、避免深层条件嵌套、限制递归类型深度)

- 解析与转换完全在 TypeScript 编译器类型系统内完成: 条件类型 `T extends X ? A : B` 做分支, `infer` 反向提取类型 (如 ReturnType), 映射类型 `[K in keyof T]` 做属性遍历/过滤/重命名 (as 子句), 模板字面量类型做字符串类型的拼接与变换 (Uppercase/Capitalize 等)
- 校验靠类型级测试, 不写运行时代码: AssertEqual 双向 extends 断言类型相等, ExpectError<T extends never> 在类型不符时编译报错
- 唯一外部依赖是本地文件 references/details.md (按需懒加载); 无外部库、无 API、无模型调用
