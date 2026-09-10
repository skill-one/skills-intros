# remotion-create (`remotion-dev/skills/remotion-create`)

## whitebox

- 环境检查: 确认 Node.js 与 Git 已安装、当前目录适合建新项目; 若项目已存在则整步跳过。
- 脚手架: 运行 npx create-video@latest --yes --blank --no-tailwind <项目名> 生成空白模板, cd 进去后 npm i 装依赖。
- 写视频: 保留脚手架, 按 Remotion React 标记最佳实践与视频版式规则添加 React 标记; 多场景视频套用 multi-scene 指南, Tailwind 仅在用户要求时引入。
- 起预览: 运行 npx remotion studio --no-open 启动长驻预览服务, 在浏览器访问 /[composition-id] 查看指定合成。
- 出片: 仅当用户明确要求时运行 npx remotion render 渲染视频文件。

- 模板化脚手架: 项目结构全部来自官方 CLI create-video@latest 的 blank 模板 (默认不含 Tailwind), 后续改动遵循「不动脚手架、只加 React 标记」原则; 运行前提是 Node.js + Git。
- React→视频转换: 视频内容即 React 组件, 依据 Video Layout Rules 控制视频优先的布局与文字尺寸; 按交互最佳实践组织标记, 让用户在 Studio 里的编辑能写回代码。多场景用 multi-scene 指南组合子序列。
- Remotion CLI 双命令通道: 预览走 npx remotion studio --no-open (长驻进程打印 URL, 服务已启动则直接返回 URL); 导出走 npx remotion render, 是显式触发的独立步骤, 默认不渲染。
