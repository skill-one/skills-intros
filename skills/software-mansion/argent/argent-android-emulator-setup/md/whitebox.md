# argent-android-emulator-setup (`software-mansion/argent/argent-android-emulator-setup`)

## whitebox

- 调用 list-devices 枚举设备, 筛出 platform 为 android 且 state 为 device 的就绪设备, 取第一个 serial (设备编号) 供后续使用
- 若无就绪设备, 调 boot-device 并传入 AVD 名 (预创建的虚拟机配置) 启动模拟器, 等待开机完成 (热启动约 30s, 冷启动 2-10 分钟)
- 若用于 React Native 调试, 执行 adb reverse tcp:8081 tcp:8081, 让设备能访问宿主机上的 Metro (RN 的 JS 打包服务); 设备重启后需重跑
- 后续所有交互 (tap / swipe / describe / screenshot / launch-app 等) 统一把该 serial 作为 udid 传入, 完成任务

- 启动加速与自愈: boot-device 先探测 AVD 的 default_boot 快照, 能在紧时限内恢复则走热启动, 否则降级为完整冷启动; 任一阶段失败会杀掉自己拉起的模拟器进程, 保证下次调用从干净状态开始
- 平台自动分发: 交互工具按传入 id 的形状自动识别 iOS/Android 并路由, 调用方无需声明平台; 底层依赖 PATH 上的 adb (Android SDK Platform Tools) 与 Android Emulator 二进制
- TV 识别与工具分流: 通过系统 feature 列表 (而非 serial 名) 判定 Android TV / leanback 设备, 打上 runtimeKind: tv 标记; 此类设备禁用触摸手势, 必须改用 describe / tv-remote / keyboard 等焦点驱动工具
