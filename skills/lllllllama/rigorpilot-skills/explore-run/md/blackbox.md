# explore-run (`lllllllama/rigorpilot-skills/explore-run`)

## blackbox

**function**: 在深度学习研究项目里, 帮你规划并总结小规模"试跑实验"(先用少量数据、短周期快速验证想法), 最后交付一份"哪些尝试值得放大"的排名报告, 而不是直接宣称实验成功。

- input: 一个深度学习研究代码库 + 明确授权, 例如: "允许试跑, 先用 1% 的数据快速验证想法", output: explore_outputs/TOP_RUNS.md: 一份按「成本低、成功概率高、预期收益大」排好序的候选试跑清单, 每条注明建议的试跑规模 (如数据子集大小、训练步数)
- input: 想尝试的参数组合, 例如: "学习率 0.1 / 0.01 / 0.001 × 批大小 32 / 64, 每组只跑 500 步", output: explore_outputs/COMPARABILITY_REPORT.md 和 CHANGESET.md: 记录每次试跑改动了什么、哪些结果之间可以公平对比、哪些因条件不同不能直接比
- input: 一批已完成的小规模试跑结果, 例如: "这 6 次快速试跑的结果在这, 帮我挑值得继续的", output: explore_outputs/SCIENTIFIC_CHANGELOG.md 和 status.json: 一份只标注为「有限证据」的结论摘要, 明确指出哪几个值得投入正式训练、哪些还不够格下结论
