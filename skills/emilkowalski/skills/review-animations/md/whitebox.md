# review-animations (`emilkowalski/skills/review-animations`)

## whitebox

- 仅接受动效代码审查请求 (模型不自动触发, 须用户显式调用); 若请求审查非动效代码, 直接拒绝并指向通用审查技能。
- 将 diff 中每个动画逐条对照'十条不可妥协标准'测量: 动效必要性、频率匹配度、缓动曲线、时长 (<300ms)、缩放原点、可中断性、GPU-only 属性、无障碍、进/出非对称时序、风格一致性。
- 扫描'即时升级'触发点 (如 transition: all、scale(0)、UI 上用 ease-in、高频/键盘操作带动画、布局属性动画等), 见到即硬标。
- 需要精确数值 (曲线、时长、弹簧配置) 时, 按需加载外部规则目录 STANDARDS.md 取确切值并引用, 不凭感觉估算。
- 按强制格式输出: Part 1 发现表格 (Before / After / Why, 逐行一条问题) → Part 2 按影响分层评论 (由高到低, 空档省略) + 显式结论 Block 或 Approve。

- 评审方法移植自严苛的代码质量审查: 默认标记, 通过需挣得; 输出强制分层, 且结论必须显式给 Block (存在体感破坏、键盘/高频操作动画、scale(0)、UI 用 ease-in、易改的非 GPU 动画等) 或 Approve。
- 工艺标准源自 Emil Kowalski 的动效哲学 (animations.dev); 完整规则目录 (缓动曲线、时长表、弹簧配置、手势、clip-path、性能、无障碍) 存放在外部本地文件 STANDARDS.md, 按需加载引用, skill.md 本身不内置数值。
- 修复建议走固定的 9 级偏好层级: 删除 → 缩减 → 修缓动 → 修原点/物理性 → 改可中断 (keyframes → transitions/springs) → 迁移 GPU → 非对称时序 → 打磨 → 无障碍/一致性; 依赖的外部资源仅 STANDARDS.md 一个本地文件, 无其他工具、库或模型 API。
