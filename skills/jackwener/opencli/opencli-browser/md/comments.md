# opencli-browser (`jackwener/opencli/opencli-browser`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我把上次会话抄下来的 [5] 编号直接复用, 报 stale_ref. 编号只对当次快照有效, 页面一跳转就得重跑 state 拿新编号.
- user: 数据采集工程师, category: 妙用, comment: 列表数据我原本从 DOM 逐条抠, 后来跑 browser network 发现底层 JSON 接口, --filter 筛到那条再 --detail 拿完整 body, 又准又不怕页面改版.
- user: 自动化测试工程师, category: 注意, comment: type 完一定 get value 回读: 自动补全框打完字弹候选, 不按 Enter 表单里就是半截词. 返回里 autocomplete: true 就是在提醒你补这一步.
- user: 运维老哥, category: 注意, comment: 先跑 opencli doctor 再干别的. 我卡了半天连不上 Chrome, 一查是 1Password 扩展挡了调试端口. Chrome 没开、扩展没装、端口被拦, 它都会直接告诉你.
- user: 运营小妹(非技术), category: 妙用, comment: 图标按钮没文字认不出, screenshot --annotate 会把 [N] 编号直接标在截图上, 对着图点编号就行. 日期框的 compound 字段还给了格式, 照抄不用猜.
- user: 前端老兵, category: 坑, comment: match_level 出 reidentified 我没当回事继续连点, 结果点到了页面上另一个同款按钮. 现在见到 reidentified 必先 state 核对再动手.
