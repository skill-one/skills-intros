# ai-research-explore (`lllllllama/rigorpilot-skills/ai-research-explore`)

## whitebox

- 校验准入: 必须同时有显式探索授权 (candidate-only / sweep / 探索性排名) 和持久的 current_research 锚点 (分支、commit、checkpoint、run 记录或已训练的本地模型), 输入接受 research_campaign 或旧版 variant_spec
- 冻结设定: campaign 模式下先固定任务、数据集、benchmark、评估来源、SOTA 参照和算力预算, 再开始任何候选工作; 按需用 analyze-project 生成仓库理解工件
- 门控排序想法: 保留研究者提供的想法, 至多补充少量单变量种子想法, 按期望收益/成本/成功率/补丁面/依赖拖累/评估风险/回滚容易度打分排序; 提议或排名前必须加载 research-thinking-loop 参考文件
- 单候选执行: 一次只推进一个清晰候选 — explore-code 做有界代码适配, explore-run 做短周期试验或 sweep; 仅当计划需要真实执行证据时才调用 minimal-run-and-audit 或 run-train, 跑完冒烟检查并按真实证据重排
- 产出工件: 经 scripts/orchestrate_explore.py 与 scripts/write_outputs.py 写入 analysis_outputs/、sources/、explore_outputs/, 必含 SCIENTIFIC_CHANGELOG.md 和 COMPARABILITY_REPORT.md, 且绝不把探索性收益包装成可信复现成功

- 双循环节奏: 外循环 (理解仓库 → 冻结设定 → 想法门控 → 判断下一个实验是否值得跑) + 内循环 (一个有界改动 → 冒烟检查 → 取证 → 对照锚点排名 → 停止或回外循环); 遇到硬阻碍、含义不明、预算耗尽、缺锚点/评估, 或头部想法过近、实现无法分解为可审计单元时, 停下来等人, 不静默自选
- 门控式参考加载 (声明前强制校验): 提议/排名候选前必加载 research-thinking-loop; 做新颖性、贡献、SOTA 或可比性声明前必加载 research-rigor-principles; 涉及训练/评估/基线/消融细节时加载 deep-learning-experiment-principles — 这些文件全部来自同级 ai-research-reproduction skill 的 references 目录
- 外部依赖: 同级 ai-research-reproduction 的 references (operating-principles / rigor-principles / experiment-principles / thinking-loop / explore-variant-spec); 本地 Zotero 优先的受限文献检索 (Zotero → 种子来源 → 仓库内定位器 → 公共定位器 → 可选 web, 只做来源解析不做开放式搜索); 确定性工件脚本 orchestrate_explore.py 与 write_outputs.py; ~/.rigorpilot/PERSONAL_RIGOR.md 仅作咨询性输入; 全程未使用任何模型 API (skill 未涉及)
