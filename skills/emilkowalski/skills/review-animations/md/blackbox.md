# review-animations (`emilkowalski/skills/review-animations`)

## blackbox

**function**: 专审网页动画/动效代码: 逐条指出哪里生硬、卡顿、多余, 给出改法, 最后判定「放行」还是「打回」。

- input: 一段实现下拉菜单展开动画的 CSS 代码, output: 一张问题清单表格 (每行: 现在的写法 → 应改成什么 → 为什么), 末尾附明确结论: 放行 / 打回
- input: 一个带 Framer Motion 动效的 React 组件代码, output: 逐条动效问题, 标注文件和行号, 每条附可直接粘贴的修改代码, 最后给出是否通过的判定
- input: 一个 diff: 给高频点击的按钮加了 500ms 缩放动画, output: 判定「打回」+ 一句话理由 (高频操作不该有动画) + 建议 (直接删掉或改快到 150ms 内)
