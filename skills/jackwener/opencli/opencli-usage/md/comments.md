# opencli-usage (`jackwener/opencli/opencli-usage`)

## comments

- user: 第一次用的新手, category: 坑, comment: 装完直接跑 COOKIE 命令, 报浏览器连不上, 折腾半天才发现漏装了 Chrome 扩展。先跑 opencli doctor, 全绿再开工, 能省一小时。
- user: 自动化脚本作者, category: 注意, comment: 脚本放 cron 里跑, 输出莫名变 yaml 把解析搞挂了。非终端环境默认输出就是 yaml, 显式加 -f json 才稳。
- user: 后端老兵, category: 妙用, comment: 我把 opencli list -f json 当活文档喂给脚本, 不再硬编码命令表。适配器每周都在加, 写死的清单会过期, 这个查询不会。
- user: 运维老哥, category: 坑, comment: npm 装完一跑就报错很迷惑, 查了半天是 Node 版本低于 21。装之前先 node -v 看一眼, 别到运行时才发现。
- user: 电商运营姑娘, category: 妙用, comment: 让 AI 帮我抓数据, 本以为要交密码, 结果 COOKIE 类命令直接复用我 Chrome 里已登录的会话, 全程没碰密码, 敢放心用了。
- user: 照旧教程上手的人, category: 坑, comment: 跟着三个月前的旧教程敲 opencli explore, 报命令不存在——这条已被移除。现在抓接口要用 opencli browser network --detail。
