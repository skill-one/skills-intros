# codebase-design (`mattpocock/skills/codebase-design`)

## comments

- user: 后端架构评审老手, category: 妙用, comment: 评审时我先问:删掉这层,复杂度是消失、还是摊回 N 个调用方?上周照这标准砍掉三个只做转发的包装层,评审会再没人争口味。
- user: 第一次用的新手, category: 坑, comment: 一开始我把整个仓库丢给它说"帮我优化",得到一堆正确的废话。改成一次只指一个模块、附上接口和调用方,产出马上能落地。
- user: QA 出身的测试工程师, category: 启发, comment: 以前总求开发加测试钩子。按"接口即测试面"聊完才懂:想测到接口背后,是模块形状不对。现在改口让开发挪逻辑,不再要钩子。
- user: 独立全栈开发者, category: 注意, comment: 只有一个实现时别急着抽缝。我曾给所有存储抽 interface,等第二个数据源出现前,每对文件都是仪式。它的标准:两个适配器才算真缝。
- user: 爱用 AI 出方案的工程师, category: 妙用, comment: 别接受第一版接口。让它并行给 3 个思路迥异的方案,按"调用方要学多少、改动集不集中"挑,选中的常是第二三版,还看懂了取舍。
- user: DDD 老兵, category: 注意, comment: 我满口 DDD,总把 seam 当 boundary 说,半场各说各话——它明确拒收这个词。开场先对齐词汇:module、interface、seam、adapter。
