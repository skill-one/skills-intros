# convex-authz (`get-convex/agent-skills/convex-authz`)

## blackbox

**function**: 检查 Convex 应用 (一种后端框架) 的权限漏洞——比如用户能冒充别人、能偷看别人的数据——并直接把代码修好。

- input: 一个含 convex/ 目录的项目路径, output: 一份权限漏洞报告: 按漏洞类型分组, 标明文件和行号, 说明"谁可以冒充谁 / 谁能读到谁的数据", 并附上每处已修复代码的前后对比 (diff)
- input: "帮我加固这个应用, 别让用户互相看到/改到别人的数据" + 项目文件夹, output: 修改好的后端代码文件: 每处漏洞都补上了身份和归属校验, 未经授权的访问会直接被拒绝; 并确认修改后代码编译检查通过
- input: 一个没有 convex/ 目录的普通项目, output: 直接告知"这不是 Convex 项目, 无法处理", 不做任何修改
