# harden (`pbakaus/impeccable/harden`)

## whitebox

- 接收 target, 按 description 匹配任务类型 (harden / 生产就绪 / 错误态 / 空状态 / i18n / 溢出 / 引导流程), 不契合则不接活
- 评估弱点: 极端输入 (超长文本、emoji、RTL、1000+ 条目、空数据) + 错误场景 (断网、超时、400~500 状态码、并发操作) + i18n 差异 (德语长约 30%、RTL、CJK、日期/数字格式)
- 按固定维度逐项修复: 文本溢出、i18n、错误处理、空/加载/权限等边缘状态、新手引导、输入校验、可访问性、性能韧性
- 验证: 按清单复测边缘用例 (100+ 字符、emoji、RTL/CJK、断网/限速 3G、连点提交 10 次、强制 API 报错、清空全部数据)

- 评估是清单驱动的人工扫描, 不执行代码: 对照三张固定检查表 (极端输入 / 错误场景 / i18n) 系统找出 target 的脆弱点
- 修复靠内嵌代码模式直接套用: skill.md 自带 CSS/JS 片段 (truncate/line-clamp、flex 的 min-width:0、RTL 逻辑属性、Intl API、debounce/throttle、prefers-reduced-motion), 全部是 Web 平台原生能力, 不引入外部库
- 外部依赖仅两个第三方项: 无障碍自动检测工具 (axe / WAVE) 与正规 i18n 库 (复数规则交给库处理, 如 t('items', { count })); 无任何模型 API 依赖, 全部逻辑来自 skill.md 规则
