# google-agents-cli-publish (`google/agents-cli/google-agents-cli-publish`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没部署就跑 publish 直接报错——必须先 deploy 生成 deployment_metadata.json，还要提前在控制台建好 Gemini Enterprise app，顺序不能反。
- user: CI 工程师, category: 妙用, comment: 各资源 ID 全走环境变量接进流水线，脚本里不写死；注册是幂等的，CI 重跑直接更新旧注册，不会越注册越多。
- user: 运维老哥, category: 注意, comment: Cloud Run 走 A2A 前先给 Discovery Engine 服务账号授 roles/run.servicesInvoker，我漏了这步，注册成功但对话里调不通。
- user: 全栈开发者, category: 坑, comment: 对话时报 Session not found，排查半天是 google-cloud-aiplatform 版本太老（≤1.128.0），升级后重新部署再注册即好。
- user: AI 应用开发者, category: 启发, comment: ADK agent 别手选 a2a，默认 adk 走原生调用；排错去 reasoning_engine_stderr 日志搜 streaming_agent_run_with_events，能看到真实报错。
- user: MCP 集成新手, category: 注意, comment: 外部 MCP server 工具列表不会自动抓，要自己导出 tools/list 存成 toolspec.json 上传，上限 10KB，且不支持 us/eu 多区域。
