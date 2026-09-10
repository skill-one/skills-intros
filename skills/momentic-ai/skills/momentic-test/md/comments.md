# momentic-test (`momentic-ai/skills/momentic-test`)

## comments

- user: 第一次配环境的新手, category: 坑, comment: 我把环境切成 staging,一跑还是打到线上——测试文件里写死的 url 在所有环境里都优先生效。切环境前先查测试自己的 url 字段。
- user: 从 Selenium 迁来的测试老手, category: 妙用, comment: 改长测试不整段重跑:先跑到上一步,在"登录完成"这类节点 preview 截图确认,splice 保存后再验下一小段。一下午改完十几步。
- user: 兼职写测试的前端, category: 注意, comment: 我上手先加了"打开首页"步骤,结果会话本来就自动从起始 URL 开始,等于重复导航。第一步直接写页面上的操作就行。
- user: 管 CI 的运维, category: 坑, comment: main 分支跑测试比开发分支慢好几倍:受保护分支只读缓存不写缓存。要么让 CI 跑,要么手动加 --save-cache。
- user: 测 AI 产品的 QA, category: 妙用, comment: 测聊天回复时缓存总回放旧对话,把 AI Action 设 cache: false 每次重跑;下单这类固定流程保留缓存,快且稳。
- user: 测试团队负责人, category: 启发, comment: 它遇到提交、删除这类不可撤销操作会先停下来问我,批准后也只执行一次。这个习惯我们后来写进了自己的自动化规范。
