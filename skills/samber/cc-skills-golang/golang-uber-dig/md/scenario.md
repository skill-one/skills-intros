# golang-uber-dig (`samber/cc-skills-golang/golang-uber-dig`)

## scenario

Go 项目一大,main() 里手动 new 几十个依赖,改一处牵全身,测试还要手写全套假对象?我用 dig (依赖注入:依赖自动装配到位) 声明式接线——砍掉胶水代码,缺依赖启动即报错。⛏
