# overdrive (`pbakaus/impeccable/overdrive`)

## whitebox

- 先强制调用 /impeccable 技能收集设计上下文 (Context Gathering Protocol); 若项目尚无任何设计上下文, 必须先跑 /impeccable teach
- 评估目标界面属于哪一类 (视觉营销 / 功能 UI / 性能关键 / 数据密集), 确认 'extraordinary' 在此场景下的具体含义
- 构思 2~3 个技术方向, 连同效果描述与权衡 (浏览器兼容、性能开销、复杂度) 直接向用户提问, 等用户选定后才写代码
- 按选定方向实现: 全程渐进增强 + 性能纪律, 并打磨最后 20% 细节 (缓动曲线、错峰节奏、次级动效)
- 用浏览器自动化工具实际预览、视觉验证、多轮迭代; 最后过五项检验 (wow / removal / device / accessibility / context)

- 双闸门防误触发: /impeccable 上下文是硬性前置, 上下文决定 '惊艳' 是否得体 (创意作品集上的粒子系统 vs 设置页上是尴尬); 本 skill 被标记为误触发风险最高, 故强制 '先提案、用户确认、后编码', 严禁跳步直接实现
- 选题 = 界面类型映射工具箱: 视觉型 → shader / scroll 驱动动画 / 电影感转场; 功能型 → 弹窗 morphing (View Transitions) / spring 物理 / 虚拟滚动; 性能型 → Web Workers / OffscreenCanvas / WASM (不可见但可感); 数据型 → GPU 加速图表; 只增强 '如何感觉', 不新增产品功能
- 校验全靠硬规则: 能力检测回退链 (@supports + WebGPU→WebGL2→CSS 静态回退)、60fps 红线 (低于 50 即简化)、强制尊重 prefers-reduced-motion、WebGL/WASM 等重资源临近视口才懒加载、离屏渲染暂停; 视觉验证依赖外部浏览器自动化工具而非假设; 可选外部库: motion (原 Framer Motion) / GSAP (spring 物理)、Three.js / OGL / regl (WebGL)、TanStack Virtual、deck.gl、D3
