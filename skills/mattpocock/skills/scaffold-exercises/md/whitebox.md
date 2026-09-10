# scaffold-exercises (`mattpocock/skills/scaffold-exercises`)

## whitebox

- 解析计划: 提取 section 名、exercise 名和各 exercise 的变体类型 (problem/solution/explainer)
- 建目录: 按 XX-section-name/XX.YY-exercise-name 命名规则 mkdir -p 每条路径
- 写 readme 存根: 每个变体文件夹生成一个非空 readme.md (标题+描述)
- 跑 lint: 执行 pnpm ai-hero-cli internal lint 校验结构
- 修复并重跑: 按报错迭代, 直到 lint 通过

- 命名约定转换: section 编号 XX + exercise 编号 XX.YY, 名称统一 dash-case (小写连字符)
- 最小存根生成: 未指定变体时默认只建 explainer/; readme-only 即可满足要求 (无代码则不需 main.ts), readme 必须非空且无坏链接
- 外部校验工具: 依赖 `pnpm ai-hero-cli internal lint` 检查子文件夹、readme、.gitkeep/speaker-notes.md、坏链接等规则; 移动/重编号时用 `git mv` 保留 git 历史后再重跑 lint
