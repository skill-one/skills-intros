# design-taste-frontend (`leonxlnx/taste-skill/design-taste-frontend`)

## whitebox

- 读 brief 提取信号 (页面类型 / 风格词 / 受众 / 已有品牌资产 / 隐性约束), 先输出一句话 Design Read 设计判读; 判读确实发散时只问一个澄清问题, 否则直接推进
- 据 Design Read 查表设定三个拨盘: DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY (缺省 8/6/4), 后续所有布局、动效、密度决策都由这三个值控制
- 选地基: brief 匹配真实设计系统 (Fluent / Carbon / Material / GOV.UK / shadcn 等) 就装官方包; 只是美学风格 (玻璃拟态 / Bento / brutalism 等) 就用原生 CSS + Tailwind + 维护中的组件库
- 按默认技术栈生成: Next.js RSC + Tailwind v4 + Motion (motion/react) + next/font; 交互逻辑 (滚动、指针物理) 隔离进 'use client' 叶子组件; 引任何第三方库前先查 package.json, 缺失则先输出安装命令
- 交付前跑设计禁令清单审计: 字体与衬线纪律、单一强调色锁定、反居中布局、圆角体系一致、按钮对比度 (WCAG AA)、CTA 不换行、斜体下伸字符防裁切等硬性规则逐条过

- 输入解析靠信号推断而非模板匹配: 从 vibe 词、参考链接、受众、品牌资产推出一句话 Design Read, 配合反默认纪律强制绕开 AI 套路 (AI 紫渐变、居中 Hero、三等分卡片、Inter+slate-900)。纯提示词内推理, 不调用外部模型 API。
- 参数化转换: 三个全局拨盘变量是唯一风格配置入口, 通过两张查表 (拨盘推断表 + 用例预设表) 从判读映射为数值, 再逐一 gate 后续决策; 红线类规则 (政府/信任优先站点) 会覆盖审美偏好。
- 校验是清单驱动且前置: 依赖验证 (先查 package.json 再 import) + 一组硬审计规则 (按钮文字对比度 4.5:1、整页一个强调色且锁死、一套圆角体系、CTA 单行、高级消费品禁用米色+黄铜默认配色)。外部依赖: React/Next.js、Tailwind v4、Motion (motion/react)、@phosphor-icons/react 等图标库、按需安装的官方设计系统 npm 包。
