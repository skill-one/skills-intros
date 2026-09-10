# caveman-setup (`juliusbrussee/caveman/caveman-setup`)

## blackbox

**function**: 把你的项目里所有调用 AI 的代码改接到一个计量网关, 让每一次 AI 调用的花费都被记录下来——模型的回答内容完全不变。

- input: 一个调用了 OpenAI / Anthropic 的代码仓库 + 4 项接入信息 (网关地址、API 密钥、密钥存放模式、控制台地址), output: 改接好的代码 (每个 AI 调用点都指向网关) + 一份验证报告, 报告里是一次真实请求的实测数字, 如: HTTP 200 · 模型 gpt-4o-mini · 8 输入 / 5 输出 token
- input: 一个用 LangChain、LiteLLM 或 Vercel AI SDK 等框架调 AI 的仓库, output: 一份改动清单, 每个调用点一行说明改了什么 (只改连接地址和加一个认证头, 不动业务逻辑), 外加一个控制台链接, 打开就能看到这次请求花了多少钱
- input: 一个没有任何 AI 调用的仓库, output: 一句如实的报告: 没找到可接入的 AI 调用点, 未做任何改动, 并提示改用别的接入方式
