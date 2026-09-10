# remotion-to-hyperframes (`heygen-com/hyperframes/remotion-to-hyperframes`)

## whitebox

- ① Lint 源码: 跑 scripts/lint_source.py 扫 Remotion 源目录, 命中 blocker (如 useState) 则停下并给出 interop 建议; 命中 warning (如 @remotion/lambda) 则丢弃该构造继续
- ② 规划翻译: 读 references/api-map.md 索引, 按源码实际用到的 API 只加载对应主题参考 (timing/sequencing/media/fonts 等)
- ③ 生成 HF composition: 输出 index.html —— 带 data-* 属性的 stage div + 扁平场景列表 + 内联样式 + 底部单个 paused GSAP timeline, 并注册 window.__timelines
- ④ 校验: 两侧分别渲染 (npx remotion render 出基线, npx hyperframes render 出译文), scripts/render_diff.sh 做 SSIM 对比, 低于该复杂度档阈值则用 frame_strip.sh 定位漂移帧并修正
- ⑤ 记录缺口: 未能干净翻译的部分 (音量渐变被丢弃、字体替换等) 写入 TRANSLATION_NOTES.md

- Lint 门禁: lint_source.py 把模式分成 blocker / warning / info 三级 —— useState、非空 deps 的 useEffect、React UI 库 (MUI/antd 等) 视为不可翻译, 拒译并指向 PR #214 的 runtime interop 方案; @remotion/lambda、delayRender 等只是警告, 丢弃后继续翻译其余部分
- 机械式 API 映射: 依赖 references/api-map.md 总索引 + 按需加载的主题参考, 把 Remotion 惯用法 (useCurrentFrame/interpolate/spring/Sequence) 映射为等价物 —— 每个帧驱动计算变成同一个 paused gsap.timeline 上的 tween; 运行时依赖 GSAP + HyperFrames 渲染器
- 量化校验而非目测: 两侧渲染必须统一像素格式 (remotion.config.ts 设 png + bt709), 否则 SSIM 差值量的是编码器差异 (~0.05) 而非翻译保真度; 通过 render_diff.sh 对比, 阈值取源复杂度档 p05 再减 ~0.02; assets/test-corpus/run.sh 跑 T1-T4 语料做回归
