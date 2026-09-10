# ui-ux-pro-max (`nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max`)

## whitebox

- 解析需求: 提取产品类型/风格关键词, 从项目文件 (package.json、pubspec.yaml、*.xcodeproj 等) 探测技术栈, 探测不到且影响方案时询问用户, 绝不默认假设
- 新项目/新页面: 运行本地脚本 search.py --design-system, 生成成套视觉方向 (风格模式/配色/字体/效果/反模式清单)
- 按需补充定向检索: --domain 查具体关切 (ux、color、typography、gsap、chart…), --stack 查已探测技术栈的落地实现指南
- 综合全部检索结果实施 UI; 交付 App UI 前对照 references/pro-rules.md 的交付前检查清单核验

- 本地检索而非外部模型: 核心是零外部依赖的 Python 脚本 search.py (Python 3.x, 无第三方库), 查询本地数据集 — 79 风格、192 产品配色、74 字体搭配、119 UX 准则、105 图标、17 GSAP 预设、25 图表类型、22 技术栈; 不调用任何外部模型 API, 输出支持 ascii/markdown/json
- 设计系统聚合与拨盘参数化: --design-system 模式聚合 product/style/color/landing/typography 多域匹配结果, 再套用 ui-reasoning.csv 的推理规则; 三个 1-10 拨盘 (--variance/--motion/--density) 调节输出 — density 直接改写 spacing CSS 变量表, motion 附带按档位匹配的现成 GSAP 代码片段
- 持久化与防编造校验: --persist --output-dir 写入 MASTER.md (全局基准) + pages/ (页面级覆盖, 优先级高于 Master); Master 已存在时必须显式 --force 才改写, 防止静默丢弃既有决策; 检索返回 0 结果时禁止编造 — 收窄查询重试一次, 仍为空则明确声明回退到内置默认值
