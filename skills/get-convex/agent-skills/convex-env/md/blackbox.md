# convex-env (`get-convex/agent-skills/convex-env`)

## blackbox

**function**: 帮你把应用要用的密钥和配置 (如 API key、数据库密码) 安全地配到 Convex 云端环境里——代码能正常取用, 但密钥不会泄漏进代码或 git 仓库。

- input: 「把我的 OpenAI API key 配到线上」+ 密钥内容, output: 密钥已存入 Convex 线上环境, 后端代码随时能取到, 代码里和 git 里都看不到这串密钥
- input: 「看看现在线上都配了哪些环境变量」, output: 一份变量清单, 告诉你哪些已配好、哪个还缺——方便上线前查漏
- input: 一段把密钥直接写死在代码里的代码, output: 改好的代码: 密钥换成从环境变量读取, 真实密钥只存在云端, 不再出现在代码里
- input: 「本地开发和线上要用不同的 key」, output: 两边各自配好各自的值: 本地用本地文件, 线上用云端配置, 互不干扰
