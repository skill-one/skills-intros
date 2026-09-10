# cavecrew (`juliusbrussee/caveman/cavecrew`)

## blackbox

**function**: 帮你干三种代码活: 定位代码在哪、做小改动 (≤2 个文件)、检查改动有没有 bug —— 且无论活多大, 回给你的永远是几行短小、带行号、一眼能扫完的结构化清单, 而不是长篇大论。

- input: 一句提问: "这个项目里 retry 逻辑定义在哪? 哪些地方在调用它?", output: 几行定位清单, 如 `src/net/client.py:42 — retry — 被 3 处调用`; 找不到就回一句 "No match."
- input: 一个明确的小改动: "把 src/config.py 里的 timeout 从 30 改成 60", output: 一行改动回执: `src/config.py:8 — timeout 30→60`, 附 `verified: 已复读确认`; 活太大或说不清则直接回 `too-big.` / `needs-confirm.`
- input: 一份改动记录 (diff, 即代码前后对比) 或分支名, 加一句 "帮我查查有没有 bug", output: 问题清单, 如 `src/api.py:17: 🔴 高: 空指针. 建议加判空.`, 末尾汇总 `totals: 1🔴 2🟡 0🔵 1❓`; 没问题则回 "No issues."
