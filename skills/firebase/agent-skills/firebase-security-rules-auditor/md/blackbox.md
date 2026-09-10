# firebase-security-rules-auditor (`firebase/agent-skills/firebase-security-rules-auditor`)

## blackbox

**function**: 给你的 Firebase 安全规则 (控制谁能读写数据库/云存储的「门卫规则」代码) 做安全体检: 打分、找漏洞、给出修复建议。🛡️

- input: 一份 firestore.rules 规则文件的代码内容 (粘贴或给文件路径), output: 一份体检报告: 1~5 分总分 + 问题清单 (如「普通用户可以把自己改成管理员」「创建时校验了字段, 修改时却没校验」), 每条附具体修复写法
- input: 一段图省事写的规则, 如「登录了就能读写所有数据」, output: 1 分 (Critical) 红灯报告: 明确指出任何陌生人登录后都能偷看、篡改、删光你的全部数据, 并给出封堵后的规则示例
- input: 一份 storage.rules (文件存储规则) 的代码, output: 报告列出风险点: 如没限制上传文件大小 (可被恶意塞爆存储费钱)、用户照片公开可读等, 每条附修复建议
