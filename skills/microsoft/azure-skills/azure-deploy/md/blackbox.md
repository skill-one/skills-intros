# azure-deploy (`microsoft/azure-skills/azure-deploy`)

## blackbox

**function**: 把已经准备就绪的应用部署上线到 Azure 云端, 部署完成后交付可访问的正式网址; 应用没准备好时我拒绝动手并指路。

- input: 一个已通过准备和校验的项目 (含 .azure/deployment-plan.md) + 一句 "ship it / 推上生产", output: 应用在云端跑起来, 你收到形如 https://myapp.azurewebsites.net 的正式访问链接
- input: 已部署过的项目代码有更新 + "push to cloud / 重新发布", output: 新版本部署完成, 同一个网址刷新后就是更新后的应用
- input: 一个从未准备过的新项目 + "创建并部署", output: 我不会开始部署, 会明确告诉你先完成准备和校验步骤, 拿到已验证的部署计划再来找我
