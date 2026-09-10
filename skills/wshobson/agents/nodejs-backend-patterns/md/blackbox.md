# nodejs-backend-patterns (`wshobson/agents/nodejs-backend-patterns`)

## blackbox

**function**: 把你要的线上服务需求变成能直接运行的 Node.js 后端代码 (负责注册登录、数据存取、给 App/网站提供接口的服务端程序)。

- input: 一句话需求: 「做一个用户注册登录接口, 密码要加密, 登录后能保持登录状态」, output: 一个可运行的 Node.js 项目: 含注册、登录接口和登录状态验证 (token 通行证) 的完整代码, 附带怎么启动的说明
- input: 一个已有的 Express 项目文件夹路径, output: 修改后的项目: 加上了统一的错误处理、参数校验 (挡住乱填的数据) 和接口限流 (防恶意刷接口), 并说明每处改了什么
- input: 需求描述: 「我要商品列表、下单、查订单这几个接口, 数据存 MySQL」, output: 完整的接口代码 + 数据库连接配置和建表脚本, 接口可直接和前端/小程序对接
