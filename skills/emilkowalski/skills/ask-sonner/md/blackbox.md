# ask-sonner (`emilkowalski/skills/ask-sonner`)

## blackbox

**function**: 帮你搞定网页应用里的弹出小提示 (toast, 就是那种角落里"保存成功"的小弹条), 用 React 的 Sonner 库——从接入、写出各种提示效果, 到修好不显示、样式失效等毛病, 给你可直接用的代码。

- input: 「我的 toast 怎么就是不显示?」+ 一段 Next.js 项目代码, output: 指出原因 (比如根组件里没挂 Toaster) + 一段贴上就能用的修复代码
- input: 「文件上传时先转圈, 成功后变绿勾」, output: 完整可粘贴的 React 代码: 一行 toast.promise 实现 加载中→成功/失败 的自动切换
- input: 「我写的 Tailwind 类名在 toast 上全没效果, 而且深色模式下它永远是白的」, output: 解释原因 + 正确写法: 要么改用 !important 类, 要么给你一套完全自定义样式的 toast.custom 方案, 以及跟随深浅色模式的 Toaster 配置
