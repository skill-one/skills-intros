# wonda-cli (`degausai/wonda/wonda-cli`)

## comments

- user: 第一次用的新手, category: 坑, comment: 以为充了余额就能用,结果全报 403 paid_plan_required。余额代替不了订阅,免费账号没有产品权限,得先去 wonda.sh/account 订阅再充。
- user: 做短视频配音的博主, category: 坑, comment: 克隆完声音闲置两周,7 天没跑 TTS 自动过期,又花 $1.50 重克隆。现在每周跑一次语音刷新有效期,voice list 的 expiresInDays 能提前看到快过期。
- user: 三人小团队主理人, category: 注意, comment: 成员想充团队钱包,CLI 报错才知 org 钱包只有 admin 在网页端能充。更易误会的是:wonda topup 永远充的是个人钱包,想充团队别指望这条命令。
- user: 写脚本跑批的后端老兵, category: 妙用, comment: 写 cron 时发现 --jq '.outputs[0].media.url' 一行拿到下载链接,stdout 永远干净;公告走 stderr,定时任务嫌吵就加 WONDA_NO_UPDATE_CHECK=1,日志清爽。
- user: 管五个平台号的社媒运营, category: 妙用, comment: 以前从 Chrome 扒 cookie 粘进去,隔三差五被平台要验证。改用 wonda wab login 原生登录,session 在反指纹浏览器里铸出,指纹一致,再没触发风控。
- user: 同时接三个客户的独立运营, category: 启发, comment: 每个任务先 wonda use --project 客户名,月底 usage --project 一拉,给谁干活花了多少一目了然。项目要先 create,打错字报 unknown_project,正好防串账。
