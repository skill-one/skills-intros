# apify-ultimate-scraper (`apify/agent-skills/apify-ultimate-scraper`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没配 APIFY_TOKEN 就直接跑，报 auth 错误卡了半天。先去 console 的 integrations 页面生成 token，用 apify login 或环境变量配好再动手。
- user: 后端老兵, category: 坑, comment: stderr 里有进度日志，不加 2>/dev/null 重定向，输出混在一起导致 --json 解析直接挂。指南强调了，我头一回还是忘了。
- user: 数据分析师, category: 妙用, comment: 同一个数据集先 --format json 看样，确认字段没问题再 --format csv 导出，不用重跑抓取，对账和交付都很方便。
- user: 跨境电商运营, category: 注意, comment: 按事件付费（PPE）的 Actor 每跑一步都扣钱，大批量抓之前让它先读 gotchas 确认计费方式，不然一次误跑烧掉不少额度。
- user: 外贸BD, category: 妙用, comment: 我说'抓谷歌地图上柏林咖啡馆老板的联系方式'，它自己挑对 Actor，还按线索工作流串了提取和整理两步，省了我一下午手抄。
- user: 品牌运营, category: 启发, comment: 以前盯竞品价格靠人肉刷新，现在描述需求让它选工具、跑完存成 CSV，我从'找数据的人'变成了'提需求的人'。
