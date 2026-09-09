# azure-quotas (`microsoft/azure-skills/azure-quotas`)

## blackbox

**function**: 查清你的 Azure 订阅在某个区域还能开多少资源(虚拟机、公网 IP、存储等),并在配额不够时帮你申请提高上限。

- input: 「看看 eastus 区域还能开多少台 DSv3 虚拟机」, output: 一张表: 该类资源的上限 / 已用 / 剩余可用, 如 上限 350 · 已用 50 · 还能开 300 台
- input: 「我想部署 20 核虚拟机, 帮我挑个配额够用的区域」, output: 几个候选区域的对比清单, 直接标出哪个区域容量够、哪个不够
- input: 「部署时报错 QuotaExceeded, 怎么办?」, output: 指出超的是哪项配额、差多少, 并帮你提交提额申请、查询审批进度(多数申请几分钟内自动通过)
