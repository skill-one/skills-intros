# firebase-ai-logic-basics (`firebase/agent-skills/firebase-ai-logic-basics`)

## comments

- user: Flutter 兼职开发者, category: 坑, comment: 只跑 flutterfire configure 就调接口，一直 PERMISSION_DENIED。它只配客户端，必须再跑 npx firebase-tools init ailogic 才真正开通 AI 服务。
- user: 第一次接 AI 的新手, category: 坑, comment: 照旧教程写了 gemini-2.0-flash，报模型不存在。老模型已下线，动手前先去官方 Models 文档抄当前模型名。
- user: 前端工程师, category: 坑, comment: 让用户传 30MB 的 PDF 直接读，报 413。超 20MB 别塞 inline 数据，先传 Cloud Storage 再把链接给模型。
- user: 后端老兵, category: 妙用, comment: 模型名我从不写死在代码里，全走 Remote Config。模型下线时改个后台配置就行，不用发版，客户端零改动。
- user: 独立开发者, category: 注意, comment: 上线前必须配 App Check，否则免费额度会被陌生人刷光。本地调试先在代码里开 debug token，再把控制台日志里的 UUID 注册进去。
- user: 想做 AI 生图的产品人, category: 注意, comment: 想用 Nano Banana 生图，免费档调不通，要先升级 Blaze 按量付费。先确认账单再写代码，免得白折腾半天。
