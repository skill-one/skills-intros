# reproduce-bug-report (`warpdotdev/common-skills/reproduce-bug-report`)

## comments

- user: 后端老兵, category: 坑, comment: 我拿它去复现 CI 挂掉的构建问题,被明确告知只管能录屏看到的 UI bug。纯后端、构建、依赖问题别来,录屏证明不了任何事。
- user: QA 七年老手, category: 妙用, comment: 一次批量派三个 agent,分别测 Windows、首次安装态、旧设置三种环境,比我手动挨个点省一下午,三条录屏直接进工单。
- user: 第一次提交 bug 的新手, category: 坑, comment: 起初只贴了「按钮点不动」五个字,报告回来是部分复现加一堆假设。后来把 issue 原文、评论、截图全贴进去,一次就复现了。
- user: 技术支持妹, category: 注意, comment: 它设计上不碰用户凭据,需要私密账号状态的工单会直接回 blocked,不会瞎试。我学会了给 Slack 频道和 thread id,录屏会直接回贴到原线程。
- user: 老项目维护者, category: 注意, comment: 它坚持对齐报告者的确切版本。我答不出用户用的哪个 build,报告里老实写了版本未知并说明用了最接近的替代版本,建议先问清版本号。
- user: 前端老兵, category: 妙用, comment: 它一复现出 bug 就停手不再改变量,录屏加按 01/02/03 排序的截图存进产物目录,我的修复 PR 第一次附上了像样的证据链。
