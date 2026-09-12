# openapi-spec-generation (`wshobson/agents/openapi-spec-generation`)

## blackbox

**function**: 把你的接口变成一份标准的 API 说明书 (OpenAPI 文档), 让前后端、调用方照着就能开发对接, 还能帮你检查代码和文档是否一致、自动生成调用代码。

- input: 一个后端项目路径 (如 FastAPI/Express 写的接口代码), output: 一份完整的 OpenAPI 文档文件 (.yaml), 每个接口的地址、参数、返回值示例、错误码都写清楚, 可直接放进文档站
- input: 一句需求, 如「设计一个创建订单的接口, 登录后才能调, 订单可取消」, output: 一份接口约定文档: 字段定义、鉴权方式 (如 token 放哪)、各种失败响应 (余额不足、重复下单等) 全部定好, 前后端拿到即可各写各的
- input: 一份已有的 OpenAPI 文档文件, output: 对应语言的客户端调用代码包 (如 Python/TypeScript), 拿来就能 import 调接口
