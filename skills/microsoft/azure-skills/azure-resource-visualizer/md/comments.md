# azure-resource-visualizer (`microsoft/azure-skills/azure-resource-visualizer`)

## comments

- user: 接手祖传架构的后端, category: 妙用, comment: 接手没文档的资源组,让它跑一遍,图上连 App 设置指向 Key Vault、托管身份访问库这类隐藏连线都标出来了,一小时摸清全貌。
- user: 没配好环境的新手, category: 坑, comment: 没先 az login 就让它画图,查不到资源组一直卡着。先在终端登录 Azure、确认 az 命令能跑,再让它分析,一次就成。
- user: 管多资源组的运维, category: 注意, comment: 它只分析你选定的那个资源组,连到组外的库只在外部依赖备注里带一句。要画全局拓扑,得按组跑几遍再自己拼。
- user: 赶交付的架构师, category: 妙用, comment: 产出是带资源清单表和关系说明的 md 文件,小改就能当交接文档交差。50+ 资源时我会让它按层拆几张图,比一张大图好读。
- user: 管文档外发的安全工程师, category: 注意, comment: 图里连接串和密钥全是占位名,不含真值,文档可以直接外发。想看真值去门户查,别指望图里带出来。
- user: 用 Confluence 的 PM, category: 坑, comment: 图是 Mermaid 语法,我们老版 Confluence 不渲染,贴过去是一段代码。先确认平台支持,不支持就导出图片再贴。
