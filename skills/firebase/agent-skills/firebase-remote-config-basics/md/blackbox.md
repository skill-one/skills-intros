# firebase-remote-config-basics (`firebase/agent-skills/firebase-remote-config-basics`)

## blackbox

**function**: 帮你远程调整 App 的配置与功能开关(比如按比例放量、按地区开关功能),不用重新发版;也能告诉你 Android/iOS 里怎么接入读取这些配置。

- input: 一句需求,如「把新版红包弹窗只对 10% 的用户开放,且仅限日本地区」(Firebase 账号已登录), output: 一份按你要求改好的 remote_config.json 供你逐项确认;你回复「deploy」后改动即在线上生效,版本历史里可查到这次记录
- input: 你的 Firebase 项目 ID, output: 线上当前的远程配置模板,存成本地 remote_config.json 文件,可用于备份、审计或修改
- input: 「我的 Android/iOS App 怎么读取这些远程配置?」, output: 对应平台的接入做法:设置 App 内默认值、启动时拉取并生效、实时监听配置变化的代码示例
