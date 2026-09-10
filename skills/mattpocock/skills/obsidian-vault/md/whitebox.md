# obsidian-vault (`mattpocock/skills/obsidian-vault`)

## whitebox

- 识别用户意图: 在 vault 中搜索、新建还是整理笔记
- 用 find / grep (或 Grep/Glob 工具) 在 /mnt/d/Obsidian Vault/AI Research/ 上执行检索 (按文件名或按内容)
- 新建笔记: Title Case 命名 → 内容按"学习单元"撰写 → 底部追加 [[wikilinks]] 关联笔记
- 整理/聚合: 汇总相关主题为 Index note (纯 [[wikilinks]] 列表), 返回结果

- 文件系统即数据库: 检索完全依赖 bash 的 find (按文件名) 和 grep -rl (按内容), 或直接对 vault 路径调用 Grep/Glob 工具, 无索引库、无外部 API
- 链接即图谱: 全库使用 Obsidian [[wikilinks]] 语法; 反向链接 (backlink) 靠全库 grep 搜索 "[[Note Title]]" 字符串实现; Index note 本质就是一组 wikilinks
- 约定优先于结构: 扁平目录 (不建文件夹)、Title Case 命名、序列笔记用层级编号——规范由执行时遵守, 无工具级校验
