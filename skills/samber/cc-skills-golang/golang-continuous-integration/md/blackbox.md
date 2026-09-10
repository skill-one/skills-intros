# golang-continuous-integration (`samber/cc-skills-golang/golang-continuous-integration`)

## blackbox

**function**: 给你的 Go 项目配好 GitHub 上的自动化流水线 (CI/CD):推代码自动跑测试、代码检查、安全扫描,打标签自动发布。

- input: 一个还没有 CI 的 Go 项目仓库路径, output: .github/workflows/ 下的一套流水线文件(测试、代码检查、安全扫描、覆盖率),推代码后自动运行,失败会标红并给出原因
- input: 一段需求,如「我要发 v1.2.3,要 Windows/Mac/Linux 全平台二进制和 Docker 镜像」, output: 发布流水线配置:之后你只要打一个版本标签,就能自动拿到编译好的多平台文件、校验和与 GitHub Release 页面
- input: 一个现有但跑不好/配置缺失的 workflow yml 文件(或直接说「我的 CI 太慢/总漏测」), output: 补齐修复后的流水线文件:比如补上竞态检测、多 Go 版本矩阵测试、依赖自动更新机器人(Dependabot/Renovate)
