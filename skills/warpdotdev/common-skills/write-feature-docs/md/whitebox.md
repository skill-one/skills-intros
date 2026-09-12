# write-feature-docs (`warpdotdev/common-skills/write-feature-docs`)

## whitebox

- 向工程师要 spec ID (Linear 票号 / GitHub issue / kebab-case 名称), 读 specs/<id>/PRODUCT.md 为主、TECH.md 为辅; TECH.md 中疑似内部实现的内容先标记待确认, 都没有则走无 spec 的代码调研路径
- 用 GitHub CLI (gh) 亲自到代码库验证 spec 里的技术声明: feature flag 名、UI 文案、Settings 路径、CLI 命令/快捷键、关联功能, 以及 spec 作者的 GitHub handle; 验证不了的标记为 [UNVERIFIED]
- 打印内容设计方案 (读者/目标/内容类型) 并停下等工程师确认; 确认后再打印大纲 (含 ✅已验证 / ⚠️待确认 两栏) 再停下等第二次确认
- 按确认过的内容类型套用 docs 仓库的模板生成完整 MDX 草稿; 如 computer use 工具可用, 尝试截图 (预测→截图→核对, 每张最多试 2 次), 失败则留 [TODO: docs reviewer] 占位
- 在 warpdotdev/docs 开 draft PR, @ docs 团队和 spec 作者等评审

- 双源解析 + 安全过滤: PRODUCT.md (用户行为/what/why) 驱动文档内容, TECH.md (实现) 只作辅助, 其中数据库 schema、内部服务名、私有 API 一律先标记、确认安全才写入; 两道独立的确认闸门 (先方案后大纲) 防止读者在未定稿时就锚定在大纲上
- gh CLI 代码自证 + 输入校验: 用 gh search code / gh api / gh pr list 核实 spec 声明, 尽量压缩工程师要人工确认的事项; 所有拼进 shell 命令的 token/spec ID 先过白名单正则 (仅字母数字、连字符、下划线), 不合法就跳过该命令; 找作者 handle 走多级降级链 (Co-authored-by → sync PR URL → PR 搜索 → commit 邮箱), 全程跳过 bot
- 模板驱动生成 + 风格硬规则: 内容类型决定用 docs 仓库 .agents/templates/ 里哪个模板; 标题写 frontmatter 不写正文 H1 (Starlight 渲染避免重复), 括号占位指令交付前必须删光; 截图有质量门 (文字可读、主体聚焦、无敏感信息、非加载态), 两次失败就丢弃留占位符
