# wizard (`mattpocock/skills/wizard`)

## comments

- user: 运维老哥, category: 妙用, comment: 生产割接我让它把 runbook 做成 wizard, 每个不可逆操作前自动加 confirm 卡点。半夜交接的人照着走, 再没人跳过备份步骤。
- user: 第一次用的新手, category: 坑, comment: 我一开始连改代码都让它做 wizard, 它直接自己干完没生成脚本。踩完才懂: 只有人必须手动的步骤(开网页、复制密钥)才找它。
- user: 创业公司 CTO, category: 妙用, comment: 新人入职配 Stripe+Sentry, 生成一次就提交进仓库、README 挂链接, 后来的人自己跑, 我没再陪配过环境。默认用完即删, 想复用要明说提交。
- user: 后端老兵, category: 注意, comment: 它不熟的第三方后台不会瞎编步骤, 会停下来反问我。第一次没提前开好控制台, 来回折腾。现在先备好后台和文档再启动, 一次过。
- user: 独立开发者, category: 坑, comment: 以为是无人值守脚本, 点完就走, 回来发现卡在等输入半小时。它每步都要你动手加回车确认, 留 15 分钟专注时间再跑。
- user: 技术组长, category: 注意, comment: 生成前它会列阶段清单让你增删排序, 我扫一眼就过了, 漏了两个 CI secrets。对着 workflows 里的 secrets.* 引用逐条核完再确认。
