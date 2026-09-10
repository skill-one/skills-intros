# sandbox-migrate-to-next (`cloudflare/skills/sandbox-migrate-to-next`)

## blackbox

**function**: 把还在用旧版 Cloudflare Sandbox 的项目,整体改造成适配新版 1.0 预览版(@next)的代码,改完可直接部署上线。

- input: 一个还在用旧版 @cloudflare/sandbox 的项目(本地代码路径或仓库), output: 升级后的项目:依赖换成新版、Dockerfile 镜像更新、所有旧写法的调用点已重写,并附一份「改了什么、为什么改」的清单
- input: 一段旧写法的代码,如 await sandbox.exec("npm test"), output: 改写好的新写法代码(改为传入命令数组、再取输出结果),功能不变,并指出旧写法里会踩坑的地方
- input: 一个上线前的疑问,如「能不能让新旧版本慢慢灰度切换?」, output: 明确答复与操作建议(此场景必须一次性整体替换,不能逐步切),并在真正动线上环境前先跟你确认
