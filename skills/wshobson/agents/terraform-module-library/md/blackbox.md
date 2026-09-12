# terraform-module-library (`wshobson/agents/terraform-module-library`)

## blackbox

**function**: 把「你想要的云上基础设施」(如网络、数据库、存储) 写成可直接复用的 Terraform 代码模块, 一次编写、全团队反复调用。

- input: 一段需求描述, 如「AWS 上要一个带 3 个私有子网的 VPC」, output: 一套拿来即用的 Terraform 模块代码: 资源定义 + 可配置参数说明 + 输出值 (子网 ID 等)
- input: 一份已有但写法混乱的 Terraform 配置文件, output: 按规范重构后的可复用模块, 带参数校验 (填错格式会直接报错提示)、统一打标签和 README 使用文档
- input: 一个写好的模块, 如「帮这个 VPC 模块补上测试和示例」, output: 配套的用法示例代码 + 自动化测试, 运行后能验证模块部署出来确实可用
- input: 一条组合需求, 如「生产环境要 VPC + PostgreSQL 数据库」, output: 组合调用多个模块的 Terraform 代码, 数据库自动接到 VPC 的私有子网里, 无需手动填写中间参数
