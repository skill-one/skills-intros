# resolve-merge-conflicts (`warpdotdev/common-skills/resolve-merge-conflicts`)

## comments

- user: 开源库维护者, category: 妙用, comment: rebase 卡在 30 多个文件, 先看汇总里每个文件的冲突块数, 改动日志、生成物直接 checkout --theirs, 真正要动脑的只剩 4 个, 半小时收工。
- user: 第一次解冲突的新手, category: 坑, comment: 删完 <<<<<<< 标记以为完事了, 没 git add 就继续 rebase, 一直报未解决。删标记不等于解决, 必须 add 进暂存区。
- user: 运维老哥, category: 注意, comment: modify/delete 冲突的文件里根本没有 <<<<<<< 标记, 我 grep 一圈啥也没找到, 白忙一场。这类要看汇总里 index 各阶段的预览。
- user: 后端老兵, category: 注意, comment: 它只给 ours/base/theirs 和文本 diff, 不会替你判断哪边逻辑对。两边同时改了同一函数时, 压缩视图不够就老实多读上下文。
- user: 前端工程师, category: 妙用, comment: 锁文件冲突几千行, 用 --context 3 --max-lines 60 输出立刻可控; 明知只要一端的生成物, 看完汇总直接 checkout, 文件都不用打开。
- user: 曾被大冲突吓退的人, category: 启发, comment: 以前十个冲突文件全打开来回跳, 越解越乱。现在严格一次一个, 解完 add 再看下一个, 心智负担小很多, 很少再解错回滚。
