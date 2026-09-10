# gsap-react (`greensock/gsap-skills/gsap-react`)

## comments

- user: 刚学前端的新手, category: 坑, comment: 我直接在 useEffect 里写 gsap.to 没写清理，路由切走后动画还在改已卸载的节点，页面越用越卡。换成 useGSAP 就自动清理了。
- user: 从原生 GSAP 转来的老前端, category: 妙用, comment: 列表页 20 个卡片组件都用 .card 选择器会互相串。给每个组件传自己的 ref 当 scope，同名 class 互不干扰，代码一行没多写。
- user: Next.js 全栈开发, category: 注意, comment: 组件顶层直接调 gsap 或 ScrollTrigger 会报 window is not defined。动画代码要全放进 useGSAP/useEffect 里，只在客户端跑。
- user: 交互开发老手, category: 坑, comment: 在点击事件回调里直接 gsap.to，组件卸载后再点仍报错——回调不在 context 里。要用 contextSafe 包裹，并在 cleanup 里移除监听。
- user: 做后台管理界面的, category: 妙用, comment: tab 切换想让入场动画重播：默认 useGSAP 只跑一次，把依赖的 state 填进 dependencies 再开 revertOnUpdate，每次切换都重置重播。
- user: 被 useEffect 坑过的 React 开发, category: 启发, comment: 以前最怕依赖写错导致动画反复闪烁，useGSAP 默认空依赖只跑一次，不随 re-render 重跑，写起来安心很多。
