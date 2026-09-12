# vue-router-best-practices (`antfu/skills/vue-router-best-practices`)

## blackbox

**function**: 帮你解决 Vue 页面跳转 (路由) 的问题: 你贴代码或描述现象, 我给出能直接用的正确写法, 告诉你坑在哪。

- input: 一段路由守卫 (跳转前的拦截检查) 代码, 现象是页面不停跳转卡死, output: 修复后的代码, 附一句话说明死循环的原因
- input: 问题描述: 「从 /user/1 点到 /user/2, 地址变了但页面数据没刷新」, output: 能让数据跟随地址更新的组件写法
- input: 一份用了旧式 next() 写法的守卫代码, output: 改写成当前推荐写法的同功能代码
- input: 现象描述: 「页面切走后, 定时器/事件还在后台跑」, output: 带清理逻辑的修复代码
- input: 「我要做一个正式上线的单页应用, 该怎么配路由」, output: 一份可直接套用的路由配置
