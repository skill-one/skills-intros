# ai-research-reproduction (`lllllllama/rigorpilot-skills/ai-research-reproduction`)

## comments

- user: 复现过十几篇论文的博士, category: 注意, comment: 上手前把论文预期指标和容差先给它，否则它只会判定『跑通了』而非『复现成功』，result-match 标不出来。
- user: 第一次用的新手, category: 坑, comment: 我以为它能全自动把训练跑完，结果默认只挑最小可信目标（先推理/评测），动数据集或指标前还停下等人确认。想全自动别选它。
- user: 组里管交接的工程师, category: 妙用, comment: 用它产出 repro_outputs/ 整套档案做组内交接，师弟照 COMMANDS.md 十分钟重跑成功，LOG.md 连我当时的踩坑和假设都留了底。
- user: 想刷分的科研狗, category: 启发, comment: 我让它改 loss 把分刷上去，被拒并要求写清对可比性的影响。后来才明白：改动不可审计的结果，论文根本不敢信。
- user: 显卡紧张的炼丹师, category: 妙用, comment: 长任务中途想停不用杀进程，往当前 run 目录丢一个 CANCEL 文件即可，整个进程树被取消，救过我半夜占着的 GPU。
- user: 被论文坑过的工程师, category: 注意, comment: README 和论文对不上时它不会擅自改协议，而是记录冲突再来问人。别嫌啰嗦，这正是『跑通就行』的工具给不了的。
