# nestjs-best-practices (`kadajett/agent-nestjs-skills/nestjs-best-practices`)

## comments

- user: 后端组 Tech Lead, category: 妙用, comment: 我把它当 review 清单用: 让 AI 按优先级表从 arch-/di- 往下过同事的 PR, 循环依赖、属性注入这类人工容易漏的点常被抓出来。
- user: NestJS 新手 (第一个项目), category: 坑, comment: 两个 service 互相 import 启动就报循环依赖, 改半天。照 arch-avoid-circular-deps 拆出公共模块才好, 新手别裸写, 先看架构几条。
- user: 运维老哥, category: 注意, comment: devops 类优先级虽标得低, 但优雅停机和健康检查是滚动发布刚需, 上线前 config/logging/graceful-shutdown 三条别跳过。
- user: 接手祖传代码的后端, category: 妙用, comment: 接手三年没人动的项目, 我没让它直接改, 先按各规则的「错误示例」对照代码列问题清单, 再按 arch→perf 顺序重构, 没改崩。
- user: 转行半年的 Java 后端, category: 注意, comment: Quick Reference 每条就一句话, 真值钱的是 rules/ 文件里错误与正确代码的对照。点名让 AI 展开某条规则再用, 别只看表动手。
- user: 兼职带新人的组长, category: 启发, comment: 以前带新人靠口头念「service 别写太大」, 现在直接发 single-responsibility 的正误代码对比当教材, review 来回少一半。
