# extension-qr-code (`caffeinelabs/skills/extension-qr-code`)

## comments

- user: 第一次接前端的新手, category: 坑, comment: 只挂了 video 忘了挂 canvas, 扫码毫无反应也不报错。把那个隐藏的 canvas ref 上立刻就好了——可以 display:none, 但必须存在。
- user: 五年 React 前端, category: 注意, comment: video 要加 playsInline 和 muted。我漏了 muted, iPhone 上黑屏不自动播放; 漏了 playsInline 会全屏顶开页面。照示例代码抄全就行。
- user: 公司内网运维, category: 妙用, comment: 内网访问不了 CDN, jsQRLoaded 一直 false。把 jsQR 下载到自家服务器, 给 jsQRUrl 传内网地址就通了, 这个配置项救了我。
- user: 独立开发者, category: 注意, comment: scanInterval 默认 100ms 相当于每秒解码 10 帧, 长时间开扫码手机发热掉电。签到场景我改 300ms 体验没差, 再用 maxResults 限制历史条数。
- user: 活动现场运营, category: 启发, comment: 同一个码会被反复识别塞进结果。我按 data 去重、timestamp 当 key, 每签完一位就 clearResults(), 一人一清不串签。结果最新在前很顺手。
- user: 后端老兵偶尔客串前端, category: 坑, comment: isSupported 初始是 null 不是 false, 我直接当布尔判断, 页面闪了「摄像头不支持」。用户拒授权后别让人刷新, error 时给按钮调 retry() 就能重来。
