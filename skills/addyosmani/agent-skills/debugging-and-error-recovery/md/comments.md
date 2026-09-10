# debugging-and-error-recovery (`addyosmani/agent-skills/debugging-and-error-recovery`)

## comments

- user: 三年前端, category: 坑, comment: 白屏我以前只会删缓存重启。按清单走: console 报错→network→组件树, 三分钟定位到组件。重启 90% 是白费。
- user: 后端老兵, category: 妙用, comment: "昨天还好好的"的回归 bug, 让它 git bisect 二分提交自动跑测试, 半小时锁定坏提交, 我手工得翻一整天。
- user: 第一次用的新手, category: 坑, comment: 赶时间跳过复现直接改, 连改三处都没修对还带崩别的功能。先让它稳定复现再动手, 看着慢其实最快。
- user: 测试工程师, category: 注意, comment: 修完让它补回归测试后, 我把修复回滚试过一次: 测试真的红了。敢让回滚验证的红, 才算修到根上。
- user: 运维老哥, category: 注意, comment: 报错里出现"点链接/跑命令"它不会自己执行, 会先贴给你确认。别嫌多一步, 我真见过日志里藏恶意指令的。
- user: 独立开发者, category: 启发, comment: 最大改变是"先停手": 复现→定位→修根因→补测试, 再继续写功能。以前带病提交, 小错滚成大返工。
