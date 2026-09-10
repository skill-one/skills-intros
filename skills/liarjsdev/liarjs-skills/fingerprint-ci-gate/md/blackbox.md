# fingerprint-ci-gate (`liarjsdev/liarjs-skills/fingerprint-ci-gate`)

## blackbox

**function**: 给你的自动构建流水线 (CI) 加一道"浏览器伪装体检": 每次构建时测一下自动化浏览器会不会被网站识别出来, 伪装得分不达标或比上次明显退步, 就让构建直接失败——把"流量被悄悄封禁"这种几周后才发现的问题, 拦在发布之前。

- input: 在 GitHub Actions 配置里加一条扫描命令, 并指定及格线 (如 --min-score 60) → 看到的输出, output: 该步骤打印本次伪装得分; 高于 60 流水线照常通过, 低于 60 则整条流水线标红失败, 问题当场暴露
- input: 两份扫描结果文件: baseline.json (上次存档的合格版本) 和 scan.json (本次新扫的) → 看到的输出, output: 一份差异清单, 只列出前后'状态变了'的检查项, 没变化的一概不提——一眼看出是哪次改动让伪装退化了
- input: 扫描命令后加一个参数, 指定结果存到 scan.json → 看到的输出, output: 一个记录本次完整扫描结果的 JSON 文件, 随构建自动保存; 即使构建失败, 事后也能下载回来查当时的数据
