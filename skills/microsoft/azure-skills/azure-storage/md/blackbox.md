# azure-storage (`microsoft/azure-skills/azure-storage`)

## blackbox

**function**: 我是 Azure 云存储顾问：帮你选对存储方案（冷热档位、服务类型），并能直接列出、上传、下载你云端存储里的文件。

- input: 「我的备份文件一年才看一两次，用哪种存储最省钱？」, output: 一份热/冷/归档档位的对比说明 + 针对你场景的推荐结论（含费用取舍）
- input: 存储账号名称（如 mystorage123）, output: 该账号下所有容器（云端文件夹）的清单
- input: 本地文件路径 + 目标容器名（或给出要下载的文件名）, output: 文件上传成功的确认结果（或下载到本地的文件）
