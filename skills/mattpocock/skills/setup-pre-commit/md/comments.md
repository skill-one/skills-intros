# setup-pre-commit (`mattpocock/skills/setup-pre-commit`)

## comments

- user: 第一次用的新手, category: 坑, comment: 以为钩子只查我改的文件, 结果全量 typecheck 把仓库里的老错误全翻出来, 每次提交都被挡. 先修历史失败, 再上钩子。
- user: 后端老兵, category: 妙用, comment: 最后一次提交我故意夹了个格式稀烂的文件, prettier 当场把它改好——30 秒验证整套钩子真的在干活, 不用自己造测试场景。
- user: 前端组长, category: 注意, comment: 同事拉完代码必须跑一次 npm install, prepare 脚本才会装上钩子; 只 pull 不装依赖的人手里没有这道闸, 提前群里说一句。
- user: GUI 提交重度用户, category: 坑, comment: 我常用 GUI 一键提交, 有回勾了「跳过钩子」, 之后一直纳闷 prettier 为啥没生效. --no-verify 会整个绕过, 别让它变成习惯。
- user: 刚接手老仓库的前端, category: 注意, comment: 没配过 prettier 时默认双引号+分号, 第一次会重排一堆老文件. 先单独提一个纯格式化 commit, 别和业务改动混在一起难 review。
- user: 单干全栈, category: 启发, comment: 用明白才懂: 钩子跑在自己电脑上, 谁都能绕过, 它只负责 30 秒拦住「忘了格式化」这类小事; 真把关的还是 CI。心态对了反而省心。
