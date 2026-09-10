# internal-comms (`anthropics/skills/internal-comms`)

## whitebox

- 收到内部沟通写作请求 (3P 更新 / 公司简报 / FAQ / 状态报告 / 领导层汇报 / 项目更新 / 事故报告等), 先识别通信类型
- 按类型到 examples/ 目录加载对应指南: 3p-updates.md、company-newsletter.md、faq-answers.md, 未明确命中则加载 general-comms.md
- 遵循所加载指南中关于格式、语气 (tone)、内容收集 (content gathering) 的具体指令
- 按指南产出内部沟通文稿

- 类型路由: 请求类型 ↔ 指南文件一一映射 (3P→3p-updates.md, 简报→company-newsletter.md, FAQ→faq-answers.md); general-comms.md 是未匹配类型的兜底分支
- 指南驱动生成: 格式 / 语气 / 素材规则全部以加载的指南文件为准, 不自行发挥
- 无匹配即澄清: 类型对不上任何指南时, 向用户追问格式或更多上下文, 而非猜测输出
- 外部依赖: 仅 skill 自带的 examples/ 目录下 4 个 Markdown 指南文件, 不调用其他外部工具、库或模型 API
