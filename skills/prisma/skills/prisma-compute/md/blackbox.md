# prisma-compute (`prisma/skills/prisma-compute`)

## blackbox

**function**: 把你的 TypeScript 网络应用一键部署上线，并帮你排查部署、构建、登录等环节的问题。

- input: 一个本地写好的 TypeScript 后端项目文件夹（如 Hono、Next.js、Nuxt 项目）, output: 一条公开可访问的线上网址，附应用 ID、部署 ID 等信息，直接发给同事就能打开
- input: 「部署失败了，报错：服务器在 localhost 上监听但公网打不开」, output: 原因诊断（监听地址写死成 localhost）＋ 修改后的代码或配置，改完即可正常访问
- input: 「帮我从零创建一个能直接部署的新项目」, output: 一个生成好的项目脚手架，含部署脚本，一条命令就能发上线
- input: 构建/部署失败的一段报错日志（或 GitHub 构建日志 ID）, output: 指出具体卡在哪一步（登录、构建、环境变量、端口），并给出对应的解决命令或改法
