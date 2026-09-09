# gpt-image-edit (`prime-skills/runcomfy-agent-skills/gpt-image-edit`)

## whitebox

- 组装 JSON body: 按输入 schema 填 prompt (必填) + images (必填, ≤10 个公网 HTTPS URL, 首张为主参考) + size (可选, 默认 auto 保持原图比例)
- 按内置提示词模式改写 prompt: 先写保留目标 ("Keep face/brand unchanged"), 再写改动; 图内文字逐字引用并注明语种/方向; 多参考图用 "image 1/2/3" 编号指代
- 执行本地 CLI 命令: runcomfy run openai/gpt-image-2/edit --input '<JSON>' --output-dir <绝对路径>
- CLI 向 https://model-api.runcomfy.net/v1/models/openai/gpt-image-2/edit 发起 POST, 轮询该请求直到编辑完成
- 把结果下载到 output-dir (仅放行 *.runcomfy.net / *.runcomfy.com 域名); Ctrl-C 会在退出前取消远端任务

- 提示词层是本 skill 的核心增量: 内置该模型已验证的提示模式 (保留优先、逐字引用图内文字、编号参考图、方位语言如 "top-right to bottom-center"), 并规避反模式 (复合长指令按需拆成多轮 pass) —— 同一个底层模型, 产出比裸提示更稳定
- Schema 校验前置: images 上限 10, size 仅接受 auto / 1024_1024 / 1024_1536 / 1536_1024, 越界直接 422; prompt 作为 JSON 字符串经 --input 传入, CLI 不做 shell 展开, 直接 HTTPS 传输, 无 shell 注入面
- 外部依赖链: RunComfy CLI (@runcomfy/cli, npm 全局装; runcomfy login 设备码登录, CI 用 RUNCOMFY_TOKEN 环境变量) → RunComfy Model API → OpenAI GPT Image 2 /edit 端点 (ChatGPT Images 2.0 图生图); 安全侧: 单文件下载上限 2 GiB, 退出码区分可重试 (75: 超时/429) 与鉴权失败 (77)
