# firebase-ai-logic-basics (`firebase/agent-skills/firebase-ai-logic-basics`)

## blackbox

**function**: 帮你把 Gemini AI 能力 (聊天、看图、语音、生成内容) 直接装进你的网页或手机 App, 交付能跑的代码和配置。

- input: 「我在做一个 Web 聊天页面, 想接入 Gemini, 回复要像打字一样逐字出现」, output: 可直接运行的前端代码: 项目初始化 + 多轮聊天 + 流式 (打字机) 回复效果, 附接线步骤
- input: 「我的 App 想让用户拍张照, AI 自动识别里面是什么并生成描述」, output: 对应平台 (iOS/Android/Flutter/Web) 的图片识别代码: 传入照片 → 返回 AI 生成的文字描述, 含大文件的处理方案
- input: 「我要 AI 每次都按固定格式返回, 比如必须是 {名称, 价格, 标签} 这样的 JSON」, output: 带结构化输出约束的调用代码, 保证返回结果严格符合你定义的字段格式, 可直接存库使用
- input: 「准备上线了, 怎么防止别人盗用我的 AI 额度? 顺带本地测试也别报错」, output: 一份安全配置清单和对应代码: 上线防护 (App Check) + 本地/自动化测试的调试令牌配置, 直接照做即可
