# paper-context-resolver (`lllllllama/rigorpilot-skills/paper-context-resolver`)

## blackbox

**function**: 复现深度学习论文时, 帮你从原论文里查清 README 没写清楚的那个关键细节 (数据集划分、预处理、评测方式等), 并指出论文和 README 说法打架的地方。

- input: 一个代码仓库的 README + 一句话提问:「论文里 ImageNet 实验用的是哪个验证集划分?README 没写」, output: 一段简短答案, 附论文原文的具体出处 (章节/段落); 若 README 与论文说法不一致, 会额外给一条 ⚠️ 冲突提醒
- input: 论文链接 (arXiv/PDF) + 提问:「论文报告的 76.5% top-1 是单裁剪还是 10-crop 测出来的?」, output: 评测方式的答案, 并标注结论是「论文原文直接写的」还是「根据上下文推断的」, 不展开整篇论文的总结
- input: 仓库信息 + 提问:「仓库里放出的 model_best.pth 对应论文表 2 里哪一行实验?」, output: checkpoint 与论文实验设置 (数据集、超参、训练轮数) 的对应关系说明, 如与 README 描述有出入会明确记录下来
