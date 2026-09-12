# skill-development (`anthropics/claude-code/skill-development`)

## whitebox

- 向用户澄清具体用例: 技能应支持什么功能、用户说什么话应触发它
- 逐条分析用例, 规划可复用资源: 反复重写的代码→scripts/, 需查的文档→references/, 输出用的文件→assets/
- 用 mkdir/touch 在插件的 skills/ 目录下创建技能骨架 (SKILL.md + 所需子目录)
- 按规范填充内容: YAML frontmatter (第三人称+触发短语) + 祈使句式正文, 并删除不用的示例文件
- 按校验清单检查结构与内容, 可调用 skill-reviewer agent 复审, 安装后用 cc --plugin-dir 实测触发

- 渐进式披露 (progressive disclosure): 三级加载控制上下文开销 — name+description 元数据 (~100 词) 常驻, SKILL.md 正文 (<5k 词) 仅触发时加载, references/examples 按需加载且不限量; 脚本可直接执行、无需读入上下文
- frontmatter 驱动触发与分流: SKILL.md 头部 YAML 的 description (须第三人称+具体触发短语) 决定技能何时被 Claude Code 自动发现并加载; 正文超过 1 万词的 references 须附 grep 搜索模式以便按需检索
- 依赖的外部工具: Claude Code 插件系统 (自动扫描 skills/ 目录发现技能, cc --plugin-dir 本地测试) 和 skill-reviewer agent (按最佳实践审查); 无额外第三方库或模型 API
