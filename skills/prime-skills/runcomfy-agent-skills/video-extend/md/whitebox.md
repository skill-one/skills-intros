# video-extend (`prime-skills/runcomfy-agent-skills/video-extend`)

## whitebox

- 按质量/成本意图选端点: 全量 google-deepmind/veo-3-1/extend-video (默认) 或 fast/extend-video (草稿档)
- 把源视频 URL + 只描述"下一幕"的 prompt 打包成 JSON, 经 runcomfy run ... --input 提交
- CLI 把 JSON POST 到 RunComfy Model API, 由 Google Veo 3-1 生成续接片段
- CLI 轮询请求状态, 成功后把成片下载到 --output-dir; Ctrl-C 会在退出前取消远端任务

- 路由: 两个端点同为 Google Veo 3-1, 仅质量/延迟/单次成本不同 — 最终交付走全量 extend, 多轮草稿走 fast extend
- 输入契约: video_url/prompt 以单条 JSON 字符串传入, CLI 不做 shell 展开 (无 shell 注入面); JSON/schema 不符返回 exit 65, 其余错误各有专用码 (64/69/75/77). 外部依赖: @runcomfy/cli、model-api.runcomfy.net、Google Veo 3-1 模型
- 续接一致性: 身份/光照/构图/物理由源视频提供, prompt 只写下一拍并显式锚定镜头 (如 "camera continues pushing in"); 长叙事把上段输出作为下段 video_url 链式续接, 每代生成累积身份漂移, 故单段限 3-5s, 长链条需 i2v 重新锚定. 下载单文件 > 2 GiB 中止
