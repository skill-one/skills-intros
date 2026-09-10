# prisma-compute (`prisma/skills/prisma-compute`)

## blackbox

**function**: 帮你把写好的 TypeScript 网站/接口一键发布上线, 并在发布出问题时帮你查明原因、修好再发。

- input: 一个在自己电脑上能正常跑起来的 TypeScript 项目 (如 Next.js、Hono、Nuxt 应用) 的文件夹, output: 一个任何人都能打开的线上网址, 部署完成后附上应用信息清单和后续要做的事 (如绑定数据库)
- input: 一句求助: 「部署成功了, 但线上一直转圈打不开」+ 项目路径, output: 一句直白的原因 (如服务只监听了本机地址, 外网进不来) + 改好的代码/配置, 重新发布后网址可正常访问
- input: 一句需求: 「我这个仓库里有 web 和 api 两个子应用, 想都发上去, 以后一条命令就能重新发布」, output: 一份写好的部署配置文件 (prisma.compute.ts), 之后执行 deploy web / deploy api 即可分别发布, 无需再设置
