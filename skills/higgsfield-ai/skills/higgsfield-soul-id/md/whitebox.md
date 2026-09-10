# higgsfield-soul-id (`higgsfield-ai/skills/higgsfield-soul-id`)

## whitebox

- Bootstrap: 检查 higgsfield CLI 是否安装、登录态是否有效、账户是否为付费计划 (Basic+)
- 收集最小输入: 一个名字 + 5~20 张多角度、多光照的人脸照片 (本地路径或已上传的 upload id 均可)
- 按用户下游用途选变体: --soul-2 (默认, 生图) 或 --soul-cinematic (影视/视频)
- 执行 higgsfield soul-id create 提交训练, CLI 自动上传照片, 捕获返回的 reference_id
- 静默轮询 higgsfield soul-id wait (默认 30 分钟超时), 完成后交付: 'Soul 就绪, 用 --soul-id <id> 调用'

- 全部通过 Bash 调用 higgsfield CLI 完成, 不直接调 API; 本地照片路径由 CLI 自动上传 (--image 同时接受路径和 upload id)
- 身份模型在 Higgsfield 服务端训练: 照片 → 人脸一致性模型 (Soul Character), 产出可复用的 reference_id, 供 higgsfield-generate 以 --soul-id 引用, 搭配 text2image_soul_v2 / soul_cinematic 等模型
- 三层校验: 训练前检查认证 (Session expired → 要求 auth login) 和付费计划 (免费计划拦截); 训练中静默等待避免刷屏; 训练失败按错误码归因 (照片不足 5 张/光照差等)
