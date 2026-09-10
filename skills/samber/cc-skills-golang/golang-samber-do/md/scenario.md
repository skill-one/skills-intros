# golang-samber-do (`samber/cc-skills-golang/golang-samber-do`)

## scenario

Go 项目一大,main.go 里手动 new 几十个服务,依赖层层传递,加一个字段要改十几处构造函数,初始化顺序错了直接启动崩溃。我用 samber/do 帮你自动装配依赖:按需创建、统一生命周期、测试时一键换成 mock。💉
