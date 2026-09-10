# json-canvas (`kepano/obsidian-skills/json-canvas`)

## whitebox

- 读取目标 .canvas 文件 (或新建空结构 {"nodes": [], "edges": []}) 并解析为 JSON
- 为每个新元素生成 16 位十六进制唯一 ID, 按节点类型 (text/file/link/group) 写入必需字段与坐标尺寸
- 添加 edges, 用 fromNode/toNode 指向已存在的节点 ID, 可选设置 fromSide/toSide/label/color
- 写回文件并校验: JSON 可解析、ID 全局唯一、所有边引用都能解析到已有节点

- 纯 JSON 文件操作, 遵循 JSON Canvas Spec 1.0 (jsoncanvas.org, 唯一外部规范依赖): 顶层仅 nodes/edges 两个数组, 数组顺序即 z-index 层叠顺序; 文本节点内容支持 Markdown, 换行必须写 \n 而非字面 \n
- ID 生成: 16 位小写十六进制字符串 (64-bit 随机值), 且必须在节点与边的全部 ID 间保持唯一
- 校验清单: ① 所有 id 唯一 ② 每条边 fromNode/toNode 引用真实存在 ③ 各类型必需字段齐全 (text/file/url) ④ 枚举合法——type ∈ {text,file,link,group}、side ∈ {top,right,bottom,left}、end ∈ {none,arrow}、color 为预设 "1"-"6" 或十六进制
