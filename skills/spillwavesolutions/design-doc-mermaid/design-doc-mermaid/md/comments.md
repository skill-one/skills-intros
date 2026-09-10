# design-doc-mermaid (`spillwavesolutions/design-doc-mermaid/design-doc-mermaid`)

## comments

- user: 后端老兵, category: 妙用, comment: 把 Spring Boot 项目整个丢给它，架构图、接口时序图、业务流程图一次出三张，@RestController 等注解都能识别，周会汇报直接用。
- user: 第一次用的新手, category: 坑, comment: 直接把 mermaid 代码贴进 Confluence，同事打开看到的是一段灰底代码。这个场景必须让它导出 PNG 再上传。
- user: 运维老哥, category: 注意, comment: GitHub wiki 上 C4 架构图偶尔渲染不出，别死磕语法，直接让它降级成 flowchart 画，效果一样还能正常显示。
- user: 技术文档工程师, category: 妙用, comment: 接手祖传文档先让它全量扫描：一条命令列出所有 mermaid 块并逐个校验，坏图当场现形，省去逐页肉眼排查。
- user: 产品经理, category: 启发, comment: 让它给节点加 emoji（👤🌐💾）后，评审会上非技术同事第一次看懂了架构图，讨论直接聚焦在业务而不是术语上。
- user: 前端全栈, category: 注意, comment: 图会存到 ./diagrams/ 目录、文档里走相对路径引用。markdown 挪位置时记得连目录一起带走，否则图片全裂。
