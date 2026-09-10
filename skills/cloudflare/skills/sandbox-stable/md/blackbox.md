# sandbox-stable (`cloudflare/skills/sandbox-stable`)

## blackbox

**function**: 帮你搭建和维护跑在 Cloudflare 上的「云端 Linux 小电脑」应用：从零写出可部署的项目，或修好你现有的一个。

- input: 一句话需求，如："做一个网页，访客点按钮就能在里面运行 Python 代码并看到结果", output: 一个完整可部署的项目（服务端代码 + 容器配置），部署后得到一个网址，打开就能用
- input: 你现有的项目代码文件夹（用的是旧版接口、跑起来有告警或报错）, output: 更新后的代码：能编译、能部署，功能不变，并附一句改动说明
- input: 报错信息或现象描述，如："部署后 Worker 连不上沙箱，日志里是 XXX 错误", output: 定位到的问题原因 + 修好的代码，直接替换即可运行
