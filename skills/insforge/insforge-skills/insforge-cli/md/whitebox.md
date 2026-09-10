# insforge-cli (`insforge/insforge-skills/insforge-cli`)

## whitebox

- 连接先行: 任务需要后端时先查 current/whoami, 未登录则 login (无浏览器场景走两步设备登录), 未关联项目则 link/create——拿到真实项目 URL 和密钥前不写任何代码, 不用占位凭证
- 记忆召回: 对已关联项目的非琐碎任务, 先跑 memory list (无 AI 调用) 召回相关的历史决策与坑
- 路由决策: 按 skill.md 的需求→命令域→references/*.md 路由表选命令; 非琐碎数据库工作必须先读 references/database/* 再动手写迁移
- 执行: 统一经 npx -y @insforge/cli <command> 执行; schema 变更优先 db migrations new + up --all, 检视/小修用 db query; --json 拿结构化输出, --yes 用于已获确认的破坏性操作
- 收尾闭环: 决策和踩坑当场 memory remember; 若卡点是 InsForge 自身问题, 用 feedback 上报后带 workaround 继续任务

- 单一执行通道 + 机器可读状态: 一切操作经 npx 拉起的 @insforge/cli 包 (强制 -y 防止 TTY 确认阻塞, 禁止全局安装); 认证与项目上下文可被 INSFORGE_ACCESS_TOKEN / INSFORGE_PROJECT_ID 覆盖; 退出码 0~5 区分 成功/通用错误/未认证/未关联/未找到/无权限, 供上层程序判断
- 路由表 + 参考文档分层校验: Command Routing 表把需求映射到命令域和 references 文档; 数据库操作受硬规则约束——只在 public schema 动应用对象 (auth/storage 等系统 schema 只读引用), RLS 用 auth.uid() 做所有权校验且 INSERT/UPDATE 必须带 WITH CHECK, 跨表检查走 public 下的 SECURITY DEFINER 辅助函数, 底层是 PostgreSQL (迁移/RLS/pgvector)
- 安全与降级约束: API key 视为全权限 admin key, 只留在服务端不进前端环境变量; 优先 CLI 命令而非裸 HTTP 调后端; config apply 报不支持的字段就如实上报, 不绕过 CLI 直连 API
