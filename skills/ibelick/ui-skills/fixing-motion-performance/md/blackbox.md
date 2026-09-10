# fixing-motion-performance (`ibelick/ui-skills/fixing-motion-performance`)

## blackbox

**function**: 我审查并修复网页动画卡顿问题——动画掉帧、滚动卡顿、过渡不流畅时, 给出具体到行的修改方案。

- input: 一个含动画代码的文件路径 (如 styles.css、animation.js), output: 一份审查报告: 逐条列出问题代码原文、一句话说明为什么会导致卡顿、以及改好的代码写法
- input: "我的页面滚动时动画一卡一卡的" + 相关代码片段, output: 修复方案: 替换前后代码对照, 直接粘贴就能消除卡顿
- input: 一段准备上线的新动画代码 (如弹窗过渡、入场动效), output: 上线前检查结论: 哪里会在用户机器上拖慢页面、哪些写法没问题, 附可直接使用的修复代码
