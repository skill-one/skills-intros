# migrate-to-shoehorn (`mattpocock/skills/migrate-to-shoehorn`)

## blackbox

**function**: 帮你把测试代码里别扭的 `as` 类型断言 (强行告诉 TypeScript「就当它是这个类型」) 换成更安全的写法, 让测试只填用得到的那几个字段, 不用伪造整个对象。

- input: 一个含 `getUser(req as Request)` 的 .test.ts 文件路径, output: 改好的同一文件: 那句变成 `getUser(fromPartial({ body: { id: "123" } }))`, 自动补上 import, 类型检查通过
- input: 一段故意传错数据的测试代码, 如 `{ body: { id: 123 } } as unknown as Request`, output: 对应的改写代码: `{ body: { id: 123 } }` 外面包上 `fromAny(...)`, 保留故意传错的意图
- input: 项目路径 + 一句话「测试里全是 as, 帮我清理掉」, output: 装好 shoehorn, 找出所有含 as 断言的测试文件并逐个改完, 最后跑一遍类型检查确认没有报错
