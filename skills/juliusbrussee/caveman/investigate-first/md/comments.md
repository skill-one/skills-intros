# investigate-first (`juliusbrussee/caveman/investigate-first`)

## comments

- user: 运维老哥, category: 妙用, comment: 偶发 500 说不清规律,它按「最便宜的验证」排假设顺序,第二条就锁定连接池泄漏,省了我一整晚瞎重启试错。
- user: 第一次用的新手, category: 注意, comment: 我让它查完「顺便修一下」,结果它只给原因和证据就停了。想让它动手改代码,必须明说「找到原因后直接修复」。
- user: 后端老兵, category: 启发, comment: 它让我看清自己的老毛病:报错在缓存就直接改缓存。先分清「看到的症状」和「猜的原因」,这次根因其实在上游数据流。
- user: 测试工程师, category: 坑, comment: 只丢一句「有时很慢」它查不了,只能反过来问我要细节。附上报错原文、复现步骤和最近改动后,一次就出了可信结论。
- user: 技术组长, category: 妙用, comment: 诊断报告是「原因+证据」格式,能直接转发给领导。而且证据够了它就停,不会为了显得努力无限查下去烧工时。
- user: 接手祖传代码的, category: 注意, comment: 它宁可回「证据不够」也不肯猜,催也没用。偶发问题先趁日志没滚动截图存现场,证据丢了它就无从下手。
