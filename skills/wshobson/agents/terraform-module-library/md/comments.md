# terraform-module-library (`wshobson/agents/terraform-module-library`)

## comments

- user: 平台工程负责人, category: 启发, comment: 以前各团队一个 VPC 三种写法. 规定全走这套模块库后, PR 只审参数不审资源代码, tags 从一个 map 统一传入, 成本报表再没缺过标签.
- user: 被销毁过资源的运维, category: 坑, comment: subnet 用 count+列表, 删一个网段后 count.index 整体位移, 后面的子网全被计划销毁重建. 换成 for_each 拿 CIDR 当 key, 删谁只动谁.
- user: 第一次跑 Terratest 的新手, category: 注意, comment: tests 里的 Terratest 是真在云上建资源再销毁, 我裸跑一次月底多了几十刀账单. 先用最小规格的 examples 跑, 并确认凭证指向测试账号.
- user: 云架构师, category: 妙用, comment: 在 variables 里加 validation 正则, 同事把 CIDR 写成 /33 时 plan 直接被拦下, 不用等 apply 跑一半报错再回滚. 现在我每个模块输入都加校验.
- user: 接手老项目的后端, category: 坑, comment: versions.tf 没钉 provider 版本, 我本地 init 拉到新版, plan 出一堆莫名 diff. 钉死版本后谁跑都一致, 接手项目先检查这个文件.
- user: 多云迁移工程师, category: 注意, comment: 目录按 aws/azure/gcp 分开, 别指望一套模块通吃云. 我以为 vpc 模块改改参数就能上 azure, 结果两云字段完全不同, 老实各写一份, 业务层再复用.
