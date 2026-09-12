# proactive-agent (`halthelobster/proactive-agent/proactive-agent`)

## whitebox

- 启动对齐: 首次检测 ONBOARDING.md, 提问认识用户并自动生成 USER.md/SOUL.md; 之后每个会话先读 SOUL.md、USER.md 和近期记忆, 校验自己没跑偏
- 每条用户消息先过 WAL 协议: 扫描其中的纠正/专名/偏好/决策/具体数值, 先写入 SESSION-STATE.md, 再开口回复
- 涉及过往内容时走统一搜索: memory_search (语义搜索) → 会话记录 → 会议笔记 → grep 精确匹配兜底, 全部落空才承认不知道
- 上下文用到 60% (用 session_status 查看) 进入危险区: 此后每条交互都追加落盘到 memory/working-buffer.md; 若被截断/压缩, 按固定顺序读 buffer → SESSION-STATE.md → 日记恢复现场, 而不是问用户'我们刚才在干嘛'
- 定期心跳: 按清单做安全扫描、自修复、把日志蒸馏进 MEMORY.md, 并主动构建用户没要求的东西 (对外发送类动作必须先获批准)

- 文件即存储, 三级记忆全是 Markdown: SESSION-STATE.md 当 RAM (每条消息更新)、memory/日期.md 存每日原始日志、MEMORY.md 存长期蒸馏结论; WAL 的触发器是用户输入内容本身 (出现纠正/专名/决策等关键词即触发), 不靠模型自觉记住
- 危险区缓冲: 上下文超 60% 后强制逐条落盘 working-buffer.md (文件不会被上下文压缩吞掉); 压缩截断后先读 buffer 提取重要上下文, 再整合进 SESSION-STATE.md 并清空
- 自进化带护栏: 改自己规则前先过 VFM 加权评分 (高频 3x + 减少失败 3x + 减轻用户负担 2x + 省自身成本 2x, 加权 <50 拒绝执行), 同时遵守 ADL 禁改清单; 优先级排序: 稳定>可解释>可复用>可扩展>新颖
- 外部依赖很轻: session_status (查上下文占比)、memory_search (语义搜索工具)、grep (精确匹配兜底)、shell 脚本 (scripts/security-audit.sh 安全审计)、cron (定时心跳提醒); 不依赖任何模型 API 或代码库 — 整套技能是纯 Markdown 协议 + 少量脚本
