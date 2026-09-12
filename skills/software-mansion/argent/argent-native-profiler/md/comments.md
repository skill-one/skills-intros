# argent-native-profiler (`software-mansion/argent/argent-native-profiler`)

## comments

- user: iOS 独立开发者, category: 坑, comment: 插着真机测了半天才发现不支持, 只能用模拟器, 白忙一场。开始前先跑 xcrun xctrace version 确认 Xcode 命令行工具装好了, 否则录到一半才报错。
- user: Android 客户端开发, category: 注意, comment: release 包没加 <profileable android:shell="true"/>, CPU 占用有数据但调用栈抓不到, 定位不到函数。manifest 加上这句或换 debuggable 包, 才能拿到完整栈。
- user: React Native 开发, category: 坑, comment: 热点里 Hermes、JSLexer 占大头, 差点去折腾运行时。后来才明白那是采集工具自身开销, 评估前先剔除这几类条目, 别把优化做在 profiler 头上。
- user: 性能优化老兵, category: 妙用, comment: 改代码前先用 create-flow 把滑动操作录成脚本, 修完后 flow-execute 回放同一操作, 再用 profiler-load 调出旧 trace 对比。交互路径一致, 修复效果才有说服力。
- user: 第一次用的新手, category: 坑, comment: 没先启动 App 就开始录, 结果什么都没抓到; 后来模拟器同时跑了 dev 和 staging 两个包, 它不知道测哪个。现在都是先启动目标包、关掉多余的再录。
- user: 客户端 QA, category: 注意, comment: 单次结果别急着下结论: 同一场景我跑两次 CPU 差了七八个点。两次方向一致、或变化超 15% 才算数; 接口返回数据量不同也会影响渲染负载, 对比时尽量固定数据。
