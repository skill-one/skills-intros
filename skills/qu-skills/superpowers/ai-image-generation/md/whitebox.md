# ai-image-generation (`qu-skills/superpowers/ai-image-generation`)

## whitebox

- 匹配意图: 由触发词 (flux / text to image / ai art 等) 确认是图像生成或编辑任务, 前提是已装 belt CLI 并 belt login。
- 选模型: 按 50+ 模型目录的"最佳用途"表选 app ID — 文生图用 FLUX/GPT-Image-2, 文字渲染用 Reve/Seedream 3.0, 放大用 Topaz。
- 组装命令: 把需求转成一条 `belt app run <app-id> --input '<JSON>'` 命令, JSON 字段含 prompt、quality、aspect_ratio、images 等。
- Bash 执行: 允许的工具仅 `Bash(belt *)`, 通过 shell 运行命令, inference.sh 平台调用对应模型 API 生成图像。
- 交付结果: 返回生成图像; 若是编辑/拼接任务, 把图像 URL 填入下一次调用的 JSON 里串联。

- 统一调用协议: 没有自有代码逻辑, 一切操作收敛为 `belt app run <app-id> --input '<JSON>'` (inference.sh CLI), 解析、鉴权、执行全靠 belt。
- 能力路由: 按任务映射到具体模型 API — openai/gpt-image-2 (编辑/局部重绘), falai/flux-dev-lora (高质量), falai/reve 与 bytedance/seedream-3-0-t2i (文字渲染), falai/topaz-image-upscaler (放大), falai/flux-2-klein-lora (快速廉价); 底层由 OpenAI / Google / xAI / ByteDance / fal.ai / pruna 托管。
- 图像复用实现编辑: 通过 JSON 的 `images` 字段传入现有图像 URL, 实现图生图、换背景、局部重绘; 多图拼接也复用同一命令模式 (infsh/stitch-images)。
