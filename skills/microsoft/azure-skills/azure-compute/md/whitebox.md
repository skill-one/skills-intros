# azure-compute (`microsoft/azure-skills/azure-compute`)

## whitebox

- 接收请求, 对照路由表分类意图: 推荐/比价/定价 → VM Recommender; 创建/部署裸 VM/VMSS → VM Creator; 容量预留 → Capacity Reservation; 机器注册/监控 → Essential Machine Management
- 意图不明时先提问澄清, 同时划清边界: 应用部署 (Docker/web app/API/serverless) 路由给 azure-prepare, 本 skill 只管裸 VM/VMSS 基础设施
- 打开匹配的 workflow 文件 (workflows/*.md), 强制规则: 严禁绕过 workflow 直接进入 references/*
- 只加载该 workflow 明确要求的 reference 支撑文件, 不做多余加载
- 按 workflow 执行; 创建类意图优先调用 Azure 工具 compute_vm_list-skus / compute_vm_list-images / compute_vm_check-quota

- 强制 workflow-first 路由: 先按路由表分类意图 → 打开 workflow 文件 → 按需加载 references; reference 文件是支撑材料而非入口
- 双重消歧: 意图不清时提问澄清; 与 azure-prepare 分工——应用部署让位给 azure-prepare, vm-creator 仅处理裸 VM/VMSS 基础设施
- 外部依赖: Azure MCP 工具集 (compute_vm_list-skus / compute_vm_list-images / compute_vm_check-quota); VM 创建意图下明确优先于 mcp__azure__get_azure_bestpractices
