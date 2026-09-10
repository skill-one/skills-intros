# anti-detect-browser (`antibrow/anti-detect-browser-skills/anti-detect-browser`)

## comments

- user: 爬虫工程师, category: 妙用, comment: 计费封的是并发浏览器数,不是身份数。我给每个爬虫任务发一个临时 profile,一次只开五个,本地攒了几百个身份,没多花一分钱。
- user: 第一次用的新手, category: 坑, comment: 想测手机页面,给旧 profile 的 launch 加了 deviceType:'android',跑完还是桌面——机型在创建时就冻结了,只能新建 profile 才生效。
- user: Docker 运维老哥, category: 注意, comment: 镜像构建期先跑一次空 launch 预热内核,把 ~/.anti-detect-browser 挂成卷,否则生产首启现场拉 190MB 必超时;它每天还要联网换令牌,内网隔离机跑不了。
- user: 多账号运营, category: 坑, comment: 临时和正式是两套命名空间,我两边各建了同名 profile,登录状态互不相通,白登两遍。临时 profile 也不会自动删,里面全是活 cookie,记得定期跑 clearTemporaryProfiles。
- user: 风控工程师, category: 妙用, comment: 拿它给自己站的反爬做回归:persona 建好就冻结,改一版策略就重跑 CreepJS 对比分数。报 bug 用 redacted_args() 导命令行,代理凭据进不了日志。
- user: 用免费额度的独立开发者, category: 注意, comment: 免费 key 传 realFingerprint:true 会直接报错拒绝,不是悄悄降级,别以为坏了,用 tags 筛指纹就够;安卓模式包里自带三台真机数据,免费 key 也能用。
