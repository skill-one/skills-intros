# best-practices (`addyosmani/web-quality-skills/best-practices`)

## comments

- user: 独立开发者, category: 坑, comment: Best Practices 拿满分我就当安全了，结果依赖包里有已知 XSS——分数根本不扫依赖。现在都配着 npm audit 和 SecurityHeaders 一起跑。
- user: 接手祖传项目的前端, category: 注意, comment: 接手老项目先全局搜 polyfill.io：我 2019 年的项目就挂着它，2024 年这服务被劫持传播过恶意代码。删掉，polyfill 改成自托管。
- user: 后端转全栈兼运维, category: 坑, comment: 没逐个确认子域名都支持 HTTPS 就加了 HSTS，还挂在 HTTP 的后台子域被浏览器直接拒连，只能等缓存过期。先查全再上。
- user: 电商站前端负责人, category: 妙用, comment: 上 CSP 先发 Report-Only 头跑两周，逐条看违规报告，确认广告和统计脚本没被误伤再强制执行，灰度全程零翻车。
- user: 前端小组长, category: 妙用, comment: 把文末审计清单复制进上线 PR 模板逐项打勾，两次提前抓到重复 ID 和生产环境没关的 source map，比人肉回忆靠谱。
- user: 刚入行的前端新人, category: 启发, comment: 以前 console 报错只要页面能跑就不管。现在明白上线前控制台必须干净，再用全局错误监听接住异常上报，才算真正收尾。
