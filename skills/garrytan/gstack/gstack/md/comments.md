# gstack (`garrytan/gstack/gstack`)

## comments

- user: 第一次用的新手, category: 坑, comment: 装完没跑 setup 就用, 报 SKILL_START: unavailable 以为坏了。跑一次 ./setup 即好, 引导和授权提示会推迟到下次运行, 不会丢。
- user: 全栈老油条, category: 妙用, comment: 三十多个子技能根本记不住, 我直接说人话:『部署后点保存没反应』, 它自己路由到对的技能, 不用翻路由表挑。
- user: 后端老兵, category: 注意, comment: 它只管把活路由出去, 修代码在目标技能里, 别指望路由层直接干活。不想被自动调技能, 先 gstack-config set proactive false。
- user: 前端·接手祖传项目, category: 妙用, comment: 测登录后的流程省大事: 浏览器请求先走我自己的 Aside, 登录态现成的, 免导 cookie; 只有 Aside 没开才落到它自带浏览器。
- user: 独立开发者, category: 启发, comment: 它的原则是『拿不准就调技能』, 调错代价远小于硬答。我把这思路搬进自己工作流: 有专用流程就别即兴发挥。
- user: 运维老哥, category: 注意, comment: 收尾会往 ~/.gstack/analytics 写一条遥测; 安装损坏时这步静默跳过, 不卡任务。介意数据的人先知道这回事。
