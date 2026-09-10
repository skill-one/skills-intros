# playwright-best-practices (`currents-dev/playwright-best-practices-skill/playwright-best-practices`)

## blackbox

**function**: 我是你的网页自动化测试工程师: 给我一个网站或一段有问题的测试, 我交还给你能跑通的测试代码、失败原因分析或接入自动检查的配置。

- input: 一个'时好时坏'的测试文件 (有时过、有时挂), output: 修复后的测试代码 + 一段话说明之前为什么不稳定
- input: 你的网站 + 一句话需求, 如 '给登录功能写自动化测试', output: 可直接运行的测试代码文件, 覆盖正常登录、密码错误、已登录免登录等场景
- input: 一段测试失败的报错信息 (或 '元素找不到' 这类描述), output: 问题诊断结论 + 改好的代码, 直接替换原文件即可
- input: 你的测试项目, 要求 '每次提交代码自动跑测试', output: 接入 CI (持续集成, 代码提交后云端自动执行) 的配置文件, 合入即生效
