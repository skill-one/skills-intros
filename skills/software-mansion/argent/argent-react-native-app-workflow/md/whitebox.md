# argent-react-native-app-workflow (`software-mansion/argent/argent-react-native-app-workflow`)

## whitebox

- 先读配置 (强制第一步): 从 argent-environment-inspector 结果及 package.json 脚本、metro.config.js 探明自定义命令与端口, 不直接跑 react-native 默认命令
- 检查并启动 Metro: 先 lsof 查端口占用、用 debugger-status 工具确认占用者是否已是 Metro, 再用项目的自定义 start 脚本启动
- 启动目标设备并装 App: 用 list-devices/boot-device 确定模拟器, 跑项目的 run 脚本并显式指定设备; Android 还需执行 adb reverse tcp:8081 让设备能连到宿主机的 Metro
- 验证运行: 用 debugger-status 确认 Metro 可达, JS 报错走 debugger-log-registry 拿日志文件再 grep, 或用组件树/screenshot 定位问题
- 把摸清的构建/运行 workflow 存入项目记忆, 下次免于重新探查

- 配置优先原则: 任何命令执行前必须先探明项目自定义脚本、端口与 Pods/node_modules 状态, 自定义脚本永远优先于 npx react-native 默认命令; 项目结构混乱则先问用户而不是猜
- Metro 单实例校验: 端口被占时, lsof 只能证明有进程监听, 须再用 debugger-status 工具做结构化判定 (connected/no_app_connected=是 Metro, metro_not_running=占用者不是 Metro); 清理须用 stop-metro 工具且需用户确认
- 按变更类型选择刷新策略: 只改 JS/React → debugger-reload-metro 热重载不重建; 改原生代码或 pod install → 重新 build; 构建失败按 清理缓存→重装依赖→pod deintegrate 阶梯递进, 连续失败 2-3 次即停止并求助用户
