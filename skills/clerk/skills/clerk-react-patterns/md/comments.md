# clerk-react-patterns (`clerk/skills/clerk-react-patterns`)

## comments

- user: 前端新手，第一次接登录, category: 坑, comment: 我直接判断 isSignedIn，刷新页面先闪"请登录"再闪回内容。加一行 `if (!isLoaded) return <Loading>` 拦在最前才不闪，这个顺序千万别反。
- user: React 老兵, category: 妙用, comment: 一个 `<Route element={<ProtectedRoute/>}>` 就能罩住整组路由，dashboard、settings 塞进去自动受保护，不用每条路由各包一层。
- user: 全栈工程师, category: 注意, comment: 纯客户端方案，后端不会自动变安全。前端 `getToken()` 拿 JWT 放进 `Authorization: Bearer` 头，后端自己验。未登录时 getToken 返回 null，发请求前记得判空。
- user: Vite 新手, category: 坑, comment: 变量名没带 VITE_ 前缀，用 process.env 读全是 undefined，登录组件一片空白。必须叫 `VITE_CLERK_PUBLISHABLE_KEY` 并用 `import.meta.env` 读，改完记得重启 dev server。
- user: 独立开发者, category: 妙用, comment: 用 `useClerk()` 的 `openSignIn()` 直接弹登录框，连 /sign-in 路由都不用先建，MVP 一天就能上线登录。登出也就一行 `signOut()`。
- user: 技术负责人, category: 启发, comment: 组里新人十有八九栽在漏判 isLoaded 上。我把这份坑表贴进 code review 清单，对着五个症状逐条查，登录相关的 bug 明显少了。
