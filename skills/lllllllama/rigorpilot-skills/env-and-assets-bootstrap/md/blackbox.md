# env-and-assets-bootstrap (`lllllllama/rigorpilot-skills/env-and-assets-bootstrap`)

## blackbox

**function**: 在你想跑通/复现一个深度学习开源项目之前,我给你一份「开跑前准备清单」:该装什么环境、数据和模型文件从哪下、放哪、还缺什么。

- input: 一个 GitHub 仓库路径 + 你想复现的目标(如「复现这篇论文的 Table 1」), output: 一份准备清单:可逐条复制的环境安装命令、数据集和预训练模型(训练好的模型文件)的下载来源与存放位置建议、尚未解决的风险列表
- input: 仓库路径 + README 里的安装/使用说明, output: 整理好的搭建步骤笔记:保守稳妥的安装命令(优先避免环境冲突)、checkpoint(训练好的模型存档)和数据集的路径规划、缓存目录位置提示
- input: 仓库路径 + 你的机器限制(如「只有 CPU 没有 GPU」「Windows 系统」), output: 按你的限制调整后的搭建方案 + 开跑前风险清单:哪些包可能版本冲突、哪些数据/模型还缺、哪些路径需要你先确认
