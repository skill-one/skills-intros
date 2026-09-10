# vue-best-practices (`antfu/skills/vue-best-practices`)

## comments

- user: 前端组长, category: 妙用, comment: 先让它画组件边界图再动手，props/emits 契约一目了然，评审省半天，基本零返工。
- user: Vue2 老项目维护者, category: 坑, comment: 项目用 Options API 没提前声明，它按 Composition API 给我重写。开口第一句必须说清技术栈。
- user: 第一次用的新手, category: 注意, comment: 动画、Teleport 这类功能它默认不加，需求里不写就不出现。要什么直接点名，别等它猜。
- user: 接私活的独立开发, category: 坑, comment: 让它写个小 todo，结果拆成容器+表单+列表三个文件。随手 demo 想单文件，要明说才给例外。
- user: 后端转前端的, category: 启发, comment: 「状态只存一份、其余 computed 推导」点醒我了，删掉一堆冗余字段，改数据不用再全局搜索。
- user: 中后台老前端, category: 注意, comment: 别一上来就催性能优化，它坚持功能先跑通。说「表格 1 万行卡顿」，它才给虚拟滚动方案。
