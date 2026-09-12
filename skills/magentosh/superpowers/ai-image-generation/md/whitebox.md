# ai-image-generation (`magentosh/superpowers/ai-image-generation`)

## whitebox

- 用户请求命中触发词 (如 generate image / flux / ai art), 技能被激活
- 根据任务类型 (文生图/改图/放大/文字渲染) 从 50+ 模型表中选定对应的 app ID
- 通过 Bash 执行 `belt app run <app-id> --input '{JSON}'`, 把 prompt 及参数发给 inference.sh
- 托管的模型 API (FLUX / GPT-Image-2 / Gemini 等) 生成图片并返回
- 把生成的图片交付给用户

- 模型路由: 按 '最佳用途' 映射选型 — 文字渲染选 Reve/Seedream 3.0, 4K 高清选 Seedream 4.5/ImagineArt, 极速低价选 FLUX Klein 4B, 放大选 Topaz Upscaler
- 统一调用协议: 所有模型共用一条命令 `belt app run <app-id> --input '<JSON>'`, 差异只在 app ID 和 JSON 字段 (prompt / images / aspect_ratio / quality)
- 外部依赖: 前置 inference.sh CLI (`belt`, 需 `belt login` 认证), 后端为各厂托管 API — fal.ai、OpenAI、Google、xAI、ByteDance、Pruna
