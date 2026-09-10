# extension-to-functions-codebase (`firebase/agent-skills/extension-to-functions-codebase`)

## blackbox

**function**: 把一个已安装的 Firebase 扩展 (云服务插件) 变成你自己的两样东西之一: 一套能直接部署进自己项目的云函数代码, 或一个可发布分享的 npm 包 (代码包, 别人安装后一行代码就能用)。

- input: 一个已安装的 Firebase 扩展的源码目录 + 一句「我要放到自己项目里」, output: 一套独立的云函数代码库, 附带配置文件 (.env), 你自己跑一条部署命令即可上线, 原扩展功能照常工作
- input: 同一份扩展源码 + 一句「做成 npm 包」, output: 一个可直接发布的 npm 包, 附带 README (安装步骤、参数配置对照表、新旧方式差异说明), 使用方装包后一行 re-export 即可启用
- input: 用旧版 (第一代) 云函数语法写的扩展代码, output: 升级为新版 (第二代) 语法的等价代码: 触发器、权限声明、API 开通、部署后初始化任务全部同步改好, 功能不变, 且附上兼容旧写法的适配层
