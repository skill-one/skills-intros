# flux-2-klein (`prime-skills/runcomfy-agent-skills/flux-2-klein`)

## whitebox

- 解析触发词 (如 "flux 2 klein" / "BFL flux 2") 并选变体: 4B 用于亚秒级概念迭代, 9B 用于精修终稿; 用户只泛称 "Flux 2" 时先反问 Klein (快) 还是 Pro (高画质)
- 前置检查: RunComfy CLI 已安装 (npm i -g @runcomfy/cli), 认证来自 runcomfy login 的 token 文件或 RUNCOMFY_TOKEN 环境变量
- 按输入 schema 组装 JSON: prompt 用 "主体+动作+场景+风格+光照+相机+质量" 的声明式语序且 ≤~512 token, steps 按阶段取 4–8 (概念) 或 ~25 (精修), width/height ≤~2K 且比例 ≤16:9, 参考图 ≤4 张
- 执行 runcomfy run blackforestlabs/flux-2-klein/<variant>/text-to-image --input '<json>' --output-dir <path>; CLI POST 到 model-api.runcomfy.net 拿 request_id, 每 2s 轮询 status 到终态, 再 GET result
- CLI 把 result 中 *.runcomfy.net / *.runcomfy.com 的图片下载到 --output-dir, 结果 JSON 打到 stdout (异步场景用 --no-wait --output json 先拿 request_id)

- Prompt 转换与预校验层: 用户意图被改写为模型训练同构的 subject-first 声明式 prompt; 对 ~512 token 上限、~2K 分辨率、16:9 比例、4 张参考图上限做 pre-flight 校验 (step-distilled 架构决定 4–8 步即够概念图, >25 步收益递减), 越界参数如 width:4096 会被上游 422 (CLI 退出码 65), 故先裁剪再提交
- 外部依赖链: RunComfy CLI (@runcomfy/cli, npm 全局) + RunComfy Model API 的异步 REST 端点 blackforestlabs/flux-2-klein/9b|4b/text-to-image (Bearer token 认证, request_id + 2s 轮询); prompt 以 JSON 体直传 HTTPS, 不经 shell 展开, 无注入面
- 参考图编辑机制: 同一 text-to-image 端点直接吃最多 4 张参考图实现风格迁移和 "保持 X、只改 Y" 式条件编辑; 要求全部 ref 保持同一视觉风格, 混搭水彩+照片+3D 会互相干扰
