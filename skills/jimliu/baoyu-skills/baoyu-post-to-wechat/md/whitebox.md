# baoyu-post-to-wechat (`jimliu/baoyu-skills/baoyu-post-to-wechat`)

## whitebox

- 读取 EXTEND.md 偏好 (主题/颜色/作者/评论开关); 无配置则先完成首次设置
- 判定输入类型: HTML 直接跳到校验; Markdown 继续走流程; 纯文本先存为 post-to-wechat/YYYY-MM-DD/<slug>.md
- 选定发布方式 api / browser / remote-api; 缺 API 凭证时走引导配置写入 .baoyu-skills/.env
- 解析主题与颜色, 校验元数据 (标题/摘要/作者/封面), 缺失项按回退链自动生成或向用户询问
- 调用 wechat-api.ts / wechat-article.ts 发布为公众号草稿, 输出含 media_id 的完成报告

- 转换: markdown→HTML 由发布脚本内部完成 (md-to-wechat.ts); 因两条路径渲染图片方式不同 — API 渲染 <img> 供上传, 浏览器用占位符做粘贴替换 — 严禁预先转好 HTML; 普通外链默认转为文末引用 (--no-cite 保留内联)
- 发布: API 方式用 bun/npx 运行脚本, 直调微信公众平台 draft/add 接口 (需 access_token、封面 thumb_media_id、need_open_comment/only_fans_can_comment); browser 方式走 Chrome CDP 粘贴替换, 需已登录会话; remote-api 变体把出站 HTTPS 经 ssh -N -D SOCKS5 隧道以白名单服务器 IP 出网, AppSecret 不离开本地
- 校验/回退: 元数据取值优先级 CLI 参数 → frontmatter → EXTEND.md (账号级→全局) → 内置默认值; 标题/摘要缺失时自动生成 (标题取首个 H1/H2 或首句, 摘要取首段截 120 字); 封面按 CLI → frontmatter → imgs/cover.png → 首张内联图 回退
