# obsidian-cli (`kepano/obsidian-skills/obsidian-cli`)

## comments

- user: 自由撰稿人, category: 坑, comment: Obsidian 没开着就跑命令会直接失败, CLI 不会帮你启动它。我的定时归档脚本连挂三天才发现, 现在脚本开头先确认 app 在运行。
- user: 双库重度用户, category: 注意, comment: 命令默认打给最近聚焦的库。我有工作和写作两个库, 不加参数时笔记经常进错库, 后来脚本里第一个参数都固定写 vault=。
- user: 第一次用的新手, category: 坑, comment: 我拿 file= 追加内容, 结果它像 wikilink 只按文件名找, 库里有两个同名笔记就追加错了地方。有同名文件时改用 path= 写从根开始的全路径。
- user: 写自动化脚本的前端, category: 妙用, comment: create 默认会打开文件抢焦点, 批量建笔记时加上 silent overwrite, 建完完全不打扰; 内容里用 \n 换行, 一条命令就能写入多行模板。
- user: 插件开发新人, category: 妙用, comment: 改完代码 plugin:reload → dev:errors 查报错 → dev:screenshot 看效果, 全程不用切窗口, 一轮十几秒, 比手动重启插件快太多。
- user: 后端老兵, category: 启发, comment: eval 里能跑 app 的完整 API, CLI 没覆盖的批量操作我用一句 JS 搞定, 存成 shell 别名后, Obsidian 就被我当笔记数据库在用了。
