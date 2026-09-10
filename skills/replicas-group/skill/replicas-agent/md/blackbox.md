# replicas-agent (`replicas-group/skill/replicas-agent`)

## blackbox

**function**: 你说要做什么,我在云端直接替你动手完成,并把能打开、能使用、能分享的成果交到你手上。

- input: 一段需求,如「帮我做个报名页面,让我能点开看看」→ 你拿到一个公开网址,浏览器打开就是能用的网页, output: 一个公开可访问的预览网址,附界面截图
- input: 一个 GitHub 仓库或 PR 链接 +「帮我修掉这个 bug 并提交」, output: 一个创建好的 Pull Request,内含修改的代码和说明,可直接审阅合并
- input: 一句「跑完把结果发到 Slack 的 #dev 频道」或一个 Linear 工单链接, output: 对应频道里出现的消息(可带截图、文件),或已更新状态、写好评论的工单
- input: 「帮我建个问卷收集大家的选择」, output: 一条 Google 表单链接,发出去后还能帮你整理收到的回答
