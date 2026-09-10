# delight (`pbakaus/impeccable/delight`)

## whitebox

- 强制前置: 调用 /impeccable 拿到设计原则和 Context Gathering Protocol; 若尚无设计上下文, 必须先跑 /impeccable teach
- 评估机会与语境: 定位可加愉悦感的自然时刻 (成功态/空态/加载/成就/悬停点击/报错/彩蛋), 判断品牌人格、受众、情绪氛围, 定下策略 (含蓄高级 / 玩趣人格 / 贴心惊喜 / 感官丰富)
- 按语境选技法并实现: 微交互动画、人格化文案、定制插画、音效、彩蛋、庆祝时刻等, 落成 CSS/JS 代码
- 验证质量: 检查是否第 100 次仍不烦人、不阻塞任务、无卡顿、契合品牌语境、支持 reduced motion 和屏幕阅读器

- 语境门控: 动手前必须完成上下文收集协议 (品牌人格/受众/情绪/领域适配度, 如银行 app ≠ 游戏 app); 代码库里推断不出的, 直接问用户, 不靠猜
- 实现依赖: 原生 CSS transition/keyframes 为主, 库按需选型——动画 Framer Motion (React) / GSAP / Lottie / Canvas confetti, 音效 Howler.js / use-sound, 弹簧物理 React Spring / Popmotion; 附带体积纪律 (压缩、懒加载愉悦特性)
- 硬性红线约束: 愉悦时刻 <1 秒、可跳过、绝不延迟核心功能; 禁止用愉悦掩盖糟糕 UX、禁止处处都要愉悦 (特殊时刻才特殊)、禁止牺牲性能与可访问性
