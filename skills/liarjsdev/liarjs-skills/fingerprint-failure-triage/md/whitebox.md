# fingerprint-failure-triage (`liarjsdev/liarjs-skills/fingerprint-failure-triage`)

## whitebox

- 跑 `npx liarjs@0.3 --all --json scan.json` 拿全量结果: 40 项检查的通过/失败状态 + 原始指纹, 通过项也要, 因为它是区分同因异源的依据
- 用 references/interpreting-checks.md 把失败 id 逐个查表归因, 按 四个来源(启动配置/页面改写层/网络路径/机器镜像) 分组, 输出分组结论而非失败清单
- 标记预期内的固有失败: headless 检查在 headless 下、tz 在数据中心 IP 下失败属正常, 不进调查
- 一次只改一处再重扫, 或用 `npx liarjs@0.3 diff before.json after.json` 只看状态变动的检查项来锁定因果

- 外部工具 liarjs (经 npx 调用的 npm 包): `--all --json` 产出含全量 check id 的扫描 JSON; `diff` 子命令做前后对比, 只打印状态移动的项
- 归因核心是查表: references/interpreting-checks.md 为每个 id 定义测量内容 + 归属组件, 把分数还原为 owner 列表
- 两条判别规则消歧: worker-consistency 挂而主线程过 → 改写只达主线程 (Web Worker 是独立 JS realm, 独立读取身份值); native-integrity 只反映函数替换方式, 与返回值是否合理无关
