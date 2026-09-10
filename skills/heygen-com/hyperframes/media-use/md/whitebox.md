# media-use (`heygen-com/hyperframes/media-use`)

## whitebox

- 把任务映射到一个媒体类型, 只读取对应的那份 reference 文件 (如 resolve → references/resolve.md)
- 首次运行: 安装并登录 heygen CLI, 用 resolve.mjs --doctor 自检通过
- resolve.mjs 先用 --candidates 列出可复用资产并自行判断是否合适, 不合适才按 type 走解析/生成
- 返回单行 resolved <id> → <path>: 得到冻结的本地文件 + ledger 记录, 全部搜索噪音留在磁盘不上上下文
- 视觉类需求改走 hyperframes media-treatment: 检查真实媒体 → 应用处理 → 确定性落盘

- 单一动词解析协议: node <SKILL_DIR>/scripts/resolve.mjs --type/--intent/--project, 契约是「一行结果、噪音留磁盘」, 环境靠 --doctor 校验
- 复用优先 + 目录→生成级联: bgm/sfx/image 查 HeyGen catalog (bgm 10k+ 曲目、image 75k+ 向量, sfx 另有内置 19 文件库); logo 按 svgl → simple-icons → GitHub 头像 → favicon 级联且永不重绘; voice 走 HeyGen TTS (可退本地 Kokoro); lut 只用用户提供或明确选定的 .cube 文件
- 真实媒体校验 + 确定性持久化: 对实际 <img>/<video> 做证据检查 (视频只看一张早/中/晚 contact sheet), 经 hyperframes media-treatment --capabilities --json 选一个效果族, 普通校正/打磨只持久化 preset/adjustment JSON; 外部依赖: heygen CLI、hyperframes CLI、Kokoro TTS
