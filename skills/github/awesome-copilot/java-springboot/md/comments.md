# java-springboot (`github/awesome-copilot/java-springboot`)

## comments

- user: 第一次写 Spring Boot 的实习生, category: 坑, comment: 直接说"写个登录接口", 它按规范给了一整套 DTO+校验+异常处理, 文件好几个, 新手看懵. 先声明"只要最小可运行版", 它就只给必要文件了.
- user: 十年后端老兵, category: 妙用, comment: 我把现有 Controller 贴给它, 让它按自己的规范逐条挑毛病, 它能点出字段注入、实体直出、缺事务这些具体问题, 比自己翻 review 清单快.
- user: 带三个新人的 Tech Lead, category: 启发, comment: 我把它的分层和项目结构建议整理成团队 code review 清单, 新人提 PR 前先自查, 我的 review 意见少了一大半.
- user: 运维老哥, category: 注意, comment: 让它写配置时必须说明环境和哪些值走环境变量, 否则示例里会出现明文密码样例, 直接抄进仓库就泄密了.
- user: 从 Python 转岗的后端, category: 注意, comment: 转岗第一周没提项目用 Lombok, 它给的标准写法贴进现有代码风格全对不上, 手工改了半天. 先交代版本和既有约定能省事.
- user: 独立开发者, category: 妙用, comment: 让它按层给测试: 控制器用 @WebMvcTest, 仓储用 @DataJpaTest. 我以前全用 @SpringBootTest 整包启动, 现在单测秒级跑完.
