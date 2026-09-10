# golang-continuous-integration (`samber/cc-skills-golang/golang-continuous-integration`)

## comments

- user: 第一次配 CI 的新手, category: 坑, comment: 照抄文档里的 action 版本号, 几天后收到 deprecation 警告才知道示例只是参考版本. 我逐个去 action 仓库核对最新 major 再替换才干净.
- user: 后端老兵, category: 妙用, comment: 我们用不上 Docker Hub, 删掉登录步骤和 docker.io 那行只留 GHCR, GITHUB_TOKEN 就能推镜像, 一个 secret 不用配. PR 上只构建不推送, 验证 Dockerfile 很安心.
- user: 开源库维护者, category: 妙用, comment: go.mod 声明 1.24, 照那张 go 版本对照表抄 matrix, 一行没改. 另外库项目发布不用完整 goreleaser, 极简配置就够, 我后来发现 gh release create 都够了.
- user: 运维老哥, category: 注意, comment: auto-merge 工作流的 actor 校验防不住伪造, 真正兜底是分支保护规则: 必需状态检查 + 必需审批. 我配好这两样才敢开自动合并.
- user: 接手祖传仓库的工程师, category: 坑, comment: 我上来就让它加 lint job, 结果仓库早就有 lint.yml, 塞出两份重复配置. 后来学乖了: 先让它读现有 workflow 再提需求, 它会查重补缺.
- user: 五人小团队 Tech Lead, category: 注意, comment: AI review 每个 PR 并行跑 4 个 job, 月底用量肉眼可见地涨. 我把触发收窄到 main 的 PR, 再砍掉用不上的 job, 成本立刻可控.
