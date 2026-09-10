# impeccable (`pbakaus/impeccable/impeccable`)

## whitebox

- 运行 `impeccable context` 启动脚本，一次性加载项目上下文：PRODUCT.md、DESIGN.md、对应界面简报及原生平台指南
- 按请求匹配操作手册：显式命令（如 critique/polish）查 Commands 表加载对应 reference 文档；新界面/换视觉风格则走 new-work.md
- 在动任何 UI 代码之前，立即读 craft-floor.md —— 质量底线、绝对禁令和检测器抓不到的手感规则
- 按手册执行设计/构建：先选模式（Persuade/Operate/Read/Experience）定优先级，遵循简报优先原则
- 有界验收：桌面+移动端截图一次性批量检查，缺陷一轮内全部修复，最多再确认一轮即停止打磨

- 上下文加载：自包含二进制启动器，首次运行时下载，无需 Node 等运行时；启动器失败时降级为直接读 PROJECT/DESIGN 文件并继续
- 命令路由：Commands 表把请求映射到对应 reference markdown（评估/精修/增强/修复各有手册）；新界面走 init→new-work，既有代码小幅精修走现有实现
- 验证有硬上限：优先跑应用截图，跑不起来则用已提交的视觉回归基准图；批量修缺陷 + 明确封顶一轮确认，避免无止境自检烧钱；另有可选 hook 在 UI 文件编辑后自动跑设计检测器
