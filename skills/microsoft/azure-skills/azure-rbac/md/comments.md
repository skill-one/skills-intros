# azure-rbac (`microsoft/azure-skills/azure-rbac`)

## comments

- user: 云运维老哥, category: 妙用, comment: 让函数应用的托管标识读 blob, 我只说了"读", 它给的是 Storage Blob Data Reader 而不是 Contributor, 连 scope 都按最小范围收, 不用我再手动收权。
- user: 后端老兵, category: 注意, comment: 帮同事授权, 我第一次直接拿 Owner 账号上去做。其实授权只需要带 roleAssignments/write 的角色(如 User Access Administrator), 别随手动用 Owner。
- user: 第一次用的新手, category: 坑, comment: 我一开始只说"给应用加权限", 它没法定位角色; 后来把资源类型、操作(只读)、范围(哪个存储账号)说全, 一次就出对的角色加能直接跑的 CLI 命令。
- user: 平台工程 DevOps, category: 妙用, comment: 我要的是"用 Bicep 写 role assignment", 它除了给片段还按最佳实践核了一遍, roleDefinitionId、principalId 占位符都齐, 贴进模板直接过 pipeline。
- user: 安全合规负责人, category: 注意, comment: 内置角色对不上需求时它会建议建自定义角色。但自定义角色要自己长期维护, 内置角色的更新你享不到; 先确认真没内置的能覆盖, 再考虑自定义。
- user: 刚接手 Azure 的运维, category: 启发, comment: 以前授权都照抄门户里别人挂的 Contributor, 现在习惯从"到底需要哪几个操作"倒推最小角色, 最小权限从口号变成了我查权限问题的默认思路。
