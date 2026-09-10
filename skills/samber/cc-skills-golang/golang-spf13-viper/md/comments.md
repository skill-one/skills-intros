# golang-spf13-viper (`samber/cc-skills-golang/golang-spf13-viper`)

## comments

- user: 第一次用的新手, category: 坑, comment: 嵌套配置 database.host 死活读不到环境变量，排查半天：只开 AutomaticEnv 没用，必须再配 SetEnvKeyReplacer 把点换成下划线，三个设置一个都不能少。
- user: 后端老兵, category: 妙用, comment: 一个二进制打天下：本地读 config.yaml，测试环境吃环境变量，线上用 flag 覆盖端口。靠 flag>env>文件>默认 的固定优先级，换环境不改一行代码。
- user: 运维老哥, category: 坑, comment: vim 改完配置热更新不触发，还以为是代码 bug。其实是 vim 原子替换换了 inode，监听跟丢了。验证热更新要用 echo >> config.yaml，别用编辑器保存。
- user: 写单测的后端, category: 坑, comment: 单测共用全局 viper，上个 case Set 的值污染下个，测试顺序一换就随机挂。改成每个测试 viper.New() 建独立实例，彻底根治。
- user: 从 Python 转 Go 的, category: 注意, comment: 结构体字段 max_conn 不写 mapstructure 标签，Unmarshal 后永远是零值还不报错。别信隐式映射，每个字段都显式打上标签。
- user: 云原生开发者, category: 注意, comment: 容器里经常没有配置文件，ReadInConfig 报错别直接 return。用 errors.As 认出 ConfigFileNotFoundError 放行，服务光靠环境变量就能起。
