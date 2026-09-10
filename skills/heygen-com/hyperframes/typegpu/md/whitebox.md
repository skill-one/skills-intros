# typegpu (`heygen-com/hyperframes/typegpu`)

## whitebox

- 页面加载:在任何 await 之前同步构建 GSAP timeline 并挂到 window.__timelines,播放器立即可读
- 异步初始化:await navigator.gpu.requestAdapter() → requestDevice() → canvas.getContext("webgpu") → configure
- 构建管线、buffer、bind group,立即 render(0) 出首帧
- 每次 seek:监听 hf-seek 事件,取 e.detail.time 写入 time uniform → 编码 render pass → pass.draw(3) → submit
- 渲染/导出模式:GPU 提交后 await device.queue.onSubmittedWorkDone(),确保画布刷帧后再截帧

- 确定性渲染契约:GPU 初始化异步、GSAP tween 必须同步;渲染只响应 hf-seek / window.__hfTypegpuTime(禁止 rAF 和 performance.now),时间由 HyperFrames typegpu 适配器以 CustomEvent 发布;随机数用种子化 PRNG
- GPU 绘制手法:WGSL 全屏大三角形顶点着色器(免 vertex buffer);毛玻璃用两趟方案(降采样到 1/6 分辨率再双线性上采样),玻璃内/环带/外区域用 rounded-rect SDF 划分;视频纹理用 copyExternalImageToTexture 按原始分辨率建纹理,alphaMode 按 opaque(全帧)/premultiplied(透明叠层)二选一
- 外部依赖:WebGPU(navigator.gpu)、WGSL 着色器、GSAP(时间线注册)、HyperFrames typegpu 适配器、FFmpeg(生产渲染时预抽视频关键帧为 PNG,绕过 headless Chrome 下 copyExternalImageToTexture 失败)
