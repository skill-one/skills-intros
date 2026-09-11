# extension-user-approval (`caffeinelabs/skills/extension-user-approval`)

## blackbox

**function**: 给你的应用加上「申请—审批」式用户管理：新用户先提交使用申请，管理员批准后才能使用核心功能。

- input: 你的应用代码（如 src/backend/main.mo）+ 一句要求：「只有批准过的用户才能用」, output: 改好的应用：新用户打开只看到「申请使用」按钮，提交后处于待审状态，批准前无法使用任何主要功能
- input: 以管理员身份打开你的应用, output: 一个管理面板：列出所有用户及状态（待审 / 已批准 / 已拒绝），一键批准或拒绝，还能给用户分配角色
- input: 普通用户打开你的应用, output: 清晰的界面提示：显示自己的审批状态，可一键提交申请；被拒后明确告知无权使用，被批准后正常进入应用
