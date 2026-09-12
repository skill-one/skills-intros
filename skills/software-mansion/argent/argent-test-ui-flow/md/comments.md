# argent-test-ui-flow (`software-mansion/argent/argent-test-ui-flow`)

## comments

- user: QA 转岗新手, category: 坑, comment: 我上来就用 await-ui-element 等一个自己猜的按钮文字，结果只干等超时。后来养成习惯：先 describe 拿到真实文案/标识，再拿它当等待条件，一次就过。
- user: React Native 独立开发, category: 坑, comment: 安卓上组件树一直拿不到，折腾半天才发现没跑 adb -s 序号 reverse tcp:8081 tcp:8081，设备根本够不着 Metro。补上这条命令立刻出树。
- user: 外包验收方技术, category: 妙用, comment: 验收最烦反复点登录。我把整条流程录成 yaml，开发每次交新版我只跑一句 flow-execute 就回归完，从半小时缩到一分钟。
- user: iOS 老开发, category: 注意, comment: 改 UI 前必须先截基线图！我改完才补截，screenshot-diff 没法对比，白跑一轮。记得 scale 设 1.0，把返回的 path 存下来。
- user: 小团队兼职测试, category: 妙用, comment: 登录密码用 {{secret:APP_PASSWORD}} 占位，值放 .argent/secrets.env。明文不出现在报告和对话里，过程录屏给客户看也不慌。
- user: 手工测试转自动化, category: 启发, comment: 以前验证全靠肉眼盯截图。现在每步先分类：看外观用截图对比，查跳转用 describe，查报错翻日志和网络记录，漏检明显少了。
