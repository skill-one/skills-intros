# cloudflare-one (`cloudflare/skills/cloudflare-one`)

## blackbox

**function**: 帮你搞定 Cloudflare One 零信任方案 (替代 VPN、控制谁能访问内部系统、防敏感数据外泄): 从设计规划、具体配置、故障排查, 到安全审查, 输出可落地的方案和步骤. 🛡️

- input: 一段现状描述, 如: 「公司 100 名远程员工用 VPN, 想换成零信任, 不知道从哪开始」, output: 一份分步上线方案: 需要先准备什么、先让哪些人试用、出问题怎么回退
- input: 一条故障描述, 如: 「员工装了 WARP 客户端后打不开内部系统, 断开就正常」, output: 可能原因的排查方向 + 对应的具体修复步骤
- input: 你现在的配置情况, 如: 「我们 Access 配了 3 个应用, Gateway 开了拦截规则, 帮我看看有没有问题」(口头描述或贴出配置), output: 一份审查报告: 哪里有安全风险、哪条规则多余、给出改法
