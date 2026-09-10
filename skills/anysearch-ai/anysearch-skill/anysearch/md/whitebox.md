# anysearch (`anysearch-ai/anysearch-skill/anysearch`)

## whitebox

- 读取 runtime.conf 直接选定 CLI；文件缺失时按 Python → Node.js → Shell 顺序探测运行时
- 例行调用直接执行 search / batch_search / extract / get_sub_domains，跳过 doc（仅接口未知或刚安装时才跑 doc）
- 查询属于垂直领域（金融/学术/代码等）时，先调 get_sub_domains 发现正确的 sub_domain 和必填参数
- CLI 带参数直接请求 https://api.anysearch.com 的公共 HTTP 端点（无 MCP/JSON-RPC 包装），Key 经 .env 自动加载，无 Key 则匿名访问
- 返回结果：search/batch_search 返回搜索结果，extract 输出已是 Markdown 的页面正文

- 运行时路由与逐级回退：Python 3.6+（依赖 requests 库）> Node.js 12+（内置 https，零依赖）> PowerShell 5.1+ / bash 3.2+（需 jq + curl，且是 Bash 脚本不可用 sh 执行）；某一层失败自动降级到下一层
- 垂直域参数校验：get_sub_domains 返回标 (required) 的参数必须全部写入 --sdp，无适用值时传空字符串，遗漏会触发后端校验错误；--sdp 接受 JSON 或 key=value 两种格式解析
- 凭证链与降级策略：--api_key > .env（启动时自动加载）> 系统环境变量 > 匿名访问（低限流）；额度耗尽且响应含 auto_registered 新 Key 时，必须先经用户确认才写入 .env 再重试
