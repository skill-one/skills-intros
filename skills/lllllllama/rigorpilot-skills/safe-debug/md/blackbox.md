# safe-debug (`lllllllama/rigorpilot-skills/safe-debug`)

## blackbox

**function**: 专治深度学习训练/推理中的各种报错：你把报错贴给它，它先给出「病根诊断报告 + 最小修复方案」，默认一行代码都不动，要改必须先经你批准。

- input: 粘贴一段训练崩溃时的报错（如 CUDA out of memory 的完整 traceback）, output: 一份诊断报告（DIAGNOSIS.md，讲清病根在哪）+ 一份最小修复清单（PATCH_PLAN.md），你的原代码零改动
- input: 加载模型 checkpoint 时报 shape mismatch 的终端输出, output: 诊断文档说明维度为何对不上、哪个环节引入的，附最小修复提案，等你明确点头后才动手改
- input: 一句「loss 训着训着变 NaN 了」+ 相关日志片段, output: 排查报告：列出最可能的原因、逐条验证步骤，并明确标注哪个改动只是修 bug、哪个会改变实验含义影响可比性
- input: 「帮我直接把这个报错修了」, output: 仍先给诊断不给补丁；确需修改时给最小改动方案并请求批准，风险较高的改动会先建议你建存档点/分支再动手
