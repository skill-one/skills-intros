# firebase-app-hosting-basics (`firebase/agent-skills/firebase-app-hosting-basics`)

## blackbox

**function**: 帮你的 Next.js / Angular 网站 (含服务端渲染) 部署上线到 Firebase, 并管好密钥和「代码一更新、网站自动跟着更新」。

- input: 一个 Next.js 或 Angular 项目文件夹 + 一句「帮我上线」, output: 部署完成的网址, 浏览器打开即可访问; 若你的 Firebase 项目还没开通按量付费, 会先给你一个开通链接再继续
- input: 一条命令 / 一句话: 「把我的 API 密钥配置好, 别写进代码里」, output: 密钥安全配置完毕, 网站能正常调用它, 且密钥不出现在代码和代码仓库里
- input: 你的 GitHub 仓库地址, output: 自动部署已设置好: 之后你每次推送新代码, 线上网站几分钟内自动更新, 无需手动操作
