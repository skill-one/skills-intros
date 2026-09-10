# web-artifacts-builder (`anthropics/skills/web-artifacts-builder`)

## whitebox

- 运行 scripts/init-artifact.sh <project-name>, 脚手架生成一个预配置好的 React + TypeScript 工程
- 直接编辑生成的代码开发 artifact (React 组件 + Tailwind + shadcn/ui)
- 运行 scripts/bundle-artifact.sh, 把整个应用打包成单个自包含的 bundle.html
- 在对话中把 bundle.html 作为 artifact 展示给用户; 测试为可选步骤, 默认跳过 (避免增加交付延迟)

- 脚手架预置而非现场搭建: init 脚本产出 Vite + React 18 + TS 工程, 自带 Tailwind CSS 3.4.1 + shadcn/ui 主题系统、40+ 预装 shadcn/ui 组件、全部 Radix UI 依赖、@/ 路径别名、.parcelrc 打包配置, 并自动检测 Node 18+ 环境锁定兼容的 Vite 版本
- 单文件打包管线: bundle 脚本安装 parcel + @parcel/config-default + parcel-resolver-tspaths + html-inline, 先用 Parcel 构建 (关闭 source map, 别名解析), 再用 html-inline 把所有 JS/CSS 内联成一个 HTML; 前提是根目录有 index.html
- 硬性风格约束 (防 AI slop): 开发阶段规避过度居中布局、紫色渐变、统一圆角、Inter 字体; 调试仅在交付后按需进行, 可借助 Playwright/Puppeteer 等工具
