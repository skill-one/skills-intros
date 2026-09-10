# refactor (`github/awesome-copilot/refactor`)

## comments

- user: 后端老兵, category: 妙用, comment: 我先让它扫出全文件的坏味道清单,再逐条处理,每改一小步跑测试并单独提交,哪步挂了能精确回退。
- user: 第一次重构的新手, category: 坑, comment: 没先补测试就让它重构核心函数,改完根本没法确认行为没变,只能人工逐行比对一晚上。记住:先写测试再动手。
- user: 测试工程师, category: 注意, comment: 它保证只改结构不改行为,正好配我的回归测试兜底。没测试覆盖的老模块,让它先补用例再动结构。
- user: 创业公司全栈, category: 坑, comment: 上线前一周想让它顺手大改核心代码,它反劝我:赶工期别重构。后来老代码稳稳扛过大促,幸好没动。
- user: 维护祖传代码的老哥, category: 启发, comment: 注释掉的旧代码我总舍不得删,它直接清掉并说 git 历史里找得回。才懂:历史交给版本库,别堆在代码里。
- user: 前端组长, category: 注意, comment: 想推倒重写的别找它,定位是渐进改良。适合每个迭代小步收拾一个模块,整库重写得换方案。
