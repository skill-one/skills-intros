# vue-testing-best-practices (`antfu/skills/vue-testing-best-practices`)

## comments

- user: 第一次写测试的新手, category: 坑, comment: 我一开始全靠 snapshot 测试, 界面变了就无脑更新快照, 后来组件坏了测试照样绿。改回断言真实渲染行为后, 真抓到过好几个 bug。快照只能当辅助。
- user: 前端两年经验, category: 坑, comment: 发完请求紧跟断言, 数据没回来就挂, 失败位置还每次不一样。改成先 await 请求、flushPromises 刷完异步队列再断言, 偶发失败直接归零。
- user: 组件库维护者, category: 妙用, comment: 我们的 Modal 用 teleport 挂到 body, wrapper.find 死活找不到内容。别在组件 wrapper 里死磕, 直接去 document.body 查, 秒过。
- user: 从 Jest 迁移来的, category: 注意, comment: 测试报 injection Symbol(pinia) not found, 我以为是版本冲突折腾半天。其实是没装插件: createPinia 塞进 global.plugins 就好。先查这步再排查别的。
- user: 后端转前端的, category: 启发, comment: 以前测试全绑组件内部实现, 改个 ref 名一片红。换成黑盒思路: 给 props、触发事件, 只看输出。现在放心重构, 测试一条不用动。
- user: 定技术方案的小组长, category: 注意, comment: 要测 computed 样式或真实 DOM 事件, jsdom 这类 node 环境跑不了, 得选浏览器环境的 runner; E2E 直接上 Playwright。选型时先分清哪些用例必须真浏览器, 别等 CI 挂了再改。
