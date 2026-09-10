# golang-modernize (`samber/cc-skills-golang/golang-modernize`)

## blackbox

**function**: 把你的 Go 代码里过时的写法升级成最新的、更安全的官方推荐写法, 并给出一份按重要性排好序的改造清单。

- input: 一个 Go 项目的路径, 例如 ./my-api, output: 一份按「安全 > 易读 > 可选」排好序的改造建议报告, 以及改好后的代码 (放在独立分支里, 主分支原样不动, 你确认后才合并)
- input: 一个 .go 文件, 里面是几年前的老写法 (如 interface{}、旧循环写法、已废弃的加密函数), output: 同一个文件的新写法版本: 界面不变但更简洁更安全, 并附逐条修改说明 (改了什么、为什么改)
- input: 「帮我把项目升级到最新版 Go」, output: 升级后的 go.mod + 一份风险清单: 列出哪些代码必须跟着改、哪些地方升级后会出问题, 以及对应的修改
