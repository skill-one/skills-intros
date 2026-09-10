# three (`heygen-com/hyperframes/three`)

## comments

- user: 3D新手, 第一次接视频合成, category: 坑, comment: 照网页教程用 clock.getDelta() 转物体, 导出视频节奏忽快忽慢. 改成 rotation.y = time * 0.7 这种纯时间函数才稳.
- user: 从网页 Three.js 项目迁来的前端, category: 注意, comment: requestAnimationFrame 在这只算预览, 正式帧以 hf-seek 为准. 我把渲染收进一个 renderAt(time), 两个入口都调它, 就不会再不一致.
- user: 接外包的独立开发者, category: 坑, comment: 在 hf-seek 回调里才加载 gltf, 前几秒渲出来是空场景, 白跑一整条渲染. 资源全部顶层 await 完, 再注册 seek.
- user: 渲染出片工程师, category: 注意, comment: renderer 默认跟设备像素比走, 我的视网膜屏上成片和预览对不上. setSize(1920,1080) 后再 setPixelRatio(1), 一次钉死.
- user: 产品广告动画师, category: 妙用, comment: 把粒子初始位置全改成带 seed 的伪随机, 同一秒渲出来帧帧一致, 客户第七次改稿也能精确复现那个角度, 不用碰运气.
- user: 写了十年动画循环的程序员, category: 启发, comment: "画面状态必须能从 time 反推"这个约束, 让我重写了状态的写法, 后来连普通网页动画也这么组织, 拖进度条调试白赚了.
