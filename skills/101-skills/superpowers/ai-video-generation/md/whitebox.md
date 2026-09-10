# ai-video-generation (`101-skills/superpowers/ai-video-generation`)

## whitebox

- 触发词命中 (如 '生成视频' / veo / image to video), skill 被调用
- 按任务类型 (文生视频/图生视频/口型/剪辑等) 从模型表选定 app id
- 组装 JSON 参数, 通过 Bash 执行 belt app run <app-id> --input '{...}'
- CLI 流式返回进度, 等任务完成拿到视频输出链接
- 按需链式追加后处理: 超分 (Topaz) / 拟音 (Foley) / 拼接 (Media Merger)

- 唯一执行通道: Bash 工具且被限定为 belt * 命令; 外部依赖是 inference.sh CLI (belt), 需先 belt login 认证
- 模型路由: 内置 任务类型→app id 映射表 (文生视频→google/veo-3-1-fast, 让图动起来→falai/wan-2-5, 数字人→bytedance/omnihuman-1-5 等), 40+ 模型均为 inference.sh 托管的远程 API
- 输入契约: 所有参数序列化为单个 JSON 经 --input 传入, 常见字段 prompt / image_url / audio_url / duration / resolution / generate_audio; 未列出的模型可用 belt app list --category video 发现
