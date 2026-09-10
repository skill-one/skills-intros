# resolve-merge-conflicts (`warpdotdev/common-skills/resolve-merge-conflicts`)

## whitebox

- 运行 extract_conflict_context.py 出汇总: 哪些文件未解决、各处于哪个 index stage、每个文件有几个冲突块
- 用 --file 逐个下钻: 只打印邻近上下文 + 每个冲突块的 ours/base/theirs 三段 + ours↔theirs 的紧凑 diff
- 解决: 合适时整体取一侧 (git checkout --ours/--theirs), 否则直接编辑删掉冲突标记; 紧凑视图不够才整读文件
- 复查: 重跑汇总脚本 + git diff --name-only --diff-filter=U, 逐文件直到清零
- 校验收尾: 确认无 <<<<<<< / ======= / >>>>>>> 残留, 跑针对性 tests/builds/linters, stage 已解决文件

- 紧凑提取代替整读: Python 脚本只输出未解决路径、冲突块上下文和两侧差异, 不把整个文件灌进上下文; 可用 --context / --max-lines / --json 控制输出量
- 两类冲突统一处理: 覆盖标记型文本冲突和 index-only 冲突 (add/add、modify/delete); 工作区文件没有冲突标记时, 脚本回退到 index-stage 预览
- 外部依赖: git (checkout --ours/--theirs、diff --diff-filter=U) + Python 3 运行脚本; 校验阶段按需调用项目的 tests/builds/linters, 不涉及模型 API
