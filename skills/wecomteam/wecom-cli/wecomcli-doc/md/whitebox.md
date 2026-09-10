# wecomcli-doc (`wecomteam/wecom-cli/wecomcli-doc`)

## whitebox

- 触发判定: 用户消息出现「doc/docx/word/在线文档」等强类型词或 doc.weixin.qq.com/doc/ 链接才进入本技能, 泛化说法 (如"新建文档/写文档") 转交 wecomcli-smartpage
- 获取 docid: 优先从 URL 中 /<type>/ 后、? 前的段落解析; 没链接则用 wecomcli-doc-manage 按名称搜索; 用户直接给了 docid 就直接用; 禁止自造
- 查参考再拼命令: 按接口路由表先用 read 工具读完对应 references/*.md, 再构造 wecom-cli doc 命令 (import / contents get / append / overwrite)
- 执行并取回内容: 返回 content 字段较短时直接展示; 内容较长时自动落盘, 拿 file_path 再用 Read 工具读取后展示
- 结果展示: 只输出 [文档名](文档URL) 链接, 不向用户暴露 docid

- 写入语义裁定: 「写入/记录/补充」等中性动词默认 append (追加不破坏原文); 仅出现「覆盖/重写/替换/清空重写」等强语义词才走 overwrite
- 新建走两步转换: 统一先生成本地 .docx 文件, 再用 wecom-cli doc import 导入为在线 doc, 且 file_name 参数须与文档标题一致
- 外部依赖: 必须存在 wecom-cli 命令行二进制 (前置 bins 检查), 且执行任何命令前先过 wecomcli-shared 公共前置检查; 读取支持 text/markdown/ooxml 三种内容格式; 按名称找文档时依赖 wecomcli-doc-manage 搜索
