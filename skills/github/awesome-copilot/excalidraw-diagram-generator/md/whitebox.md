# excalidraw-diagram-generator (`github/awesome-copilot/excalidraw-diagram-generator`)

## whitebox

- 解析请求: 从自然语言中识别图类型 (流程图/思维导图/架构图/ER 图等 9 类)、关键元素、关系与复杂度
- 按类型抽取结构化信息: 不同类型有不同抽取清单, 如流程图抽"步骤+判断点", ER 图抽"实体+PK/FK+基数", 时序图抽"参与者+生命线+消息"
- 手写生成 Excalidraw JSON: 元素数组 (rectangle/ellipse/diamond/arrow/text) + 坐标、尺寸、颜色, 所有文字强制 fontFamily: 5 (Excalifont)
- 交付前校验: 检查 ID 唯一、坐标不重叠、字号≥16、箭头连接合理、JSON 有效、元素数 <20
- 保存为 .excalidraw 文件, 附打开方式 (excalidraw.com 拖拽或 VS Code 扩展) 与元素统计

- 关键词映射表定类型: "流程/步骤"→流程图, "数据库/实体"→ER 图, "交互/消息"→时序图等; 每类对应固定抽取清单和元素数上限 (如流程图步骤 ≤15)
- 纯本地 JSON 拼装, 不依赖外部模型 API: 布局用公式计算——关系图用网格公式 (√n 分列), 思维导图用极坐标 (三角函数环绕); ID 用时间戳+随机串生成; 元素过多时主动建议拆成多张图
- 可选外部工具: Python 脚本 add-icon-to-diagram.py / add-arrow.py, 用于注入云架构图标库 (.excalidrawlib, 需用户先从 libraries.excalidraw.com 下载并跑 splitter 脚本拆分); 脚本直接改文件, 避免把几百行图标 JSON 读入上下文
