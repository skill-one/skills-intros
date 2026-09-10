# animate (`emilkowalski/skills/animate`)

## whitebox

- 先过两道闸门: 按使用频率判定该不该动 (每天 100+ 次的操作直接拒绝, 输出零代码是成功), 再给动效点名一个目的 (反馈/空间连续性/状态指示...), 点不出名字就不建。
- 从低成本到高成本选工具, 停在第一个够用的: CSS transition → @starting-style → CSS animation → WAAPI → Motion 库。
- 写实现: 只动 transform 和 opacity (clip-path 例外), 曲线、时长、弹簧参数全部查内置表取值, 严禁凭感觉编 cubic-bezier。
- 同步补齐中断与降级: 快速触发的元素用 transition 不用 keyframes, 退出路径镜像入场, prefers-reduced-motion 和 hover 门控与动画一起交付。
- 对照 Never Ship 清单自查 (出现 ease-in、scale(0)、transition: all 即不合格), 然后输出代码加三行说明: 闸门结论、参数清单、需要真人感受验证的点。

- 两段式硬闸门: 频率和目的两个判断在一切之前, 可以否决需求本身——判定不该动效时直接给替代方案 (即时状态切换/静态提示) 而非硬写; 若需求本质是组件 (toast/抽屉/下拉菜单) 则移交 pick-ui-library 技能, 不手搓。
- 查表制, 不做估值: 工具阶梯、属性白名单、缓动曲线表 (--ease-out 等 3 条强曲线)、时长表 (按钮 100-160ms / 下拉 150-250ms / 弹窗 200-500ms, UI 一律 <300ms)、弹簧配置表 (Apple 风格 duration+bounce / 传统 physics 两套) 全部预置; 表里没有的曲线从 easing.dev 或 easings.co 取, 不手调。
- 外部依赖: RECIPES.md 提供按钮按压、下拉、tooltip、modal、drawer、toast、手风琴、stagger、拖拽 dismiss 等成品配方作为起点; 需要弹簧、手势驱动或退出动画时引入 Motion 库 (motion.dev), 且必须写完整 transform 字符串而非 x/y/scale 简写 (否则掉帧); 优先复用代码库已有的 token, 不另起一套平行体系。
