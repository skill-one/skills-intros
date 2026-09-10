# safe-refactor (`juliusbrussee/caveman/safe-refactor`)

## blackbox

**function**: 在不改变软件功能的前提下, 把你的代码收拾得更整洁、更有条理——功能照旧, 代码变好。

- input: 一个几千行的杂乱 Python 文件, 说「太乱了, 帮我整理」, output: 结构清晰后的同款代码文件, 跑起来的效果和之前完全一样
- input: 一段代码 + 一句话要求, 如「这几处重复的逻辑合并成一个」, output: 合并后的代码: 重复消失, 原来的调用处照常工作
- input: 一段代码 + 它的测试/运行命令, 要求「随便改, 但行为不能变」, output: 重构后的代码 + 同一条命令的运行结果, 证明改前改后行为一致
