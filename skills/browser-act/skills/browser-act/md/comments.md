# browser-act (`browser-act/skills/browser-act`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我上来自己敲命令, --help 里根本找不到工作流。正确顺序是先加载 skill, 再跑 get-skills core 拿完整用法, 输出千万别截断。
- user: 公司电脑上的后端, category: 注意, comment: 先确认 Python 3.12+ 且要用 uv 装, 我公司机器还是 3.10, 装完直接报错, 升级后才跑通。首次安装会下载外部包并要你确认, 提前跟 IT 打好招呼。
- user: 数据采集工程师, category: 妙用, comment: 抓 JS 渲染页以前 curl 只拿到空壳。轻量提取模式不开会话直接返回渲染后内容, 秒级完成, 单页抓取我全用它替换了 curl/WebFetch。
- user: 多账号运营, category: 妙用, comment: 七八个账号各建一个浏览器, 配置互相隔离、各绑各的代理, 并行跑单不串号。比手动开多个 Chrome 切 cookie 稳太多。
- user: 内网安全负责人, category: 注意, comment: 过安全审查我重点看了: cookie、登录态、页面内容全存本地, 唯一出网是授权后的验证码图片; 连本地 Chrome 也需明确确认, 审批很好过。
- user: 前端自测党, category: 启发, comment: 改完样式让 AI 截图回来核对布局, 复查从半小时变一分钟。我把「截图自查」写进了提交前 checklist, 再没被视觉细节打回。
