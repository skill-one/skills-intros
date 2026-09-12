# vue-router-best-practices (`antfu/skills/vue-router-best-practices`)

## comments

- user: Vue3 新手, category: 坑, comment: 守卫里无条件 next('/login'),结果登录页自己也被拦,页面无限重定向白屏。必须先判断目标是否已是登录页再放行。
- user: 后端转前端, category: 坑, comment: 同一路由只换 id 参数,组件不重建,页面还是旧数据。后来 watch 路由参数更新才拿到新内容,别指望生命周期钩子。
- user: Vue2 老用户, category: 注意, comment: beforeRouteEnter 里访问不到 this,想拿组件实例得写进 next 回调。从 Vue2 迁移旧守卫代码时在这里连续报错。
- user: 前端组长, category: 妙用, comment: 把守卫里的鉴权接口改成 await 等返回再放行,页面不会再先渲染一下又跳转闪烁,白屏感和回跳都消失了。
- user: 独立开发者, category: 坑, comment: 组件里开的定时器和事件监听,路由跳走后还在后台跑,接口一直被打。离开页面时必须手动清掉。
- user: 第一次搭 SPA 的人, category: 注意, comment: 做单页应用别先裸写页面后补路由,第一天就装 vue-router,后补要改一堆 import 路径和跳转代码。
