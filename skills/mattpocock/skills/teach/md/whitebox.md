# teach (`mattpocock/skills/teach`)

## whitebox

- 读状态: 解析工作区文件 — MISSION.md (学习动机)、learning-records (学习进度)、NOTES.md (偏好), 据此算出「最近发展区」, 定本次教什么
- 取知识: 只从 RESOURCES.md 登记的高质量可信资源获取知识, 明确不信任自身参数记忆
- 造课程: 复用 ./assets/ 已有组件, 生成一节自包含 HTML 课程到 ./lessons/000N-*.html — 一次只教一个紧扣使命的点, 短而完整
- 沉淀: 把要点压缩进 reference/ 速查文档, 并追加一条新学习记录 (编号递增)
- 交付: 用 CLI 命令打开课程文件给用户, 并提醒可随时向 agent 追问

- 状态机 = 文件系统: 教学是多会话有状态的, 全靠目录内文件承载 — MISSION.md 未填时第一动作是反问用户动机; learning-records 按 0001- 编号递增, 是计算教学切入点 (ZPD) 的唯一依据
- 构建管线 = 资源 → 组件 → 课程: ./assets/ 存可复用组件 (共享样式表是每个工作区首个必建组件), 禁止内联未来课程会重复的代码; 格式遵循本地规范文件 (MISSION-FORMAT.md / RESOURCES-FORMAT.md / LEARNING-RECORD-FORMAT.md); 教学顺序固定为「先知识、后技能(交互反馈回路)」
- 校验 = 即时反馈 + 防泄露: 技能通过反馈回路训练 (测验/实操, 反馈越即时越好); 测验各选项字数一致, 防止格式暗示答案; 课程论断附资源引用链接保证可信。外部依赖: 仅「CLI 命令打开课程文件」一项, SKILL.md 未指定任何外部库、搜索引擎或模型 API
