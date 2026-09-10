# vite (`antfu/skills/vite`)

## blackbox

**function**: 帮你搞定 Vite (前端项目的构建工具) 相关的一切: 配置、报错、打包、升级迁移, 直接给你能用的代码和文件。

- input: 贴一段报错的 vite.config.ts 和错误信息, output: 修好的配置文件 + 一句话说明问题出在哪
- input: 「我在写 Vue 组件库, 要发布到 npm」或「要做 SSR 应用」, output: 可直接使用的 vite.config.ts, 以及 package.json 里需要同步修改的字段
- input: 一个旧版 (Vite 5/6) 项目的配置文件, 说「帮我升级到 Vite 8」, output: 迁移后的新配置文件 + 改动清单 (哪些写法过时了、换成了什么)
