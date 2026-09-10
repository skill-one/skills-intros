# clerk-nextjs-patterns (`clerk/skills/clerk-nextjs-patterns`)

## blackbox

**function**: 帮你的 Next.js 项目写好、修好与用户登录/权限 (Clerk) 相关的代码——页面拿不到登录用户、接口老报未登录、操作没做权限校验这类问题, 给它描述现象或贴代码, 它直接给你改好的代码。

- input: 一句话描述问题: 「页面里 userId 一直是 undefined, 用户明明登录了」, output: 修正后的页面代码 (补上 await, 标注哪里改了)
- input: 贴一个 Server Action (表单提交的处理函数) 代码: 「这个操作不希望没登录的人调用」, output: 开头加了登录校验的 Action 代码, 未登录会直接被拒
- input: 一个问题: 「登录了但调接口还是返回未登录」, 并给出 middleware 文件路径, output: 改好的 middleware 配置 (补全了让登录请求也被拦截检查的规则)
- input: 需求: 「要把登录令牌带给 Hasura / Supabase 等外部服务」, output: 在页面或接口里安全获取并附带令牌的示例代码
- input: 贴一段 API 接口代码: 「该返回 401 还是 403, 帮我理清」, output: 修正后的接口代码: 未登录返回 401, 登录但无权限返回 403
