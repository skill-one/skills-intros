# resolve-merge-conflicts (`warpdotdev/common-skills/resolve-merge-conflicts`)

## blackbox

**function**: 当 Git 合并/变基/搬提交卡在冲突时, 我替你把冲突解决干净, 让代码恢复到能继续提交的状态。

- input: 一个 git 合并卡住、文件里满是 <<<<<<< >>>>>>> 标记的仓库, output: 所有冲突解决完的仓库: 标记清零、改动已暂存, git status 不再显示未合并文件
- input: 一个冲突文件的路径, 如 src/api.ts, output: 只展示该文件冲突处的双方改动对比, 以及改好后的文件 (不用你通读上千行)
- input: 一句裁决, 如 "这个文件保留我这边改的版本", output: 该文件整体替换为你指定一方的内容, 暂存完毕, 无残留冲突标记
