# shadcn-ui (`giuseppe-trisciuoglio/developer-kit/shadcn-ui`)

## whitebox

- 按触发词匹配确认任务契合：如 "set up shadcn/ui"、"install button/dialog"、"form with validation"、"dark mode" 等
- 用 Bash 执行 npx shadcn@latest init 初始化项目（新项目先 create-next-app），并校验 tsconfig 的 @ 路径别名与依赖
- 用 Bash 执行 npx shadcn@latest add <component> 安装所需组件——组件代码被复制进项目，而非装成依赖包
- 遇到进阶场景（多字段表单、图表、Next.js 集成、主题定制）用 Read 查阅 references/*.md 里的现成模式
- 用 Write/Edit 产出组件代码，遵循既定模式：交互组件加 "use client"、表单用 Form/FormField 全家桶、主题走 CSS 变量

- 组件复制机制：靠 shadcn CLI（npx shadcn@latest add）把组件源码直接复制进项目，用户完全拥有并可改；约束：不是 npm 包、无版本号，安装前须确认 registry 来源可信
- 无障碍 + 主题层：组件构建在 Radix UI 原语上（ARIA 无障碍属性内置）；样式用 Tailwind CSS 工具类 + CSS 变量做主题，深色模式配合 next-themes
- 表单校验管线：React Hook Form 管状态 → Zod schema 定义校验规则 → zodResolver 桥接两者，错误经 FormMessage 展示；图表则是 Recharts 外包一层 ChartContainer 统一配色与提示框主题
