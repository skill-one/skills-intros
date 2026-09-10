# golang-cli (`samber/cc-skills-golang/golang-cli`)

## whitebox

- 先判定模式: 新建 CLI 走 Build、给现有 CLI 加命令/补全走 Extend (先读现有命令树)、查错走 Review (对照 Common Mistakes 表逐项核对)
- Build 时按 skill 章节顺序执行: 先搭项目结构 — cmd/myapp/ 下每条命令一个文件, main.go 极简只调 Execute()
- 写 root 命令: 必设 SilenceUsage/SilenceErrors, 用 PersistentPreRunE 保证每次子命令执行前先初始化 Viper 配置
- 添加子命令与 flag, 每个可配置 flag 都 viper.BindPFlag, 使取值自动按优先级回落 (flag > 环境变量 > 配置文件 > 默认值)
- 补齐版本注入、退出码、stdout/stderr 分离、信号处理、shell 补全, 再写 CLI 测试收尾; cobra/viper 具体 API 查官方文档

- 配置分层: Viper 按 CLI flag → 环境变量 (必须 SetEnvPrefix 加前缀防撞名) → 配置文件 → 代码默认值 的优先级合并取值; 配置文件视为可选, 缺失时忽略 ConfigFileNotFoundError 而非崩溃
- 解析与校验: pflag (经 Cobra) 解析 flag; 参数用 Cobra 内置校验器 (NoArgs/ExactArgs/RangeArgs 等) 加 MarkFlagRequired/互斥约束; 错误经 SilenceUsage 抑制 usage 噪音, 并按 Unix 约定映射退出码 (0 成功 / 1 一般错误 / 2 用法错误 / 128+N 信号)
- 依赖栈: spf13/cobra (命令树) + spf13/viper (配置) + spf13/pflag (解析); 输出用 fatih/color (非终端自动去色) 与 tablewriter, 交互用 bubbletea; 发布靠 go build -ldflags 注入版本 + goreleaser; 测试经 cmd.OutOrStdout()/ErrOrStderr() 重定向捕获; 更深的 cobra/viper 细节转交专用 skill (golang-spf13-cobra / golang-spf13-viper)
