# dart-build-cli-app (`dart-lang/skills/dart-build-cli-app`)

## comments

- user: 运维老哥, category: 妙用, comment: Mac 上 dart compile exe 加 --target-os=linux --target-arch=x64,编出的 Linux 单文件扔服务器直接跑,省得专门开台 Linux 机器。
- user: 第一次写 CLI 的新手, category: 坑, comment: 开发时一直 dart run,把脚本发同事才发现他没装 Dart 直接报错。要分发就先 dart compile exe 编成单文件,对方零依赖。
- user: 后端老兵, category: 注意, comment: 异步代码里报错栈默认是断的,根本没法排。包一层 Chain.capture 再用 chain.terse 输出,用户看到的错误才短且可读。
- user: 写定时脚本的, category: 坑, comment: 曾在底层函数 catch 住异常只打日志,命令失败仍 exit 0,上游定时任务全误判成功。失败必须写 stderr 并返回非零退出码。
- user: 测试工程师, category: 妙用, comment: test_descriptor 建临时文件,test_process 真起进程跑命令,连输出流、退出码、文件改动都能断言,比 mock 单测可信一个量级。
- user: 想跨平台分发的独立开发者, category: 注意, comment: 交叉编译只支持 Linux 目标,Windows 和 macOS 版必须去对应系统上编。我在 Mac 换了一堆参数试错,最后才明白这个硬限制。
