# extension-object-storage (`caffeinelabs/skills/extension-object-storage`)

## blackbox

**function**: 给你的应用加上"传文件、看文件、下文件"的能力：图片、视频、大文件都能存、能在线看、能下载。

- input: "帮我做一个图片相册：用户可以上传照片，在页面上浏览、点开看大图", output: 一个带上传入口和相册页的应用：照片上传后立即可浏览、点开放大显示
- input: 一个几百 MB 的大视频文件，拖进应用的上传框, output: 上传成功并在页面内直接播放，不会因为文件太大而卡住或失败，上传时还能看到进度
- input: 在应用的文件列表里点击某个文件的"下载", output: 浏览器开始下载这个文件，保留原始文件名（如 report.pdf）和格式，打开就能用
