# ask-sonner (`emilkowalski/skills/ask-sonner`)

## comments

- user: 第一次接 React 的新手, category: 坑, comment: 在 layout 和页面各挂了一个 Toaster，每条通知都弹两次。只保留根布局那一个，重复立刻消失。
- user: 用 Tailwind 的 UI 同学, category: 坑, comment: 给 toast 写的 Tailwind 类全没生效——默认样式优先级更高，类名前加感叹号（!text-red-900）才行，改多了不如直接 toast.custom。
- user: 全栈老兵, category: 妙用, comment: toast.loading 返回的 id 再传给 toast.success('完成', { id })，上传的转圈原地变成功，不用先关再弹，体验顺滑。
- user: Next.js 用户, category: 注意, comment: toast() 只在客户端有效。我在 server action 里直接调，啥也不弹；改成返回结果、前端收到后再 toast 才正常。
- user: 深色模式强迫症, category: 注意, comment: theme 默认 light 且不跟系统。接 next-themes 后要写 <Toaster theme={resolvedTheme} /> 才跟着切，别指望它自动识别。
- user: 后台管理系统开发者, category: 坑, comment: toast.promise 第一个参数必须是真 promise。我传了普通函数，它永远转圈；包成 () => fetch(...) 立刻恢复。
