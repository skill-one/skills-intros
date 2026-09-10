# wecomcli-meeting (`wecomteam/wecom-cli/wecomcli-meeting`)

## whitebox

- 解析用户意图，映射为操作类型：create / list / search / get / cancel / update / original get
- 用 Read 读取该操作的参考文档（references/meeting-*.md），严格按文档工作流执行，禁止凭记忆直接发命令
- 参数补全：姓名经 wecomcli-contact 技能解析为 userid；创建/更新前借 wecomcli-calendar 技能查参会人忙闲、订会议室（拿 meeting_room_id）
- 执行 wecom-cli meeting <action> --json '{...}'，从返回提取 meeting_id 等字段驱动后续编排（get 详情 / original get 转写原文）
- 按输出规范渲染：只展示主题、时间、参会人姓名，屏蔽 userid、会议号与入会链接

- 依赖与调用：唯一外部二进制是 wecom-cli（bin 依赖），统一走 wecom-cli meeting <action> --json；跨技能依赖 wecomcli-contact（姓名→userid）、wecomcli-calendar（忙闲 free list、会议室 rooms search）；核心协议是 read-before-execute——每次操作必先读参考文档，参数格式与边界行为以文档为准
- 标识符解析与校验：姓名必须经 contact 技能搜索验证后转 userid（wo 前缀），禁止拼接/编造；attendees 强制对象数组格式 [{"userid":"woxxx"}]；meeting_id 用 mt 前缀长字符串，9 位会议号（meeting_code）仅供入会、不能当 id；错误按类型分流——权限/参数错误不重试、网络超时可重试，重试上限 2 次
- 消歧与接口编排：创建场景遇到模糊表述（"开会/xx会"）必须文字追问固定问题"需要创建日程还是会议？"，查询场景反向禁止追问、改为日程+会议双查后按是否含入会链接分类合并去重；"总结会议"是两接口编排——meeting get 取平台 AI 生成的 notes（纪要/待办），带自定义要求时跳过纪要、直接 meeting original get 拉转写原文重新加工
