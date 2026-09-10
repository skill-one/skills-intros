# baoyu-comic (`jimliu/baoyu-skills/baoyu-comic`)

## whitebox

- 加载偏好配置 EXTEND.md (项目级或用户级); 找不到则先阻塞式完成首次设置, 否则不往下走
- 分析输入内容, 与用户确认画风/语调/版式/语言等选项, 再生成分镜脚本和角色定义 (storyboard + characters)
- 每张图的完整 prompt 先落盘为 prompts/NN-xxx.md 文件, 文件不存在绝不调用图像后端
- 先单独生成角色参考图 (characters.png, 4:3), 再按批 (默认 4 张/批) 生成各页位图, 角色图作为参考传入每一页
- 所有页生成完毕后, 用 scripts/merge-to-pdf.ts 合并为最终 PDF, 输出完成报告

- 图像后端解析优先级: 当前消息指定 > EXTEND.md 固定偏好 > 运行时原生图像工具 (如 Codex imagegen / Cursor GenerateImage) > 仅有的一个非原生后端 (如 baoyu-image-gen) > 都没有则询问用户; 依赖 bun 或 npx 作为脚本运行时
- 硬性约束两条: 禁止用 SVG/HTML/Canvas 等代码渲染替代位图生成; 禁止用 ImageMagick/Pillow 等程序化覆盖修补图内文字, 文字错了只能重生成
- 参考图机制: 角色参考图压缩 (sips 转 JPEG 或 pngquant) 后以 --ref 传入每页保证角色一致; 用户参考图可标记 direct/style/palette 三种用法; 后端不支持多参考图时改为把角色描述内嵌进 prompt 文本
