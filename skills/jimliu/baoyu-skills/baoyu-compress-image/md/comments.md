# baoyu-compress-image (`jimliu/baoyu-skills/baoyu-compress-image`)

## comments

- user: 个人博客站长, category: 坑, comment: 没加 -k 直接压, 原 png 被换成了 webp, 原图没了. 现在我批量处理前先 git 提交一道, 或者统一带上 -k.
- user: 前端实习生, category: 注意, comment: 先确认机器上有 bun 或 npx (跑 JS 的工具), 都没有会直接跑不起来. 我装了 bun 才成功, 别上来就白折腾.
- user: 运维老哥, category: 妙用, comment: 把 -r --json 接进发布前检查: 输出的压缩前后大小直接进日志, 谁提交大图一查便知, 没多装任何东西.
- user: 新媒体运营, category: 注意, comment: 默认质量 80 压照片够用, 但带文字的截图会发虚. 我压公众号截图固定 -q 90, 纯照片保持默认.
- user: 自由摄影师, category: 妙用, comment: 在用户目录的 EXTEND.md 里写好默认保留原图, 之后每张照片压缩都自动留底, 一次配置, 再不用记参数.
- user: 后端老兵, category: 启发, comment: 以前靠构建时插件压图, 配置半天还拖慢打包. 现在提交前随手压一道, 大图进不了仓库, 反而更省事.
