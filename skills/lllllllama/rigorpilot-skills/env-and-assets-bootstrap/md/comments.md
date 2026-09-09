# env-and-assets-bootstrap (`lllllllama/rigorpilot-skills/env-and-assets-bootstrap`)

## comments

- user: 复现论文的研二学生, category: 坑, comment: 一开始只丢 repo 路径让它搭环境,输出太空泛没法用。后来把 README 安装段原文一起贴给它,给出的 conda 命令才能直接照抄。
- user: 跑模型的算法工程师, category: 妙用, comment: 把它标出的未解决依赖风险当开跑前的预检清单:提前下好 checkpoint 和数据集,免得训到一半才发现缺权重文件。
- user: 实验室服务器管理员, category: 注意, comment: 它默认 conda 优先、策略保守,我们机器习惯 Docker+pip,得提前说清约束;缓存目录也让它指到独立盘,免得撑爆 home。
- user: 第一次复现的新手, category: 坑, comment: 以为它能帮我挑哪个 repo 值得复现、还替我读论文补细节——都不行,它只管选定目标后的环境与数据路径准备。
- user: 复现过十几个模型的老手, category: 启发, comment: 以前上来就 pip install 一把梭,失败多半栽在环境。现在先让它出 setup 笔记、写清资产路径假设,再动手跑,返工少多了。
- user: 赶 deadline 的实习生, category: 注意, comment: 它产出的是候选命令和 setup 笔记,不会替你把环境装好,命令要自己跑。好处是风险提前标出,比裸读 README 省心。
