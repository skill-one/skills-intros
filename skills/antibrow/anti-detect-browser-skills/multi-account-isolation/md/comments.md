# multi-account-isolation (`antibrow/anti-detect-browser-skills/multi-account-isolation`)

## comments

- user: 跨境电商运营, category: 坑, comment: 同一个 profile 名,一处脚本传了 temporary: true 另一处没传,等于一个名字跑两个身份,表现像天天掉登录。上线前统一这个值,能省半天排查。
- user: 第一次用的新手, category: 坑, comment: 资料夹名是 profile 的 id,不是显示名。我改完名把旧文件夹当垃圾删了,人设没了,canvas 哈希每次重启都变。认准文件夹里的 profile.json 再动手。
- user: 风控测试工程师, category: 妙用, comment: 把检查 1/3/7(时区、canvas 哈希、出口 IP)接进 CI 跑 liarjs,代理商悄悄把两个美区出口挪进同一 /24,当周就被拦下,没等到账号出事。
- user: 运维老哥, category: 注意, comment: 内核每天要联网换 license token,没有离线模式,要求零出网的机器别硬上。报障前先跑 antibrow info 和 redacted_args(),密钥自动打码,可直接贴。
- user: 多账号工作室老板, category: 启发, comment: 11 项检查全绿,账号照样被限,最后发现是两张卡挂在同一支付主体。浏览器层干净≠平台当你是两个人,付款方式、联系方式、行为节奏得另查。
- user: 指纹检测爱好者, category: 注意, comment: 别在一个 profile 里刷新指纹图新鲜,重启后 canvas 哈希一动,CreepJS 反而标记异常。稳定本身才是要求,人设冻结后就别再动它。
