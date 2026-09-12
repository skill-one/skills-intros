# argent-native-profiler (`software-mansion/argent/argent-native-profiler`)

## whitebox

- 确认目标 App 已启动后调用 native-profiler-start (只需 device_id), 工具自动探测运行中的 App 并开始录制 (iOS 走 xctrace, Android 走 perfetto)。
- 用户操作 App 或用模拟器工具驱动目标场景后, 调用 native-profiler-stop 停止录制并导出数据 (iOS 发 SIGINT 给 xctrace 导出 XML, Android 等 perfetto 守护进程退出后 adb pull .pftrace)。
- 调用 native-profiler-analyze 解析导出的 trace, 返回按严重度排序的瓶颈报告 (CPU 热点 / UI 卡顿 / 内存泄漏)。
- 调用 profiler-stack-query 向下钻取: hang_stacks 查卡顿调用链、function_callers 查可疑函数、thread_breakdown 查线程分布、leak_stacks 查泄漏分配栈。
- 呈现发现后询问用户继续排查 / 实施修复 / 停止; 修复后重新录制同一场景, 用 profiler-load 从磁盘重载历史 trace 对比前后指标。

- iOS 后端: Xcode Instruments 的 xctrace 命令行 (依赖 PATH 中的 Xcode CLI 工具), 在已启动的模拟器上录制; 泄漏归属缺失 (<Call stack limit reached>) 时, 带 malloc_stack_logging: true 冷启动重录以获取真实分配回溯 (有额外开销, 仅用于泄漏归因)。
- Android 后端: adb shell perfetto 采集 + 进程内 WASM trace-processor 引擎解析; 提供逐卡顿 jank 原因码、主线程 blocked_function 归因、GC 重叠标注和 RSS 增长信号 (仅作内存压力提示, 非确认泄漏); App 需 debuggable 或声明 profileable 才能采到调用栈。
- 结果分级规则: CPU 函数占比 >15%、所有 UI 卡顿、已归属泄漏 = RED; 3–15% 与未归属泄漏 = YELLOW; run-to-run 波动属正常, 只有两轮以上方向一致或 >15% 变化才视为有效信号。
