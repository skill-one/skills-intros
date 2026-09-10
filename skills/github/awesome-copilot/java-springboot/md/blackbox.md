# java-springboot (`github/awesome-copilot/java-springboot`)

## blackbox

**function**: 帮你写出规范、好维护的 Spring Boot (Java 后端开发框架) 应用代码, 并按业界最佳实践改进已有代码。

- input: 一句需求描述, 如: 「帮我写一个用户注册的接口, 邮箱和密码要校验」, output: 一套完整可用的 Spring Boot 代码: 注册接口 + 参数校验 + 密码加密存储 + 数据库保存
- input: 粘贴一段自己写的、比较随意的 Java 代码, output: 按最佳实践重构后的代码, 并指出改了什么、为什么改 (如: 业务逻辑集中、错误返回格式统一、不把数据库对象直接暴露给前端)
- input: 描述一个困扰, 如: 「配置文件里数据库密码是明文写的, 怎么办?」或「怎么写测试?」, output: 直接可落地的解决方案和对应代码, 如: 密码改从环境变量读取、给出单元测试 + 集成测试的写法
