# dbs-save (`dontbesilent2025/dbskill/dbs-save`)

## blackbox

**function**: 把这次对话里聊出来的诊断结论存成本地存档，下次回来能接着上次的进度继续，不用从头再讲一遍。

- input: 对话里聊完一轮诊断后，说一句「保存这次诊断」, output: 本地多了一份存档文件，并收到一行回执：存在哪了、当前项目下共有几份、下次怎么接着用
- input: 「/dbs-save list」, output: 一份清单：每份存档的日期、标题、状态（进行中/已结论）和来源，例如「5月1日 · 定价拉到10倍价差 · 已结论」
- input: 「/dbs-save location」, output: 一句话告诉你存档现在放在电脑的哪个位置，方便你找到文件或备份
