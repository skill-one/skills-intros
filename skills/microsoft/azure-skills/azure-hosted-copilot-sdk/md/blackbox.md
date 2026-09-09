# azure-hosted-copilot-sdk (`microsoft/azure-skills/azure-hosted-copilot-sdk`)

## blackbox

**function**: 一句话:你给我一个用 GitHub Copilot SDK 做的应用 (或一句想做一个的想法),我帮你把它搭出来、加功能、换成你自己的模型,并准备/部署到 Azure (微软云) 上跑起来 ☁️

- input: 一句话需求:「帮我搭一个 Copilot 智能问答应用」, output: 一个完整可运行的新项目:网页界面 + 后端接口,本地就能跑起来,且天生为上 Azure 做好了准备
- input: 一个已在用 Copilot SDK 的现有项目文件夹, output: 同一个项目,补齐了上云所需的一切配置,发布到 Azure 后拿到一个可以访问的网址
- input: 现有项目 + 一句改动要求,如「把模型换成我自己的 Azure 模型」或「加个对话历史功能」, output: 改好的代码:应用按你的要求接上新模型/新功能,原有部分不被破坏
