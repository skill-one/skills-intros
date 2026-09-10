# azure-validate (`microsoft/azure-skills/azure-validate`)

## comments

- user: 第一次用的新手, category: 坑, comment: 一上来就喊验证被它拦下:得先跑 azure-prepare 出计划,状态到 Approved 才放行。顺序错了白跑一趟。
- user: 后端老兵, category: 妙用, comment: 以前部署总卡在角色权限不够,跑十几分钟才报错。现在它提前查清 RBAC 角色和托管标识权限,缺啥补啥,一次过。
- user: 运维老哥, category: 注意, comment: 不是一条命令跑完:每轮按提示做一个动作,带 -CompletedStep 再跑,进度记在 .azure/validate-status.json,中断能续。
- user: 接私活的全栈, category: 注意, comment: 验证全过它就停,不会自动部署,我干等半天。开头明说'验证完直接部署',它才转给 azure-deploy 执行,省一轮对话。
- user: DevOps 老哥, category: 坑, comment: 想手动改 validate-status.json 跳步,它不认:Validated 状态只能由脚本走完全程后设置。老实按步骤来,别抄近道。
- user: 云上踩过坑的独立开发者, category: 启发, comment: 以前直接 azd up 冲,失败再回头查,返工很贵。现在固定 prepare→validate→deploy,五分钟预检换一次成功,这账划算。
