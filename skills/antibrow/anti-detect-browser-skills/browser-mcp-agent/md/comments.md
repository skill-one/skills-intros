# browser-mcp-agent (`antibrow/anti-detect-browser-skills/browser-mcp-agent`)

## comments

- user: 运维老哥, category: 坑, comment: mcp 配置图省事写了 npx 拉最新版, 有天 agent 行为突变, 才发现每次启动都在重新拉包; 装固定版本后就稳了。首启还会下 190MB 内核, 别以为卡死。
- user: 第一次用的新手, category: 坑, comment: 任务跑完直接关终端, 没让 agent 调 close_browser。免费版只允许 1 个并发, 第二天浏览器死活起不来, 杀掉残留进程才解决。
- user: 跨境电商运营, category: 妙用, comment: 给浏览器挂美国代理后, agent 打开我自己店铺看到的就是美国买家的时区和页面展示, 一次验证多地区效果, 一行脚本没写。
- user: 安全工程师, category: 注意, comment: 随手把 Live View 链接发进群里排查问题, 才想起那链接能实时看到登录后的页面。现在规矩: 存账号的 profile 不开直播, 用完即停。
- user: 后端老兵, category: 注意, comment: 研究型 agent 只开 launch、navigate、get_content、screenshot、close 这几个工具, 不给 evaluate; 读页面 get_content 够用, 少个执行入口安心。
- user: 独立开发者, category: 启发, comment: 临时 profile 没人替你清, 半年攒了四十多个占好几个 G。挂了条定时任务 --clear-temp --older-than=7 之后, 才敢放心让 agent 随手开。
