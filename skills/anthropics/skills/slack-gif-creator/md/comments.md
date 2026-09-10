# slack-gif-creator (`anthropics/skills/slack-gif-creator`)

## comments

- user: 第一次用的新手, category: 坑, comment: 以为能画可爱卡通形象,结果出的是几何图形拼的。它不认 emoji 字体、没自带素材,全靠圆形多边形线条现画,预期先摆正。
- user: 运维老哥, category: 注意, comment: 没装依赖就跑,直接报 ImportError。先 pip install pillow imageio numpy,传 Slack 前再用 is_slack_ready 校验一遍,免得传了被拒。
- user: 群运营小编, category: 坑, comment: 做了个 5 秒的表情动图,Slack 死活传不上。表情限 128x128、3 秒内;save 时加 optimize_for_emoji 和 remove_duplicates,体积直接砍半。
- user: 品牌设计师, category: 妙用, comment: 把公司 logo 传上去当配色参考,生成的动画自动贴品牌色,省了我从零对色号。内部小动效提案根本不用开 AE。
- user: 前端工程师, category: 妙用, comment: 默认匀速运动很僵硬,interpolate 加个 easing='bounce_out',落地瞬间有回弹感。一个参数的事,质感差一个档次。
- user: 团队行政, category: 启发, comment: 以前发通知全是文字刷屏没人看,配个 3 秒小动画当开头,盯着看完的人明显变多。动图不是玩具,是抢注意力的工具。
