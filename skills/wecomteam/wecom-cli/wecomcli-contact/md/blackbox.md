# wecomcli-contact (`wecomteam/wecom-cli/wecomcli-contact`)

## blackbox

**function**: 报一个人名（中文、拼音、英文名或花名都行），我从公司通讯录里帮你找出这个人：他是谁、在哪个部门、什么职务，并给出系统唯一标识 userid。

- input: 「帮我查一下张伟的 userid」, output: 张伟的用户信息：userid、所在部门（如「技术部 / 后端组」）、职务，直接可复制使用
- input: 「zhangsan 是谁？」（只记得拼音或英文名）, output: 拼音/英文名对应的员工：中文姓名 + 部门 + 职务
- input: 「公司有几个李娜？都是谁」, output: 所有叫李娜的人的完整名单，每人附英文名/部门/职务，方便区分同名
