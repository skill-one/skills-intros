# vue (`antfu/skills/vue`)

## blackbox

**function**: 你描述需求或丢给我 Vue 代码, 我给你写好、改好或修好的 Vue 3 组件代码 (TypeScript, 现代写法), 可直接放进项目用。

- input: 一句需求: 「写一个用户卡片组件, 支持传入姓名和头像, 点击卡片时通知父组件」 → , output: 一个完整的 .vue 组件文件: 含 props 定义、点击事件上报、类型标注, 复制进项目即可运行
- input: 一段旧版 Vue 2 组件代码 (options API 写法, 带 this 和 data/methods) → , output: 改写成现代 Vue 3 写法的同一组件: <script setup lang="ts">、组合式函数, 功能不变但更简洁
- input: 一段报错或截图描述: 「v-model 双向绑定子组件时控制台警告, 数据不更新」 → , output: 修好的组件代码 + 一两句说明问题出在哪、改动点是什么
