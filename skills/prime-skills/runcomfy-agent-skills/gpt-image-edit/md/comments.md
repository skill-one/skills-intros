# gpt-image-edit (`prime-skills/runcomfy-agent-skills/gpt-image-edit`)

## comments

- user: 跨境电商运营, category: 妙用, comment: 一张英文海报出了日、德、阿三个语种版,人脸没动。诀窍是新标题字符要原样加引号并标注语种,只说"换成阿拉伯语"必拼错字。
- user: 第一次用的新手, category: 坑, comment: 首条 prompt 塞了换背景+改标题+调色三件事,人脸和 logo 全飘了。拆成两次、每条开头先写保持什么不变,就稳了。
- user: 品牌设计师, category: 启发, comment: 被它逼出的习惯:动图前把"不能动的"(脸、标、构图)和"要改的"分开列,列完才发现哪些是真品牌资产,不再来回试稿。
- user: 电商美工, category: 坑, comment: 3:2 详情图手滑传了 1:1,被硬裁掉两边,白跑一次。想保原比例就写 size:auto;size 只有固定几档,乱填直接报 422。
- user: 写 CI 脚本的后端, category: 注意, comment: 脚本里别用交互式 login,直接设 RUNCOMFY_TOKEN 即可;退出码 75(超时/限流)要写自动重试,77 是没登录,别当接口挂了排查。
- user: 出海广告投手, category: 妙用, comment: 多图合成要按序号引用:"用图1的人、图2的光线、图3的配色",模型分得很清。第一张会被当主参考,主体一定放第一张。
