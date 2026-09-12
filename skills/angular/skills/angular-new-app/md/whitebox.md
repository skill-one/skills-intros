# angular-new-app (`angular/skills/angular-new-app`)

## whitebox

- 先探测环境中是否有 Angular CLI (`which ng` / `where ng`); 没有则征求用户同意后 `npm install -g @angular/cli` 全局安装
- 用 `npx ng new <app-name> --interactive=false --ai-config=agents` 脚手架生成应用, 按 flag 定制形态 (`--style` / `--routing` / `--ssr` / `--prefix` / `--skip-tests`)
- 把 `ng new` 生成的 AI 配置内容读入上下文, 作为后续写代码的规范约束
- 按需求用 `npx ng generate component/service/pipe/...` 产出代码, 记下 CLI 返回的文件路径, 再在其上增补业务逻辑; 期间可随时 `npx ng build` 编译查错并修复
- 用户要求时 `npx ng add tailwindcss` 接入 Tailwind v4; 建好部分功能前不启动 app, 是否启动交由用户决定

- 骨架一律走 Angular CLI 而非手写: `ng new` 建应用、`ng generate <类型>` 产组件/服务/管道等, 依赖 CLI 返回的路径精确定位新文件后再增补
- `--ai-config` 是一致性机制: 让 CLI 把 AI 代理最佳实践配置写入项目并载入上下文, 使后续生成代码贴合现代 Angular 规范; 补充最佳实践还可经 `ng mcp` 的 `get_best_practices` 获取
- 外部依赖与校验: 依赖 Node + npm + 网络; 质量校验靠 `npx ng build` 编译通过; 样式接入走 `ng add tailwindcss` (Tailwind v4)
