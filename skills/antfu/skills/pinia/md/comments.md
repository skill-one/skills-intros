# pinia (`antfu/skills/pinia`)

## comments

- user: 前端新手, category: 坑, comment: const { user } = store 解构完页面就不更新了，折腾半天才发现要用 storeToRefs()。action 倒是可以直接解构。
- user: Vue 老兵, category: 妙用, comment: 在 setup store 里直接用 VueUse 的 useLocalStorage 存登录态，持久化不用自己写同步代码，意外地省事。
- user: SSR 项目负责人, category: 注意, comment: 吃过大亏：store 建在模块顶层，SSR 下用户数据互相串。必须在函数内调用 useXxxStore()，每个请求各拿各的。
- user: 测试工程师, category: 妙用, comment: 组件测试套 createTestingPinia，store 全变 mock，只需断言 action 被调用过，不用造真实数据。
- user: Vuex 迁移户, category: 启发, comment: 从 Vuex 迁来才想明白：mutations 是历史包袱，Pinia 直接在 action 改 state 就行，代码量立减三分之一。
- user: 开发体验控, category: 注意, comment: 每个 store 文件记得加 acceptHMRUpdate 那几行，改 store 热更新不丢状态，否则一改就整页刷新。
