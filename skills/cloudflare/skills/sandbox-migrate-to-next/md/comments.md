# sandbox-migrate-to-next (`cloudflare/skills/sandbox-migrate-to-next`)

## comments

- user: 后端老兵, category: 坑, comment: 我先把 Worker 包升到 @next、容器镜像还停在 stable,启动直接协议对不上。两边必须是同一个 @next 标签,缺一不可。
- user: 独立全栈开发者, category: 坑, comment: 最大的坑:以为 await exec 等于命令跑完。新版只表示进程已启动,要再调 output 或 waitFor* 才拿得到结果。
- user: 运维老哥, category: 注意, comment: 生产切换必须 --containers-rollout=immediate 一次到位,灰度会留两边协议混跑的坏窗口,在线终端当场断。
- user: 前端转全栈新手, category: 坑, comment: 我在 exec 前先 cd,以为下条命令还在原目录,结果全回到默认路径。要么每条带 cwd,要么拼成一段 bash 脚本跑。
- user: 数据工程师, category: 注意, comment: 用 Python 解释器记得把镜像换成 cloudflare/sandbox:next-python,普通 next 镜像没那套 API,我白排查一晚。
- user: 接私活的自由开发者, category: 妙用, comment: 长任务我改成启动后立刻返回响应:超时只取消等待不杀进程,拿着 handle 稍后再取输出,接口再没卡过。
