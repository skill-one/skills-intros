# expo-cicd-workflows (`expo/skills/expo-cicd-workflows`)

## comments

- user: 第一次给 App 配自动化的新手, category: 坑, comment: 工作流文件我随手放项目根目录, 推上去死活不触发. 必须放 .eas/workflows/ 目录下, 位置是硬性要求.
- user: 从 GitHub Actions 迁来的前端, category: 注意, comment: 我凭 GitHub Actions 的记忆直接写 YAML, 表达式上下文和触发器写法对不上. 让它先拉 schema 再生成, 一次过.
- user: Expo 独立开发者, category: 坑, comment: 首次跑校验脚本报找不到模块, 是 scripts 目录没装依赖. 先 npm install --prefix 再 validate, 别愣着查半天.
- user: 五人小团队技术负责人, category: 妙用, comment: EAS 新增了 job 类型我不认识, 它不背旧答案, 每次现场抓最新 schema 来写, 生成完还自动校验, 我不用盯文档更新.
- user: DevOps 老哥, category: 注意, comment: 校验前要联网拉 api.expo.dev 的 schema, 我们 CI 容器默认断网, 提前开白名单, 否则校验必挂.
- user: React Native 老兵, category: 妙用, comment: 我手滑把 needs 写成不存在的 job 名, 校验当场报出来. 不用等推上去在 EAS 控制台看红叉, 省一整轮.
