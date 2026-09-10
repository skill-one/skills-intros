# run-train (`lllllllama/rigorpilot-skills/run-train`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我以为它会顺手把环境装好, 结果依赖没装它只把 run 记成 blocked 不动。先自己装好依赖再叫它。
- user: 管实验室显卡的管理员, category: 妙用, comment: 先让它跑几分钟启动验证, 确认不报错再开全量训练, 之后再没浪费过一整晚的卡。
- user: 做推理部署的算法工程师, category: 注意, comment: 它只管训练这一段, 推理评估、装环境、调实验都不归它, 喂错任务它不接。
- user: 接手师姐代码的博士生, category: 妙用, comment: 接手师姐的活只看 train_outputs 文件夹: 命令、日志、checkpoint、指标都在, 我照着就把训练续上了。
- user: 复现过十几篇论文的老研究僧, category: 启发, comment: 以前命令和 seed 全靠翻终端历史, 现在每步证据都落在标准文件里, 我开始照这个格式管自己的实验。
- user: 被导师催复现的研二学生, category: 注意, comment: 喂任务要给四样: 训练目标、能跑的命令、环境假设、跑法(启动验证/短跑/全量/续跑), 缺一样它先不动。
