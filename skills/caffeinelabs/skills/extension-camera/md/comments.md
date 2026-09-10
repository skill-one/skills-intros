# extension-camera (`caffeinelabs/skills/extension-camera`)

## comments

- user: 第一次用的新手, category: 坑, comment: 预览区没给高度, 视频直接塌成 0, 我还以为摄像头坏了。外面包一层固定 aspect-ratio 或加 min-height 就好了。
- user: 前端工程师, category: 妙用, comment: capturePhoto 直接返回 File 对象, 塞进 FormData 就能传后端; canvas 挂 display:none 藏起来完全不碍事, 省了个截图库。
- user: 移动端老哥, category: 注意, comment: video 标签记得加 playsInline 和 muted, 少了它 iPhone 上会强行全屏播放, 预览直接废掉。
- user: 桌面端产品经理, category: 注意, comment: 桌面浏览器切换摄像头不生效, 只有 environment 模式可用。我把切换按钮在桌面端隐藏了, 免得用户点了没反应来提 bug。
- user: 独立开发者, category: 妙用, comment: 手机拍照上传场景我把 quality 调到 0.6、格式用 jpeg, 照片体积小一大半, 后端存图压力立减。
- user: 后端老兵, category: 坑, comment: 相机没就绪就点拍照, capturePhoto 返回 null, 我把 null 直接传上传接口报了 500。现在按钮一律 disabled={!isActive}。
