# swiftui-expert-skill (`avdlee/swiftui-agent-skill/swiftui-expert-skill`)

## comments

- user: SwiftUI 新手, category: 坑, comment: 把数组下标当 ForEach 的 id,数据一增删界面就错乱。改成稳定唯一标识后正常——它的检查清单直接点名这类 bug,贴代码给它审一遍很值。
- user: 性能排查老手, category: 妙用, comment: 丢 .trace 文件给它,用 --fanin-for 查出某列表每秒被 UserDefaultObserver 触发重绘,修掉一处源头,全页卡顿消失。
- user: 第一次做性能分析, category: 坑, comment: 在模拟器录 trace,SwiftUI 轨道全是空的。先 --list-devices 看设备类型:模拟器要换 Time Profiler 模板才有数据。
- user: 老项目维护者, category: 注意, comment: 苹果的"软废弃"API 还能用。我让它改 bug 时顺手迁移旧写法,diff 大到没法审。现在只让它动本次任务相关的废弃 API。
- user: 独立开发者, category: 妙用, comment: 想上 iOS 26 的 Liquid Glass,它不会硬上,自动加 #available 门控并给旧系统配降级方案,低版本用户不受影响。
- user: 后端转 iOS, category: 启发, comment: 以前优化靠猜,现在先看 coverage 百分比和 top_sources,搞清"谁在让视图刷新"比"哪行代码慢"更值,排查方向整个变了。
