# clerk-cli (`clerk/skills/clerk-cli`)

## whitebox

- 会话起步: `clerk --version` 确定二进制并全程绑定; `clerk doctor --json` 体检登录、项目 link、密钥与环境健康, 有问题先修再继续。
- 发现端点: `clerk api ls [关键词]` 在 CLI 内置的 OpenAPI 目录中动态查找接口路径, 不凭记忆猜。
- 发起请求: `clerk api <path>` 自动带上凭证并解析目标 app/instance (repo 的 git remote + link 元数据, 也可 `--app`/`--instance` 显式指定); 读操作把大响应先落盘, 再用 `jq` 抽取所需字段。
- 变更操作: 先加 `--dry-run` 预览请求, 确认无误后去掉它 (必要时加 `--yes`) 真正执行; 实例配置优先走 `clerk config patch/put` 而非裸端点。
- 可信性检查: 一旦出现沙箱告警 (keychain/登录/link/网络失败), 该次结果视为不可信, 换到宿主 shell 重跑同一条命令。

- 预认证网关: `clerk` 二进制封装三套 API (默认 Backend、`--platform` Platform、`--fapi` Frontend), 自动处理 OAuth 凭证 (存 OS keychain)、密钥解析与 app/instance 定位, 无需手写 curl; 未登录时可走 accountless 临时密钥路径。
- OpenAPI 目录 + 请求校验: 接口靠 CLI 自带的 OpenAPI 目录枚举发现; JSON 请求体必须合法, 非法 payload 被 CLI 拒绝; agent 模式下交互式确认被绕过, `--dry-run` 是变更的唯一安全网。
- 上下文保护: GET 结果一律先写文件, 用 `jq` 做字段投影/聚合/翻页检查 (无 `jq` 时退回 python3 或 node), 只把小结果读回对话, 避免刷爆上下文。
