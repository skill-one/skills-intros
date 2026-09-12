# better-accessibility (`jakubkrehel/skills/better-accessibility`)

## blackbox

**function**: 检查你的网页/应用代码对特殊使用场景 (纯键盘操作、屏幕阅读器朗读、画面放大、减少动效) 是否友好, 并给出能直接落地的修改。

- input: 一个登录表单的代码文件 (如 login.html), output: 一份问题清单表格: 每条含严重程度 (HIGH/MEDIUM/LOW)、代码位置 (文件:行号)、改前 → 改后的写法、原因, 末尾给出 "Block" 或 "Approve" 的总结论
- input: 一个自定义弹窗组件的代码, output: 修改后的代码: 打开弹窗时光标自动进入、按 Esc 可关闭、弹窗开着时背景点不动、关闭后光标回到原来的按钮
- input: 一段只靠红色标出填错字段的表单代码, output: 修改后的代码: 错误提示带上文字/图标 (不只靠颜色), 提交时屏幕阅读器 (把页面内容读出来的软件) 能听到出错提示
- input: 一排只有图标没有文字的按钮代码, output: 修改后的代码: 每个按钮补上描述性名称, 读屏软件能念出 "搜索" 而不是 "按钮"
