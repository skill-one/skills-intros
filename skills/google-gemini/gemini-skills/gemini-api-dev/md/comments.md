# gemini-api-dev (`google-gemini/gemini-skills/gemini-api-dev`)

## comments

- user: 后端老兵, category: 妙用, comment: 多轮对话不用自己拼历史消息,拿到第一轮的 id 传给 previous_interaction_id 就行,服务端自己记上下文。我本地那套会话管理代码全删了。
- user: 第一次接大模型的新手, category: 坑, comment: 我先装了旧的 google-generativeai 包,示例全跑不通。正确的是 google-genai,包名少个词,import 也得写 from google import genai,坑了我半天。
- user: 独立开发者, category: 注意, comment: 默认会存交互记录,付费档留 55 天。做隐私敏感功能记得显式 store=False,但它会让多轮对话和后台任务失效,先想清楚再关。
- user: 维护三年老项目的迁移党, category: 注意, comment: 老代码里的 gemini-2.5 系列已经废弃,提出来会被自动换成 3.8-flash 并注明。省事了,但上线前记得自己核对一遍模型名,别盲信替换。
- user: 做 AI 客服的全栈, category: 坑, comment: system_instruction 不是会话级的,第二轮没传,机器人当场忘了人设乱答。tools 和 generation_config 同理,每一轮都要重新带上,我栽过一次。
- user: 给团队搭调研助手的开发, category: 注意, comment: deep-research 必须开 background=True,然后轮询 client.interactions.get 等状态变 completed。它跟 store=False 互斥,想跑后台就别关存储。
