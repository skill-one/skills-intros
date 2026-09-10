# dbs-agent-migration (`dontbesilent2025/dbskill/dbs-agent-migration`)

## whitebox

- 审计: 扫描 CLAUDE.md / AGENTS.md / SOURCE_OF_TRUTH.md / 项目内 skills/ 及 4 个宿主 bridge 目录 (~/.claude/skills, ~/.codex/skills, ~/.grok/skills, ~/.agents/skills), 判定项目规则层类型 (A~D) 和宿主覆盖情况
- 规则迁移: 把平台无关规则拆入 AGENTS.md, 宿主专属规则留在薄壳 (如 CLAUDE.md), 删过时重复内容; 写盘前先向用户确认新建/改写哪些文件、保留与删除什么
- 定真源: 已有 skills/ 则定为唯一真源并排除备份/示例; 没有则扫描 *skill*.md 类候选生成清单, 用户逐项确认后才新建 skills/
- 统一命名并生成 bridge: 按规范名用固定模板为 Claude/Codex/Grok/通用 Agents 生成薄指针文件 (Grok 必带 user_invocable: true; ~/.agents/skills 优先软链指向真源)
- 验证: 逐项检查 AGENTS.md 可独立工作、frontmatter 补齐、bridge 指回真源、Grok bridge 的 user_invocable、readlink 无悬空软链、多端集合一致, 输出完成度与维护方式

- 规则层分类引擎: 纯文件系统探测 (无 API/库/模型依赖), 按关键文件是否存在把项目归为 A (齐全)/B (只有 CLAUDE.md)/C (只有 AGENTS.md)/D (skill 散落) 四类, 叠加宿主覆盖判定 (单端/多端/不一致), 以此决定后续动哪一层; 不假设项目已规范
- 真源 + 薄桥接生成: skills/ 为唯一真源, bridge 只做入口不存长逻辑。Grok bridge 用固定模板, 强制校验 frontmatter 含 user_invocable: true、description 提及 /触发词、绝对路径用正斜杠; Claude/Codex bridge 模板用 source_of_truth 字段 + bridge_mode: passthrough; ~/.agents/skills 优先写软链不复制, 更新软链后用 readlink 验证指向; 目标已有真实目录则不覆盖, 上报让用户确认迁出
- 命名收敛 + 确认闸门: 每个 skill 只留一个 kebab-case 可调用名 (正式 Skill 加 dbs- 前缀), 硬约束目录名 = frontmatter name = bridge 目录名 = 斜杠命令, Codex openai.yaml 的 display_name 必须与英文标准名一致; 各阶段写盘前需用户确认, 未授权写宿主目录时只给预览; Phase 6 以 8 项清单收口 (含悬空软链/悬空引用检查)
