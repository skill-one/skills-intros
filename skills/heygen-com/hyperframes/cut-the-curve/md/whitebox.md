# cut-the-curve (`heygen-com/hyperframes/cut-the-curve`)

## whitebox

- 触发条件: 任务涉及转场、文字节拍交接、动态文字入场或组合滑动; 第一步先读 motion-doctrine 中的 seam 法则 (向量定律、current、ledger、Seam Gate)
- 从 7 个技法的目录表里按 scope/axis/用途匹配技法 (场景边界→Cut the Curve, 同景文字换→Zoom-Through, 到达/回报节拍→Inverse Zoom, 标题卡/段落开场→Waterfall Entry, 组内让位→Nudge Curve)
- 按目录中的硬参数排时间轴: 行程取画面 ~12% (±230px@1920)、切口两侧镜像缓动 (power4.in/power4.out 或 power3.in/expo.out)、模糊峰值按主体定、级联间隔按元素重量递减
- 从 examples/gsap-implementation.md 取对应 GSAP 代码模板 (worker + registry) 生成实现
- 过 Seam Gate 各条校验 (含 Z 符号、切口两侧模糊/透明度一致、#root 不透明背景) 并对照反模式表, 不符即修正后输出

- 速度匹配剪切原理: 在峰值速度处剪切, 切口两侧方向与速度必须一致 — 靠镜像缓动实现 (出 power4.in + 入 power4.out, 同距离同时长, 等效一个 power4.inOut 的两半); Z 轴额外校验 scale 变化率的符号 (推/拉不可互反, 切口±0.1s 内来方场景不得自带从小到大的入场)
- 参数化规则集: 模糊按主体定档 (文字 10px / 全幅表面 18–20px, 模糊只加在 wrapper); §6 入场用 tl.set 二值 0→1 (禁渐显) 且间隔逐元素收缩 (×0.84); §7 滑动用三段缓动链 (power3.in→线性→power4.out, 时长约 20/18/62%); 全程只用 transform/opacity 以保证可 seek
- 外部依赖仅 GSAP 一个库: 全部实现为 GSAP 时间轴代码, 模板统一取自 examples/gsap-implementation.md; 无模型 API, 校验靠静态规则 (Seam Gate 条目 + 反模式清单) 而非运行时检测
