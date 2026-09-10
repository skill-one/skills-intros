# baoyu-compress-image (`jimliu/baoyu-skills/baoyu-compress-image`)

## whitebox

- 解析运行时: 检测 bun 是否安装, 没有则回退 npx -y bun, 都没有则提示安装 bun
- 读取偏好: 按优先级查找 EXTEND.md (项目 .baoyu-skills/… → XDG 配置 → 用户家目录), 第一个找到的生效, 找不到用内置默认值 (webp / 质量 80)
- 执行主脚本 scripts/main.ts <input> [options], CLI 参数 (格式/质量/--keep/--recursive/--json) 叠加在偏好之上
- 压缩时按 sips → cwebp → ImageMagick → Sharp 顺序探测本机可用工具, 用第一个可用的执行
- 输出结果如 image.png → image.webp (245KB → 89KB, 64% reduction), 默认原地替换原文件 (--keep 可保留)

- 工具自动降级链: 压缩前按顺序探测 sips (macOS 系统工具) → cwebp (Google WebP 命令行) → ImageMagick → Sharp (Node 图像库), 依赖系统里装了哪个, 不内置压缩引擎本身
- 两级配置合并: EXTEND.md (三级路径, 先找到先赢, 支持默认格式/质量/是否保留原图) 提供默认值, CLI 参数再覆盖, 未指定任何配置时落到内置默认 (webp, 质量 80)
- 输入兼容文件与目录: 目录加 --recursive (-r) 可递归处理子目录; --json (-) 输出 JSON 供程序化调用; 默认输出为同路径换扩展名, 支持 webp/png/jpeg 三种格式
