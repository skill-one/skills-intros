# documentation-and-adrs (`addyosmani/agent-skills/documentation-and-adrs`)

## blackbox

**function**: 把"当初为什么这么做"写成文档:技术决策记录、项目 README、代码里的关键注释、更新日志——让三个月后的你和接手的人不用重新猜。

- input: 一句决策描述,如「我们决定弃用 MongoDB,改用 PostgreSQL」, output: 一份 Markdown 决策记录文件 (ADR):写清背景、当时考虑过的备选方案及各自的优缺点、最终选择的理由和影响
- input: 一个项目文件夹的路径, output: 一份 README.md:新人拿到就能照着跑起来——安装步骤、常用命令表、项目架构简介
- input: 一段含义不明、注释混乱的代码文件, output: 修改后的代码:补上解释「为什么这么写」的注释,删掉复述代码的废话注释和被注释掉的死代码
