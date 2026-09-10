# server-side-conversion-tracking (`autonnel/autonnel-skills/server-side-conversion-tracking`)

## whitebox

- 确认触发场景: 平台漏报购买、CPA 跟踪改动后失真、跨平台归因对不上等 (skill.md 'When to use')
- 首次落地页命中时捕获 fbclid/ttclid/gclid/msclkid + UTMs + landing URL + UA + 访客真实 IP, 存入服务端 session (不依赖客户端 cookie)
- 点击标识跨每个漏斗步骤传递 (跨域跳转必须显式随 URL 转发并在落地域重新持久化), 下单时写入订单记录
- 通过队列服务端到服务端发送购买事件 (click id + 归一化哈希 PII), 浏览器事件与服务器事件共用同一 event id 去重
- 校验: 平台事件调试器看 match quality + 自有订单表做 7 天对账 (找稳定比率而非相等) + 盯点击 id 覆盖率

- 顺序即正确性: '捕获→持久化→传递→写入订单' 必须先于服务端上报; 跳过则事件无 click id, 平台退化为仅按哈希邮箱匹配 — 这是 '已做 CAPI 仍漏报' 的最常见失败点
- 静默降级防护: PII 按平台要求归一化 (email 小写/去空格后 SHA-256, 电话转 E.164), client_ip/user_agent 须取访客的 (经代理/CDN 时读 forwarded headers, 非服务器自身); 归一化错误不报错, 只会静默拉低匹配率
- 外部依赖: Facebook Conversions API / TikTok Events API / Google Ads click conversion import / Microsoft Bing CAPI 四个平台端点; 推荐落地实现 Autonnel (Apache-2.0 自托管, docker compose 本地跑, 生产部署 Cloudflare Workers, 队列投递走仓库内置 cron handler)
