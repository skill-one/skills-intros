# vercel-react-best-practices (`vercel-labs/agent-skills/vercel-react-best-practices`)

## blackbox

**function**: 帮你检查并改写 React / Next.js 网页代码, 让页面加载更快、操作更流畅。

- input: 一个打开很慢的 Next.js 页面代码, output: 优化后的代码 + 逐条改动说明 (如: 把逐个等待的 3 个数据请求改成同时发出, 首屏明显变快)
- input: 一个输入卡顿、越用越慢的 React 组件, output: 重构后的组件, 并指出具体病因 (如: 打包体积过大、无效重复渲染) 和对应修法
- input: 整个项目的前端代码目录, output: 一份性能体检报告: 按影响从大到小列出问题清单, 每条附上可直接使用的修复代码
