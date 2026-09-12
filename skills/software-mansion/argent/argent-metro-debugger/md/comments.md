# argent-metro-debugger (`software-mansion/argent/argent-metro-debugger`)

## comments

- user: 第一次用的新手, category: 坑, comment: 拿着实体 iPhone 调了一下午，debugger 全被拒。后来看文档才知物理 iPhone 一律不支持，必须先把 app 跑进模拟器再连。
- user: 安卓端开发, category: 坑, comment: 安卓上 Metro 老连不上，restart-app 也没用，八成是 adb reverse 没做或掉了：adb -s 序号 reverse tcp:8081 tcp:8081，设备重启后要重跑。
- user: RN 前端老兵, category: 妙用, comment: component-tree 自带包围盒和点击坐标，把坐标直接喂给 inspect-element，一步定位到源码行号，不用在模拟器里瞎点猜位置。
- user: Electron 桌面端开发, category: 妙用, comment: 以为只有 RN 能用，结果 Electron 开着 CDP 端口也连上了，读日志、执行 JS 都行；但组件树那几个工具会被拒，仅限 RN。
- user: 接手别人 RN 项目的开发, category: 注意, comment: 连不上别死磕 connect：先跑 debugger-status，它不报错、直接返回 reason 和 guidance 照做即可；no_app_connected 就 restart-app 后再试一次。
- user: 后端转前端的, category: 坑, comment: grep '[L:42]' 会匹配全部行——方括号是正则字符类。搜日志锚点记得用 grep -F；日志超一万条别自己翻，丢给 Explore 子代理。
