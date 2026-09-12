# conventional-commit (`github/awesome-copilot/conventional-commit`)

## comments

- user: 后端老兵, category: 妙用, comment: 提交全规范后, `git log --grep "feat(parser)"` 一条命令就能捞出某模块所有功能提交, 排查回归快多了。
- user: 第一次用的新手, category: 坑, comment: 改完文件没先 `git add` 就让它提交, 结果进去的还是上次暂存的旧代码, 白跑一趟, 记住流程第一步是暂存。
- user: 开源项目维护者, category: 注意, comment: description 必须用祈使句: 写 "added" 不合规, 一律 "add/fix", 像下指令, 不是写日记。
- user: 五人小团队 TL, category: 妙用, comment: 破坏性改动用 `feat!:` 并在 footer 补 BREAKING CHANGE 说明, 同事升级前一眼看到, 省掉无数群内解释。
- user: 独立全栈开发者, category: 注意, comment: 它生成后会直接执行 commit 不等你确认, 想改措辞要么事前说清, 要么事后 `git commit --amend` 补救。
- user: 刚入职的实习生, category: 启发, comment: 以前一把梭全提交, 但 type 只能选一个才学乖: 用 `git add -p` 分批暂存, 一类一提交, 历史一下子能读了。
