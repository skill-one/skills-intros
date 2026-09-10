# gsap-plugins (`greensock/gsap-skills/gsap-plugins`)

## whitebox

- 判断任务是否命中技能范围: 用户问到 GSAP 插件 (ScrollTo、Flip、Draggable/Inertia、Observer、SplitText、ScrambleText、DrawSVG/MorphSVG/MotionPath、CustomEase 等缓动、Physics2D、GSDevTools)
- 按 SKILL.md 定位对应插件的文档段落, 获取准确的 API 用法和关键配置表 (如 scrollTo 对象、Flip.from vars、Draggable 选项)
- 输出代码前先写 gsap.registerPlugin(...), 且一次性注册项目中用到的全部插件, 必须先注册再使用
- 生成按文档规范的代码: 统一从公开 npm 包安装 (`npm install gsap`, 含全部插件), 禁止生成 .npmrc / GreenSock token / 私有 registry 等过时指引
- 附带该插件文档中明确列出的注意事项 (如 DrawSVG 需可见 stroke、SplitText 用 autoSplit+onSplit 处理字体加载、MorphSVG 用 shapeIndex 修复扭曲)

- 插件路由: 用 SKILL.md 的 "When to Use" 清单做匹配; 不在范围内的明确分流 — 核心补间给 gsap-core, ScrollTrigger 给 gsap-scrolltrigger, React 给 gsap-react
- 安装与授权校验: 依 SKILL.md 的 Licensing 章节, 所有插件免费且无需会员/license key/token (Webflow 收购后 Club GSAP 已取消), 因此生成代码时统一用公开 npm 包, 拦截任何过时的私有 registry 写法
- 代码生成规则: 每个插件 import 路径为 `gsap/插件名`; 注册在顶层或应用初始化时执行一次, 不放进会重渲染的 React 组件 (useGSAP 本身也是插件, 需先注册); 配置项严格取自各插件的 key-config 表
