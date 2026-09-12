# async-python-patterns (`wshobson/agents/async-python-patterns`)

## blackbox

**function**: 帮你把 Python 代码改写得又快又稳: 让它同时处理多个网络请求/数据库查询而不互相等待, 并修复卡死、漏写等待、超时失控等异步代码的常见毛病。

- input: 一个「抓完一个网页再抓下一个」的 Python 爬虫脚本 (100 个页面要跑 10 分钟), output: 改写后的并发版脚本: 100 个页面同时抓, 几十秒跑完, 附一段中文说明讲清改了哪里、为什么快了
- input: 一段运行时卡死不动或报错的 async Python 代码 (贴在对话里), output: 修好的可运行代码 + 逐处标注: 原来错在哪一行、为什么错、改成了什么
- input: 一句需求描述, 如「同时给 1000 个用户发请求, 单个超过 3 秒就放弃, 失败的单独列出来」, output: 可直接运行的完整 Python 代码, 自带超时中断和失败清单, 跑完打印「成功 N 个 / 失败 M 个」
