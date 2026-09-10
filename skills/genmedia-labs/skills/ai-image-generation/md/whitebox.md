# ai-image-generation (`genmedia-labs/skills/ai-image-generation`)

## whitebox

- 触发: 用户请求生成或改图, 命中关键词 (generate image / text to image / image to image / i2i 等)
- 意图路由: 先分 t2i 还是 i2i, 再按意图选模型 — 图内文字→GPT Image 2, 写真/产品→Seedream 5, 极速迭代→Klein 4B 或 Nano Banana 2, 意图不明→缺省 FLUX 2 Klein 9B (i2i 缺省 Nano Banana 2 Edit)
- 构造输入: 按所选模型的 prompting 模式写 prompt (主体先行、图中文字用 "…" 原样引用), 并填 schema 字段, 枚举值严格取自文档 (如 GPT Image 2 仅 3 种 size)
- 执行: 鉴权就绪后经 Bash 调 `runcomfy run <vendor>/<model>/<endpoint> --input '{JSON}' --output-dir ./out`
- 交付: 从输出目录取回图片文件

- 模型路由表: 内置 intent→endpoint 映射 (vendor/model/endpoint 字符串), 每条标注 pick-for / avoid-for 权衡, 支持多参考图等条件 (Klein t2i ≤4 张, NB2 edit 1–20 张, GPT Image 2 edit ≤10 张)
- Prompt/参数模式绑定: 每个模型各有规则并在构造时套用 — GPT Image 2 必须原样引用图内文字并指明文字系统 (kana/Cyrillic/Arabic); Klein 用主体先行描述、steps 4–8 打稿 ~25 精修; Nano Banana 2 用 num_images/seed/aspect_ratio/resolution/enable_web_search 控制成本与真伪
- 外部依赖: 全部执行经 `runcomfy` CLI (npm 包 @runcomfy/cli, Bash 权限仅限 `runcomfy *` 命令); 无本地权重, --input JSON 按各模型页 schema 原样传给 RunComfy 远端模型 API, 鉴权靠 `runcomfy login` 或 RUNCOMFY_TOKEN 环境变量
