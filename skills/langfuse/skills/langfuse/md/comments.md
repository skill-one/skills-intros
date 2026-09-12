# langfuse (`langfuse/skills/langfuse`)

## comments

- user: 第一次接 AI 观测的新手, category: 坑, comment: 我把私钥直接贴进聊天里, 被拦下还白换了一把 key。正确做法: 终端里自己 export 公钥/私钥/BASE_URL 三个变量, 让它读环境变量就行, 安全又省事。
- user: 数据工程师, category: 妙用, comment: 先跑 npx langfuse-cli api __schema 列出全部接口, 再用 list/get 配合 jq 在终端批量拉 trace 做对比, 十次实验结果几分钟导完, 不用开网页一个个翻。
- user: 全栈开发, category: 注意, comment: 让它写埋点代码时它会先去抓最新官方文档, 别嫌慢。我之前让 AI 凭记忆写, SDK 参数全是旧版用法, 返工更久。这步先查文档反而是省时间。
- user: 自部署运维, category: 坑, comment: 我们是私有化部署, 我没提服务器地址, 它默认连了官方云, 翻半天查不到数据。开口第一句就给自建 URL, 或让它先检查 BASE_URL 环境变量, 一次就对。
- user: 不懂代码的产品经理, category: 注意, comment: 让它教我在网页上配评估器, 网页按钮名和 API 字段不一样, 它会主动要截图核对。别光用文字描述界面, 直接截屏发它, 它指的步骤才准。
- user: 刚接手评测的工程师, category: 妙用, comment: 我把「trace 有了但不知道怎么评」这句原话丢给它, 它先盘数据采集再定指标, 还给 LLM 裁判做了准确率校准, 比自己瞎搭评测流程快得多。
