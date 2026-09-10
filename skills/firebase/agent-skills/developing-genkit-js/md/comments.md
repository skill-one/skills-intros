# developing-genkit-js (`firebase/agent-skills/developing-genkit-js`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没先跑 genkit --version, 全局装的是老版 CLI, 照文档一步步写还是各种报错。先 npm i -g genkit-cli@^1.29.0 就顺了。
- user: 老项目迁移党, category: 注意, comment: 网上教程多是 1.0 前的写法 (configureGenkit、response.text() 之类), 照抄全报错。把报错原文贴给它, 它会先对照文档改成新 API。
- user: 后端老兵, category: 妙用, comment: 让它 genkit docs:search 查流式输出和 tool 用法, 回的全是官方最新说法, 不用再翻过时的博客和 Stack Overflow。
- user: 独立开发者, category: 妙用, comment: 本地调试挂 Ollama 插件零成本跑通, 上线前换成 Google AI, 代码基本不动。换模型供应商只改一处, 真省。
- user: Next.js 全栈打工人, category: 注意, comment: 开工先说清自己用的框架 (Next.js/Firebase/Express), 它会从 package.json 判断后用对应写法, 别让它瞎猜。
- user: AI 编程老用户, category: 启发, comment: 它主动承认内置知识过时、回答前先查官方文档, 比很多自信写出废弃 API 的助手靠谱, 这个自查习惯我抄走了。
