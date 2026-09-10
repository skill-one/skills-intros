# accessibility (`addyosmani/web-quality-skills/accessibility`)

## comments

- user: 三年前端, category: 坑, comment: Lighthouse 拉满 100 分别急着收工, 自动化只查一小半问题。我们弹窗里 Tab 出不来它根本不报, 最后照清单手动过一遍键盘和读屏才算数。
- user: 原生控老前端, category: 妙用, comment: 把 div+role 换回原生 <button> 后, Enter、空格、焦点全是白送的, 删了一堆手写键盘监听。但别给原生按钮再补 Enter 监听, 会双触发。
- user: 接手老项目的前端新人, category: 启发, comment: 以前嫌焦点框破坏视觉, 后来明白它就是键盘用户的鼠标指针。:focus-visible 让它只在键盘操作时出现, 设计干净和无障碍可以兼得。
- user: 电商后端客串写登录页, category: 坑, comment: 我曾在密码框禁粘贴防脚本, 结果密码管理器生成的 20 位密码没法登。放开粘贴并加 autocomplete="current-password", 另留邮箱链接登录备用。
- user: 移动端设计师出身的切图仔, category: 注意, comment: 点按目标至少 24×24 像素, 我们的关闭按钮 18px 手机上总点偏; 有吸顶导航记得给焦点元素加 scroll-margin-top, 否则落点会被挡住。
- user: 读屏重度用户, category: 坑, comment: 报错只描红边框对我完全无效。请用文字提示加 aria-invalid 和 role="alert", 提交失败后把焦点移到第一个错处, 我才能继续往下走。
