# baoyu-danger-gemini-web (`jimliu/baoyu-skills/baoyu-danger-gemini-web`)

## comments

- user: 第一次用的新手, category: 坑, comment: 第一次跑命令半天没输出，差点以为卡死了——其实是在弹浏览器等我登 Google 授权。机器上没装 Chrome 或 Edge 的话，这步会直接失败。
- user: 运维老哥, category: 注意, comment: 服务器直连 Google 必超时，命令前内联加 HTTP_PROXY 环境变量才通。用几天报 cookie 失效，跑一次 --login 重新授权即可。
- user: 独立设计师, category: 妙用, comment: 把客户 logo 截图用 --reference 传入，配 --image 连出十几张风格变体再挑，试稿从一天缩到十分钟，全程不开设计软件。
- user: 后端老兵, category: 妙用, comment: 加 --json 拿结构化输出，--sessionId 保持同一会话，我把它嵌进脚本流水线当出图后端，逐轮让它改图，全程不用申请 API 密钥。
- user: 自媒体写手, category: 妙用, comment: 长提示词写成 markdown 模板用 --promptfiles 传入，换风格只改文件里一行，命令不用重敲，同事照着文件就能复现同款图。
- user: 合规岗工程师, category: 注意, comment: 这是逆向的非官方网页接口，官方一改版随时可能失效；登录 cookie 会存在本地文件里，公司管控机或合规敏感环境我直接绕开不用。
