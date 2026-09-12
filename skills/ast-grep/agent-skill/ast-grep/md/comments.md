# ast-grep (`ast-grep/agent-skill/ast-grep`)

## comments

- user: 后端老兵, category: 妙用, comment: 最妙的是反向匹配：找没有 try-catch 的 async 函数。正则根本表达不了"缺少某物"，我用 not + has 写一条规则扫全库，揪出三十多个裸奔的 await。
- user: 第一次用的新手, category: 坑, comment: 写了 has: pattern: await $X 却一条都匹配不到，查了一小时以为是语法错。其实是漏了 stopBy: end，加上立刻出结果。规则没命中先查这个，别急着怀疑自己。
- user: 运维老哥, category: 坑, comment: bash 里用 --inline-rules 直接写 $ARG，被 shell 当变量展开成空串，匹配永远是 0。写成 \$ARG，或者整条规则用单引号包住，我吃过这亏。
- user: 前端开发, category: 注意, comment: 别凭直觉猜 kind 名：箭头函数不叫 function_declaration，所以我的规则一直漏匹配。先跑 --debug-query=cst 看解析器眼里的结构，照抄 kind，省大半调试时间。
- user: 技术负责人, category: 妙用, comment: 把它当评审前的自动检查：团队规定 hooks 不能写在 if 里，我写了条规则放进 CI，不合规的 PR 直接标红，比人肉盯靠谱得多。
- user: 测试工程师, category: 启发, comment: 用熟后发现大部分 grep 撞墙的需求都能翻译成规则："类方法里的 console.log"、"没判空就取属性"。现在固定流程是先写个小样例文件验证规则，能命中再扫全库。
