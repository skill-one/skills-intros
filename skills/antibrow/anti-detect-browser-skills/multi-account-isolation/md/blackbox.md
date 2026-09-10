# multi-account-isolation (`antibrow/anti-detect-browser-skills/multi-account-isolation`)

## blackbox

**function**: 帮你验证一台电脑上的多个浏览器账号环境是不是真的互不关联, 并把会导致平台判定关联的具体漏洞逐个揪出来。

- input: 几个浏览器环境 (profile) 及各自代理的清单, 比如「fixture-us-01 配美国代理 A, fixture-de-01 配德国代理 B」, output: 一份逐项体检报告: 每个环境的时区是否和出口 IP 所在地一致、浏览器通话功能 (WebRTC) 是否泄漏了真实地址、指纹数据是否稳定、有没有两个环境共用同一 IP 或登录数据, 每项标注「通过 / 不合格 + 原因」
- input: 一句现象描述: 「明明每个账号分开环境分开登录, 平台还是判定它们关联」, output: 按可能性排序的原因结论, 例如: 两个环境用了同一个出口 IP、时区和 IP 位置对不上、两个环境混用了同一份存储目录, 每条附对应的修法
- input: 一个指纹检测网站 (whoer / CreepJS / Pixelscan) 的检测结果页面, output: 一段人话解读: 哪些数值互相打架 (比如 IP 显示美国、时区却是柏林)、各自意味着什么风险、下一步先改哪一处
