# caveman-help (`juliusbrussee/caveman/caveman-help`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我以为 /caveman-help 能开启原始人模式，结果只弹出说明卡，回复语气照旧。它是纯查表工具，想真生效要另敲 /caveman。
- user: 每天开十几个会话的重度用户, category: 坑, comment: 模式只在当前会话有效，新开会话就退回默认 full。后来 export CAVEMAN_DEFAULT_MODE=ultra，从此不用每次手动切。
- user: 运维老哥, category: 注意, comment: 环境变量优先级高于 config.json。我在配置文件里改默认模式一直不生效，排查半天，是 shell 里残留的旧 export 盖住了它。
- user: 中文内容创作者, category: 妙用, comment: 本来怕中文被翻成英文，实测只压语气不换语言，代码和报错原文原样保留。wenyan 模式写周报，短还带点古意。
- user: 技术文档写手, category: 注意, comment: 拿它压 Python 和 txt 没反应——compress 只吃 .md 文件。压完省约 46% 输入 token，长文档喂 AI 前先过一遍很值。
- user: 开源维护者, category: 启发, comment: 它逼我把提交信息砍进 50 字符还能说清改动。回头看以前的三行提交，一半是废话——简洁是约束出来的，不是天赋。
