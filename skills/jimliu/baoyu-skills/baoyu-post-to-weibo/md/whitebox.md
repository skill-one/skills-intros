# baoyu-post-to-weibo (`jimliu/baoyu-skills/baoyu-post-to-weibo`)

## whitebox

- 判定发布类型：输入为 .md 文件 → 走头条文章；纯文本/带图文本 → 走普通微博
- 读取偏好：按优先级查找 EXTEND.md（项目 > XDG > 用户主目录，首个命中生效），并确定运行时（bun 优先，否则 npx -y bun）
- 启动脚本，通过 CDP 驱动真实 Chrome 打开微博页面（普通微博 = 首页发博框；头条文章 = card.weibo.com 文章编辑器）
- 填充内容：普通微博直接填文本 + 图片/视频（≤18 个文件）；头条文章先点「写文章」，填标题/导语，把 Markdown 转好的 HTML 粘贴进编辑器，再逐个替换图片占位符
- 脚本只负责填充，最后交由用户在浏览器中人工审核并手动发布

- 浏览器驱动：全程通过 Chrome CDP (远程调试协议) 操控真实浏览器，绕过反爬检测；遇到 debug 端口连接失败时，自动 pkill 仅限 baoyu-skills profile 的 CDP Chrome 实例后重试（绝不误杀用户日常 Chrome）
- 头条文章转换与校验：Markdown → HTML（默认主题，不传 --theme）；标题超 32 字截断并告警，导语超 44 字自动从正文重新生成；正文经剪贴板 + 模拟真实粘贴键入 ProseMirror 编辑器，图片先占位（WBIMGPH_）再逐个替换，完成后自动核对占位符残留数与预期图片数是否一致，不一致则输出警告
- 运行时解析：${BUN_X} 按安装情况解析为 bun 或 npx -y bun（两者都无则提示安装 bun）；Chrome 支持 --profile 指定自定义配置目录，首次运行需手动登录，会话由 Chrome profile 持久化
