# gsap-plugins (`greensock/gsap-skills/gsap-plugins`)

## comments

- user: 被旧教程坑过的外包前端, category: 坑, comment: 照老教程配 .npmrc 填 GreenSock token 装包，一直 403。其实现在 npm i gsap 就包含全部插件，免费、不需要任何密钥。
- user: 第一次用的新手, category: 坑, comment: 用 ScrollToPlugin 忘了 registerPlugin，点击后瞬间跳到目标、没有滚动动画，控制台还不报错。加一行注册就修好了。
- user: UI设计转前端, category: 注意, comment: DrawSVG 只动画描边不动填充。path 没先在 CSS 设 stroke 和 stroke-width 就 from 0，画面一片空白，设上才画出来。
- user: H5活动页作者, category: 注意, comment: Draggable 填了 inertia:true 却没注册 InertiaPlugin：拖拽正常、松手惯性消失，全程无报错，容易以为是自己写法错了。
- user: 交互动画爱好者, category: 妙用, comment: MorphSVG 变形中途扭曲打结，先跑一次 shapeIndex:'log'，把控制台自动算出的数值贴回动画参数，形状立刻正常。
- user: 独立全栈开发, category: 注意, comment: 自定义字体没加载完就 SplitText，断行位置是错的。改用 autoSplit:true 并在 onSplit() 里返回动画，字体重排会自动重切。
