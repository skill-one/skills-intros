# caveman-learn (`juliusbrussee/caveman/caveman-learn`)

## whitebox

- 运行 caveman learn report --json，解析 caveman.learn.v1，呈现 Cave Score、四个组成部分和按 token 消耗排名的 sinks（每条标注类别：REDUCIBLE / RECURRING_CONTEXT / SKILL_DISTILLATION / LOAD_BEARING）；若带 spend 块则先报（只说窗口内成本，不外推）
- 用户挑选要处理的 sinks（可选先跑 caveman learn simulate <sink_id> 看历史扫描范围内的量级，不外推未来）
- 逐条走同意循环：REDUCIBLE 先 --dry-run 物化候选，给出具体 diff 和 before→after tokens/turn，用户说 yes 才用自己的文件工具落地；RECURRING_CONTEXT 和 SKILL_DISTILLATION 各有专属流程
- 重测门禁：改完重跑 report（或重数被改文件），after 必须低于 before，否则回滚；通过后跑 caveman learn applied <sink_id> 登记，供后续纵向判定
- 用 caveman learn savings 汇报收益，按证据等级分组呈现，逐条读出 confounders 和 provenance，绝不跨等级求和、绝不标称已验证

- 分析器只读 / 编辑器隔离：caveman CLI（learn 子命令）只测量不修改，是唯一的 token 计数来源；所有写入经我自己的文件工具 + caveman mem CLI，且每条编辑单独征得同意，无一键全应用
- 定位器 + 哈希校验（RECURRING_CONTEXT）：候选只携带 locator（rel_path、jsonl_line、block_index、content_sha256），不带正文；我本地重新打开该行、按空行分段定位块，对原始块算 sha256 与 locator 比对，不一致即中止；入库用 caveman mem remember --（-- 防止 --- 开头的块被当参数），删源前用 caveman mem recall 读 tokens_added 核算门禁，并保证召回命中 + 指针就位，否则回滚
- 证据等级账本：savings 按测量方式分四档（deterministic_remeasure / controlled_holdout / counterfactual_replay / interrupted_time_series），不同档不可相加；技能蒸馏不走净负门禁（成本和收益落在不同位置），改用 on/off 对照实验，每臂 ≥5 个会话才允许下结论
