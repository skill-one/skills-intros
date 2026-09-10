# pr-walkthrough (`warpdotdev/common-skills/pr-walkthrough`)

## comments

- user: 刚接手同事项目的新人, category: 妙用, comment: 大 PR 我先按 tour 把四个视图走完再读代码, 顺序不乱。点节点还能跳到 GitHub diff 的具体行号, 直接当 diff 目录用。
- user: 内网开发的安全老兵, category: 坑, comment: 断网双击 index.html 直接白屏——D3 是从 CDN 拉的, file:// 本地打开也救不了。先确认浏览器能出外网, 或让生成时把 D3 内联进 HTML。
- user: 想省 review 时间的后端, category: 注意, comment: 它不是 review 工具, 不找 bug 也不给 approve, 只帮你搞懂改动结构。想让它挑逻辑错是白跑, 结论还得自己读代码下。
- user: 维护老仓库的开源作者, category: 妙用, comment: 分支没开 PR 也能出图, 它会自己推断默认分支当 base 算 diff。我清理陈年分支前先跑一份, 看清牵连面再决定动不动。
- user: 全键盘 vim 党, category: 妙用, comment: 1~4 切四个视图, n/p 走 tour, f 一键适配窗口, / 搜文件名。第二遍过 PR 全程没碰鼠标, 比挨个找按钮快得多。
- user: 带 5 人小组的 tech lead, category: 启发, comment: 以前 onboarding 我手画架构图, 现在每个 PR 自带一份。小 PR 只出两三个节点不是偷懒, 是按规模刻意缩放, 这种克制反而敢信。
