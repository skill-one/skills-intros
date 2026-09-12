# parallel-deep-research (`parallel-web/parallel-agent-skills/parallel-deep-research`)

## whitebox

- 解析参数: 取话题 $ARGUMENTS, 校验 parallel-cli ≥ 0.3.0, 按话题生成小写连字符文件名 $FILENAME, 并选定处理器档位 (默认 pro-fast, 约 2–10 分钟)
- 异步提交任务: 执行 parallel-cli research run --no-wait --json, 立即返回 run_id / interaction_id / 监控 URL, 并把监控 URL 告知用户; 加 --text 让结果输出为 markdown 报告
- 轮询等结果: 执行 parallel-cli research poll "$RUN_ID" -o "$FILENAME" --timeout 540, 阻塞等待任务完成; 未完成则告知用户研究仍在服务端运行, 重跑同一 poll 命令继续等待
- 交付: 把 poll 打印到 stdout 的 executive summary 摘给用户, 告知生成的文件路径 ($FILENAME.md 报告 + $FILENAME.json 元数据) 及 interaction_id (供后续追问链式续接)

- 异步任务模型: --no-wait 让提交命令立即返回而非阻塞数分钟; 轮询用 --timeout 540 适配工具执行时长上限; 不给 poll 传 --json, 靠 -o 落盘防止大结果刷爆上下文, stdout 只保留 executive summary
- 输出格式转换: --text 把 API 默认的结构化 JSON 换成带内联引用的 markdown 报告 (报告式需求用); 可用 --text-description 进一步约束字数/侧重点; -o 落盘时 .md 仅在用了 --text 时生成, .json 恒定生成
- 多轮上下文链 + 外部依赖: 追问时用 --previous-interaction-id 传上一轮 interaction_id, 新任务自动携带全部前文, 且可降档用 lite-fast 等轻量处理器; 整条链路依赖外部工具 parallel-cli ≥ 0.3.0 (Parallel research API) 与互联网, 403 视为余额不足需先查询/充值
