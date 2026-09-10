# react:components (`google-labs-code/stitch-skills/react:components`)

## comments

- user: 接私活的前端, category: 妙用, comment: 客户改需求我重跑, 它先查 .stitch/designs 里有没有旧设计, 问我是重新拉还是复用本地。断网时选复用照样继续改组件, 白省一次下载。
- user: 第一次用的新手, category: 坑, comment: 我让 AI 用自带抓取直接拉 HTML, Google 存储域名直接失败白等半天。换脚本 fetch-stitch.sh 一次成功, URL 记得带引号, 不然 shell 报错。
- user: 设计师转前端, category: 注意, comment: 截图默认是低清缩略图, 我对着糊图核对配色和间距对半天。在截图 URL 后拼上 =w 宽度值(宽度的数字在元数据里)再拉, 才是能看清细节的高清图。
- user: TS 严格派, category: 注意, comment: 别跳过 validate 直接跑 dev。AST 报告会点名缺哪个 Props 接口、哪处样式写死了 hex, 对着改五分钟就过, 跳过就是带病上线。
- user: 维护老项目的中级前端, category: 妙用, comment: 它从设计 HTML 的 head 里抽出 tailwind.config 同步进 style-guide.json, 色值全换成主题类名而不是硬编码, 接进我现有主题几乎零改动。
- user: 写了十年 jQuery 的老兵, category: 启发, comment: 以前我拿设计稿就一个文件糊到底。看它把文案图片全塞 mockData.ts、逻辑拆进 hooks, 换数据源只动一处, 我现在自己写项目也照这个结构拆。
