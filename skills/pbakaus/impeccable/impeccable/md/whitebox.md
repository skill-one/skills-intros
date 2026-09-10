# impeccable (`pbakaus/impeccable/impeccable`)

## whitebox

- 会话开头跑一次 `scripts/impeccable context` 启动器, 读入 PRODUCT.md、DESIGN.md、surface brief 和平台指南作为设计约束
- 路由用户请求: 显式/隐含的子命令加载 Commands 表对应 reference/*.md 手册; 新界面走 reference/new-work.md; 两者都不匹配则当通用设计任务处理
- 编辑任何 UI 代码前, 先读 reference/craft-floor.md (质量底线与禁令清单)
- 按请求对应的 mode (Persuade/Operate/Read/Experience) 和 brief 执行设计/编码工作
- 有界验证收尾: 构建 → 一轮批量检查 (桌面+移动截图) → 一批修完 → 最多再确认一轮即停止打磨

- 上下文装配依赖自包含 launcher 二进制 (首run自动下载一次, 不需 Node 等运行时); launcher 不可用时先告知用户, 降级为直接读已有的 PRODUCT.md/DESIGN.md 继续干活, 不臆造缺失上下文
- 指令分发是纯文档路由: 每个子命令对应一份 reference/*.md 操作手册 (如 polish/bolder/harden), 可通过 `pin` 生成独立快捷命令, `hooks` 挂设计检测器在 UI 文件编辑后自动跑检测
- 验证策略有硬性预算上限 (bounded passes), 明确禁止开放式自检循环 — 防止无限打磨烧用户钱; 未运行完 context 不阻塞已获许可的编辑
