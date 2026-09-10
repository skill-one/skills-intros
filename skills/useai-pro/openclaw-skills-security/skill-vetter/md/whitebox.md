# skill-vetter (`useai-pro/openclaw-skills-security/skill-vetter`)

## whitebox

- 读取目标 skill 的 SKILL.md, 核对元数据: name 是否有仿冒拼写、version 是否符合 semver、description 是否名实相符、author 是否可识别
- 对照权限风险表逐项评估 fileRead / fileWrite / network / shell, 专门拦截 network + shell 组合 (该组合可通过 shell 命令外传数据)
- 扫描 SKILL.md 正文, 按 Critical / Warning / Informational 三档匹配红旗规则 (如引用 ~/.ssh、base64 混淆、要求 sudo、提示注入)
- 将 skill 名称与已知合法 skill 名对比, 检测增删字符、字符调换、同形字等仿冒 (typosquat)
- 输出固定格式的审查报告: 判定 SAFE / WARNING / DANGER / BLOCK + 各权限裁决 + 红旗清单 + 安装建议

- 纯静态规则审查, 无外部依赖: 按元数据中的 permissions 声明 (仅 file-read), 不联网、不写文件、不执行 shell, 全部判定基于内置检查清单和风险等级表
- 红旗分级决策: Critical 项 (凭证文件引用、curl/nc/bash -i、base64 混淆、禁用安全机制的指令、外部服务器引用) 触发即 BLOCK; Warning 项 (/**/* 通配、改 .bashrc/crontab、sudo、'ignore previous instructions' 类注入) 标记待人工复核
- 信任层级加权: 按来源分级 (官方 > UseClawPro 验证 > 知名作者 > 高下载量社区 > 未知作者), 未知来源执行完整审查; 存疑时建议先在沙箱运行
