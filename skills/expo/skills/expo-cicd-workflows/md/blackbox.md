# expo-cicd-workflows (`expo/skills/expo-cicd-workflows`)

## blackbox

**function**: 帮 Expo 应用开发者编写和管理「自动化流水线」配置文件——就是那份告诉云端"代码一有变动, 就自动打包、测试、发布应用"的指令清单.

- input: 一句需求: 「每次合并代码到 main 分支, 自动构建安卓包并提交测试」, output: 一个可直接使用的 .eas/workflows/deploy.yml 配置文件
- input: 一个已有的 workflow YAML 文件, output: 检查结果 + 修正后的文件 (语法错误、缺失参数、写错的引用都标出来并修好)
- input: 一个问题: 「EAS 流水线支持哪些触发方式和任务类型?」, output: 一份按官方最新规范整理的答案清单 (触发条件、可用的任务种类、各自参数)
