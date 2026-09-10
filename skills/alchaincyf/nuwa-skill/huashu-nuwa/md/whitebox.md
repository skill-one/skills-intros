# huashu-nuwa (`alchaincyf/nuwa-skill/huashu-nuwa`)

## whitebox

- 入口分流 (Phase 0)：判断输入是明确人名（直接路径）还是模糊需求（诊断路径，反推2-3个候选人/主题），同时澄清聚焦方向、本地语料和蒸馏档位（快速/标准/深度），并在开跑前报成本量级。
- 建目录 (Phase 0.5)：创建 .claude/skills/<name>-perspective/ 结构，含 references/research/（6个调研文件）和 sources/，本地语料（PDF/字幕/博客）先归档进去。
- 并行调研 (Phase 1)：spawn 6个 subagent 分别调研著作/对话/表达/他者评价/决策记录/时间线，每个agent强制把结果写入对应 research/*.md（含来源URL和一手/二手标记），完成后暂停展示调研质量摘要表，用户确认才继续。
- 框架提炼 (Phase 2)：汇总素材，用三重验证（跨域复现/生成力/排他性）从15-30个候选论点筛出3-7个心智模型，再提取决策启发式、表达DNA、价值观反模式、诚实边界，二次checkpoint确认。
- 构建与验证 (Phase 3-5)：按 skill-template.md 组装 SKILL.md（含自动推导的 Agentic Protocol 研究工作流），跑 quality_check.py 六项自检 + 子agent三项测试（已知/边缘/风格）+ 双Agent精炼，全部通过后交付。

- 多Agent分工采集 + 文件即断点：6个subagent各管一个信息维度（要求：引语必须有出处、区分「他说过/别人说他/我推断」、保留矛盾不和稀泥），调研结果强制落盘到 references/research/，所以调研文件本身就是断点——上下文不够或成本失控时可直接分阶段续跑不清零；外部依赖是 WebSearch/fetch，视频字幕用自带脚本 download_subtitles.sh + srt_to_transcript.py，PDF/网页转写优先复用已装skill（gemini-video、web-article-reader、pdf）。
- 三重验证过滤通用观点（Phase 2 核心转换）：每个候选论点过三关——跨域复现（≥2个领域出现）、生成力（能推断他对新问题的立场）、排他性（不是所有聪明人都这样想）；全过→心智模型，只过1-2关→降级为决策启发式，0关→丢弃；方法论文档从 references/extraction-framework.md 读取，而非模型自由发挥。
- 分层质检防编造：quality_check.py 自动检查6项硬标准（模型数3-7、每个模型有局限、表达DNA辨识度、诚实边界≥3条、内在张力≥2对、一手来源>50%）；不依赖自评，用独立子agent跑已知/边缘/风格三项测试（边缘问题的期望答案是「基于模型X推断，但不确定」而非斩钉截铁）；信息源黑名单（知乎/公众号/百度百科）在agent prompt中硬编码排除。
