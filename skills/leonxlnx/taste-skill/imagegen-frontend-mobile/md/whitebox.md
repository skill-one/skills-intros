# imagegen-frontend-mobile (`leonxlnx/taste-skill/imagegen-frontend-mobile`)

## whitebox

- 解析请求: 先定平台模式 (iOS / Android / 跨平台), 再按用户关键词重调基线参数 (如 "clean"→降密度、"fintech"→强信任感)。
- 锁定设计圣经: 多屏任务在生成前先固定整套设计系统——配色、字体、间距、圆角、图标风格、样机框样式。
- 直接出图: 按请求数量 1:1 生成屏幕图 (禁止只给文字方案), 默认装进干净的手机样机框, 内容仍是主角。
- 流程与一致性自检: 屏幕须构成可信的 app 流程 (如 onboarding→auth→home), 且全部停留在同一产品世界内不漂移。
- 仅交付图像: 输出只有屏幕图/细节图/流程图, 明确不写 SwiftUI/React Native/Flutter/HTML 任何代码。

- 基线配置适配 (解析/转换): 内置约 22 个命名参数 (DESIGN_VARIANCE、VISUAL_DENSITY、TEXT_READABILITY_PRIORITY=10 等) 作为默认值, 随用户语义动态重映射, 而非套死固定模板。
- 规则门禁 (校验层): 一组硬规则把关每次输出——屏幕数不得缩水 (要 5 屏就出 5 图)、细节不清时禁止裁剪旧图必须重新独立生成、文字必须保持可读、样机框均匀整洁且内容优先。
- 无外部依赖声明: SKILL.md 未绑定任何具体的图像生成 API、库或外部工具, 仅声明 "generates images only", 即依赖底层模型自身的图像生成能力。
