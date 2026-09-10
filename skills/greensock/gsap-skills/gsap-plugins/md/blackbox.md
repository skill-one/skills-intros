# gsap-plugins (`greensock/gsap-skills/gsap-plugins`)

## blackbox

**function**: 把你的网页动效需求写成能直接跑的 GSAP 代码 (GSAP 是一个主流网页动画库) —— 滚动、拖拽、图形变形、逐字文字动画等, 还能帮你修动画报错。

- input: 一句需求: 「点击导航后, 页面平滑滚动到对应区块」, output: 一段可直接粘贴运行的 JS 代码, 含插件注册, 粘上就生效
- input: 一段会报错/不动的动画代码, output: 修好的代码 + 一句话说明问题 (如漏了插件注册、用了过期的付费安装方式)
- input: 一个 SVG 图形 + 需求: 「想让它像被人手绘出来一样出现」, output: 用 DrawSVG 描边动画实现的代码, 线条从无到有逐渐画出来
- input: 布局代码 + 需求: 「卡片交换位置时想要流畅的过渡, 而不是瞬间跳过去」, output: 用 Flip 插件补上的代码: 卡片平滑滑动到新位置
- input: 需求: 「标题文字逐个字蹦出来」, output: 用 SplitText 实现的逐字动画代码
