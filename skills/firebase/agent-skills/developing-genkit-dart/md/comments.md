# developing-genkit-dart (`firebase/agent-skills/developing-genkit-dart`)

## comments

- user: 第一次写 Dart 的新手, category: 坑, comment: 普通 Dart 类当 schema，模型输出一直对不上格式。必须用 schemantic 库（@Schema()、$ 前缀类）才认，换完立刻正常。上手前先读它的文档。
- user: Flutter 独立开发者, category: 妙用, comment: genkit start -- dart run main.dart 别当成可选包装：本地 UI 能看每次 flow 的完整调用链和真实 prompt，调 agent 比 print 日志快太多。
- user: 后端老兵, category: 注意, comment: Gemini、Claude、OpenAI 是三个独立插件，初始化写法各不相同。我拿 OpenAI 经验猜 Anthropic，卡了半小时。用哪个就翻哪个的参考文档，别想当然。
- user: 做 agent 应用的全栈, category: 妙用, comment: 一直不敢让 agent 直接动文件，后来用 filesystem 插件配 toolApproval 中间件，工具执行前先拦下来给人确认，这才敢放进生产流程。
- user: 运维老哥, category: 坑, comment: 装之前先跑 genkit --version 确认。我机器上 curl 和 npm 各装了一份，新旧版本打架，报错排查半天才发现原因。
- user: 前端转写 Dart 的, category: 启发, comment: 以前 AI 逻辑全散在界面代码里，现在用 defineFlow 把每段拆成独立可跑、可追踪的单元。设计功能先想怎么拆 flow，定位问题也快了。
