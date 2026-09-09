# azure-resource-visualizer (`microsoft/azure-skills/azure-resource-visualizer`)

## whitebox

- 用户未指定资源组时: 列出所有资源组 (含位置) 供其编号选择, 等用户确认后才继续
- 查询该资源组内全部资源, 逐一提取类型、SKU/层级、区域、网络配置、托管身份与依赖
- 映射资源间关系: 网络连接 (VNet/子网/NSG/专用终结点)、数据流向、身份访问、配置引用 (如 App Settings → Key Vault)
- 构建 Mermaid 架构图: 用 subgraph 按层分组, 节点标注 SKU 等配置, 每条连线加说明, 密钥/连接串等敏感值一律用占位名
- 套用模板写出 markdown 文件 [资源组名]-architecture.md: 概述 + 资源清单表 + 图 + 关系详解 + 建议

- 数据获取: 优先 Azure MCP 工具 (intent 式调用: list resource groups / list resources in group / get resource details), 复杂查询回退 `az` CLI (如 az resource list、az network vnet show); 跨订阅批量盘点用 Azure Resource Graph 查询
- 图生成规则: Mermaid graph TB (纵向) 或 graph LR (横向, 适合宽架构), 节点用 <br/> 嵌入配置细节, 连线区分 --> (数据流/依赖)、-.-> (可选)、==> (关键路径), 输出前校验语法有效
- 硬性约束: 只读分析 (绝不修改/删除 Azure 资源), 不遗漏任何资源, 不凭空假设未经验证的关系; 产出的 markdown 结构为 H1/H2 层级 + 表格清单 + ```mermaid 代码块
