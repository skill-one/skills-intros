# convex-create-component (`get-convex/agent-skills/convex-create-component`)

## blackbox

**function**: 把一句功能需求变成能直接合入项目的 Convex 后端模块（Convex 是一种后端云服务）：自带独立数据表和对外接口，并接进你现有的应用，交付时代码能跑、类型检查通过。

- input: 一句需求，如「给我的应用加通知功能：用户能收通知、查未读数」, output: 一套可直接合入项目的后端代码：通知数据表、发送/查询未读的接口，前端调用时登录身份自动接好
- input: 一个现有项目文件夹 + 一句要求，如「把我的 Slack 集成抽成独立模块」, output: 改好的代码交付：独立模块 + 主应用里几行接入代码，边界问题（登录、配置、跨模块数据）已修好，`npx convex dev` 跑通
- input: 「这个模块要发布成 npm 包，团队其他项目也要用」, output: 一个可发布的模块包代码 + 各应用里的安装接入方式，每个接口的类型签名齐全，调用时拼写错误会直接报错
