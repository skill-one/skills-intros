# xcode-project-setup (`firebase/agent-skills/xcode-project-setup`)

## whitebox

- 环境校验: 先跑 `swift --version` 确认本机 Swift 工具链可用, 并确认目录下已有 .xcodeproj (没有则停下让用户手动建项目)
- 定位 skill 自带的 Swift 配置包 scripts/xcode_spm_setup 的绝对路径
- 执行 `swift run --package-path <skill路径>/scripts/xcode_spm_setup xcode_spm_setup <项目.xcodeproj> <仓库URL> <版本> [--plist 可选配置文件] <模块名...>
- 脚本自动完成两件事: 向项目注入 package 仓库依赖, 并把指定 product 模块挂到主 target 的 Frameworks 构建阶段 (等效于手动在 General > Frameworks 里点 +)
- 若是 Firebase, 脚本自动给 OTHER_LDFLAGS 注入 -ObjC 标志; --plist 指定的文件 (如 GoogleService-Info.plist) 被挂入 resources 构建阶段; 已存在的包/文件自动跳过 (幂等)

- 纯 Swift 脚本改写 .pbxproj: 明令禁止 Ruby/xcodeproj gem, 也禁止 sed/文本解析直接改 .pbxproj, 更不手动改 .pbxproj 添加源文件——新 .swift 文件靠 Xcode 的 folder synchronization 直接落盘即生效
- -ObjC 链接标志注入: Firebase iOS SDK 依赖内部 ObjC categories 和 +load 方法, 静态链接时会被 Apple linker 剥掉导致运行时崩溃, 脚本加 Firebase 时自动注入 -ObjC 到 OTHER_LDFLAGS 兜底
- 外部依赖: 仅需本机 macOS + Swift 工具链 (swift run 编译并执行自带脚本); 不调用任何网络 API, SDK 版本号需预先查 Firebase GitHub releases 取最新版填入命令行参数; 脚本幂等, 重复执行安全
