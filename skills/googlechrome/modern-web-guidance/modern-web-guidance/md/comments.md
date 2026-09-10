# modern-web-guidance (`googlechrome/modern-web-guidance/modern-web-guidance`)

## comments

- user: 后端老兵, category: 注意, comment: 这工具只管前端. 我拿它查 Express 路由和 SQL 优化全是空结果, 白折腾一场. 后端和部署问题直接问模型, 别走它.
- user: 第一次用的新手, category: 坑, comment: 在沙箱环境里直接让它跑, 卡在下载上白等十几分钟才超时. 后来先让 AI 申请带网络的 npx 执行权限, 再跑一次就过.
- user: 前端老手, category: 妙用, comment: 以前 AI 写弹窗全凭旧记忆, 手搓遮罩层几十行. 我立了规矩: 动手前必须先 search, 结果直接用原生 Popover, 代码砍一半.
- user: Windows 办公机用户, category: 注意, comment: Windows 上 npx 会直接失败, 换成 npx.cmd 就行. 权限白名单也要对应写成 npx.cmd, 我排查了半小时才定位到这.
- user: 运维老哥, category: 注意, comment: 批权限千万别写裸的 npx *, 那等于放行任意包执行. 只批 npx -y modern-web-guidance@latest * 这一条, 范围最小.
- user: 团队 Tech Lead, category: 启发, comment: 把「不用 polyfill」这类浏览器支持策略写进 CLAUDE.md 后, AI 碰到新特性会主动配降级方案, 我 review 时不用再逐行查兼容性.
