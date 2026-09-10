# golang-google-wire (`samber/cc-skills-golang/golang-google-wire`)

## scenario

Go 项目手动初始化依赖链 (数据库→缓存→业务层), 构造函数一改就处处要补, 漏了往往到运行时才炸。我用 google/wire 在编译期生成装配代码: 缺啥依赖, 跑一下 wire 立刻报错, 构建前就修完。🪡
