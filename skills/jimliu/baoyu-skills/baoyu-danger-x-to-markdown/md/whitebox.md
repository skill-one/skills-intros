# baoyu-danger-x-to-markdown (`jimliu/baoyu-skills/baoyu-danger-x-to-markdown`)

## whitebox

- 校验授权: 读 consent.json, accepted 且 disclaimerVersion=1.0 则打印警告继续; 否则展示免责声明请求同意, 拒绝即退出
- 加载偏好: 按项目 → XDG → 家目录优先级查 EXTEND.md; 未找到则阻塞式首次设置 (AskUserQuestion 问媒体/输出目录/保存位置) 后写入再继续
- 执行转换: 用 bun (无则 npx -y bun 兜底) 运行 {baseDir}/scripts/main.ts <url>, 经逆向工程 X API 拉取推文/线程/文章
- 媒体处理: download_media=ask 时先不带 --download-media 保存, 检出远程图片/视频 URL 则询问; 确认后带 flag 重跑, 下载到 imgs/ 与 videos/ 并把链接改写为本地相对路径
- 落盘输出: 生成 YAML front matter + 正文, 写入 x-to-markdown/{username}/{tweet-id}/{content-slug}.md

- 数据源是逆向工程的非官方 X API (非官方, 可能随 X 改版失效); 认证优先读环境变量 X_AUTH_TOKEN/X_CT0, 兜底自动打开 Chrome 登录并本地缓存 cookies
- 运行时为 TypeScript 脚本 scripts/main.ts, 由 bun 执行, 无 bun 时退化为 npx -y bun (依赖任一可用)
- 校验分两层: 同意层 (consent.json 版本必须为 1.0, 不匹配即重新弹声明) 和配置层 (EXTEND.md 三级查找, 取值优先级 CLI 参数 > EXTEND.md > 内置默认); 支持 x.com/twitter.com 推文 URL 与 x.com/i/article/<id> 文章 URL, 统一转成 front matter + markdown
