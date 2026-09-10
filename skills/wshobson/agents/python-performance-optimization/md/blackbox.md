# python-performance-optimization (`wshobson/agents/python-performance-optimization`)

## blackbox

**function**: 给跑得慢、卡、吃内存的 Python 代码「体检 + 治病」: 告诉你慢在哪, 并把代码改快改省。

- input: 一个运行很慢的 Python 脚本文件路径, output: 一份分析报告, 指出最耗时的几处代码, 并给出改快后的代码和前后耗时对比
- input: 一段处理大数据时内存爆掉的 Python 代码, output: 改写后的代码, 内存占用明显下降, 并附改法说明
- input: 一段代码 + 描述: 「这个循环越跑越慢, 怎么回事?」, output: 问题定位 (哪行是瓶颈、为什么), 加上对应的优化版本代码
