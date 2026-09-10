# design-md (`google-labs-code/stitch-skills/design-md`)

## whitebox

- 定位数据源: 通过 Stitch MCP Server 发现工具前缀, 若未提供 ID 则用 list_projects / list_screens 逐级查找, 再以 get_screen / get_project 拉取屏幕元数据 (截图 URL、HTML 下载地址、尺寸) 和项目 designTheme
- 下载资产: 用 web_fetch 抓取 htmlCode.downloadUrl 的 HTML/CSS 源码 (截图可选)
- 解析提取: 从 HTML 中解析 Tailwind 类名、自定义 CSS 与组件模式, 从截图/结构提炼氛围, 从代码提取色板 hex、圆角、阴影、字体等技术 token
- 语义化转换: 把技术值翻译成设计语言并附精确值 (如 rounded-lg → "Subtly rounded corners"), 并推导各元素的功能角色 ("why" 而非 "what")
- 落盘输出: 按固定五节结构 (主题氛围 / 色板角色 / 字体规则 / 组件样式 / 布局原则) 用 Write 生成 DESIGN.md

- 检索依赖: 全部项目数据来自 Stitch MCP Server (stitch* 工具命名空间); 参数约定——projectId/screenId 只传数字 ID, 项目级元数据走完整路径 projects/{id}
- 翻译引擎: 核心机制是"技术值 → 物理化描述"的映射, 如 rounded-full → Pill-shaped、rounded-none → Sharp squared-off edges、微弱阴影 → Whisper-soft diffused shadows; 颜色按 "描述性名称 + hex + 功能角色" 三元组记录, 而非笼统的 "blue"
- 输出约束: 结果强制对齐 DESIGN.md 五节模板, 语言仅用描述性设计术语 (禁止裸写 rounded-xl 这类技术 jargon), 精确值 (hex/pixel) 必须以括号形式跟随描述; 用到的其他工具: Read、Write、web_fetch
