# caveman-review (`juliusbrussee/caveman/caveman-review`)

## blackbox

**function**: 看代码改动, 挑出问题, 每个问题一句话: 哪一行、错在哪、怎么改, 可直接贴进 PR 评论。

- input: 一段代码改动 + 一句「review 一下」, output: 一组短评, 一行一条, 如: L42: 🔴 bug: user 可能为 null, 取 .email 前先加判断。
- input: 涉及多个文件的大改动, output: 每条短评带文件名和行号, 并标好严重度: 🔴 会出事故 / 🟡 埋雷隐患 / 🔵 小建议。
- input: 一段含安全漏洞的代码, output: 漏洞那条展开成完整段落, 讲清风险和修法; 其余问题仍是一行一条。
