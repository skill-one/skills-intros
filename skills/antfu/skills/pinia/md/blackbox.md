# pinia (`antfu/skills/pinia`)

## blackbox

**function**: 帮你编写、排查和优化 Vue 应用中的状态管理 (Pinia) 代码——让数据在不同页面/组件间正确共享与更新。

- input: 「购物车数据要在商品页、购物车页、结算页之间共享, 怎么写?」, output: 一份可直接运行的 store 定义 + 各组件中的使用示例代码
- input: 一段状态不更新的 store 代码 (如直接解构导致丢失响应), output: 指出问题原因, 并给出修正后的代码 (如改用 storeToRefs)
- input: 一个组件测试文件 + 相关的报错信息, output: 基于 @pinia/testing 的正确测试写法, 附 mock store 的完整示例
