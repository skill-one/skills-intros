# ai-image-generation (`prime-skills/runcomfy-agent-skills/ai-image-generation`)

## whitebox

- 触发词命中 ("generate image" / "text to image" / "i2i" 等), 拿到用户的生图或改图需求
- 按 t2i (文生图) vs i2i (图改图) 分类意图, 在 11+ 模型目录里按文档化特征选型 (排版文字→GPT Image 2, 照片写实→Seedream 5, 极速迭代→Klein 4B 等)
- 按该模型的提示词模式写 prompt (主体先行、图内文字加引号、非拉丁文字指明文种), 并映射到该模型的字段 schema
- 通过 Bash 执行 `runcomfy run <vendor>/<model>/<endpoint> --input '{JSON}' --output-dir ./out`
- 生成结果落盘 output-dir, 交付给用户

- 意图路由: 先定 t2i 还是 i2i 端点, 再按各模型 "Pick for / Avoid for" 的文档化特征选型; 无明确倾向时用默认值 — t2i = FLUX 2 Klein 9B, i2i = Nano Banana 2 Edit
- Schema 校验/映射: 各模型字段表硬性约束参数 — 如 GPT Image 2 只接受 1024_1024 / 1024_1536 / 1536_1024 三种 size, Klein steps 限 4–25 且超过收益递减, Nano Banana 2 走 aspect_ratio/resolution 枚举; prompt 与参数序列化成 JSON 填进 --input
- 外部依赖: 全部经 RunComfy CLI 调用远端模型 API (npm i -g @runcomfy/cli 或 npx 零安装, runcomfy login / RUNCOMFY_TOKEN 认证); 唯一工具面是 Bash(runcomfy *), 需要遮罩 inpainting / outpainting 等超出本技能范围的操作时转交 image-edit skill
