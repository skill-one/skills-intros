# hyperframes-cli (`heygen-com/hyperframes/hyperframes-cli`)

## whitebox

- 初始化项目: npx hyperframes init 脚手架 (或 capture 抓取现有网站), 非交互模式需 --non-interactive --example=<name>
- 找现成的动效原语: 先用 npx hyperframes catalog --query "<英文描述想要的效果>" 搜索目录, 命中则 add 安装, 不再手写动效
- 创作与快速反馈: 用 HTML/composition 编写时间线, 编辑过程中反复跑 npx hyperframes lint; 含子组合时用 snapshot --at 检查挂载点
- 最终门禁: npx hyperframes check (先重跑 lint, 再开一个浏览器会话审计运行时错误/请求失败/布局/motion.json 断言/WCAG 对比度), 通过后 preview --background 交用户审阅, 未经批准不渲染
- 批准后渲染: --quality draft 迭代, --quality high 交付 out.mp4, 再用 test -s + ffprobe 验证文件存在、非空、时长合理

- 双层级目录检索: 默认按词汇重合度本地排名 (纯本地, 查询不外发); 加 --on-device 才启用 ~33MB 量化 ONNX 模型 (bge-small-en-v1.5 + tokenizer, 缓存于 ~/.hyperframes/) 做语义排名; --json 信封携带 tier/dropped/unindexed/top_score 用于判读结果可信度; 只有 feedback --search-miss 这条独立命令会把查询外发
- check 校验机制: 一次 lint 复跑 + 单浏览器会话 + 单次 seek pass, 审计运行时错误、失败请求、布局、*.motion.json 断言和 WCAG 对比度; 持续性发现阻塞退出码, 瞬态出入场发现仅提示; doctor --json 恒定 exit 0, 须门禁其 payload 的 .ok 字段
- 多后端渲染管线: 本地依赖 Node.js ≥22 + FFmpeg + 浏览器, 帧捕获出片; 可切换 --docker 容器化渲染、HeyGen 托管云渲染 (200MB 上传限制, 超限走 cloud render --dry-run --json 排查 .hyperframesignore)、AWS Lambda / GCP Cloud Run 分布式渲染
