# python-appservice-deploy (`microsoft/azure-skills/python-appservice-deploy`)

## blackbox

**function**: 把你的 Python 网站项目 (Flask/Django/FastAPI) 一键部署上线到 Azure, 最后给你一个浏览器能直接打开的网址。

- input: 一个本地 Flask 项目的文件夹路径 + 你想给应用起的名字, output: 部署完成提示 + 可访问的网址, 如 https://应用名.azurewebsites.net
- input: 一个 FastAPI 项目的文件夹路径, output: 已上线的网址, 启动方式已自动配好, 不需要你自己写启动命令
- input: 之前部署过的应用名 + 改动后的代码, output: 新版本上线成功, 网址不变, 刷新即可看到更新
