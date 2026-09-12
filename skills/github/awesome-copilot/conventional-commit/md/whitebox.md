# conventional-commit (`github/awesome-copilot/conventional-commit`)

## whitebox

- 运行 git status, 查看有哪些文件被修改
- 运行 git diff (或 git diff --cached) 检查具体改动内容
- 用 git add <file> 暂存改动
- 按固定 XML 模板 (type/scope/description/body/footer) 构造规范化的 commit 消息
- 在集成终端执行 git commit -m "type(scope): description" 完成提交

- 消息校验: type 必须取自枚举 feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert; description 必须用祈使语气 (add 而非 added); scope/body/footer 可选, footer 用于 BREAKING CHANGE 或 issue 引用
- 消息生成: 以 git diff 的改动内容为依据, 套用固定 XML 结构模板 <type><scope><description><body><footer> 产出符合 Conventional Commits 规范 (conventionalcommits.org v1.0.0) 的消息
- 外部依赖: 全程仅依赖本地 git CLI (status/diff/add/commit), 无需模型 API 或第三方库; 最终提交命令在集成终端自动执行
