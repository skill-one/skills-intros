# flutter-setup-declarative-routing (`flutter/agent-plugins/flutter-setup-declarative-routing`)

## comments

- user: 前端转 Flutter 的新手, category: 坑, comment: 部署后一刷新 /details/1 就 404:用了 path URL 策略后,静态服务器得把所有路径指向 index.html,Nginx 加 try_files 才好。
- user: 原生 Android 转过来的, category: 注意, comment: assetlinks.json 写对了也不生效?debug 签名的 SHA256 对不上,autoVerify 过不了。换 release 签名构建,再用指南里那条 adb 命令测。
- user: 实习第一个月的新手, category: 坑, comment: 全项目都写 context.go,安卓返回键一点直接退出 App。详情页要用 context.push 才有返回栈,tab 切换才用 go。
- user: 踩过 AASA 的 iOS 开发, category: 注意, comment: AASA 文件必须不带 .json 后缀、HTTPS 直连无重定向;Apple 那边有缓存,改完几小时不生效,先怀疑缓存,别急着重写配置。
- user: 带底部导航的电商 App 开发, category: 妙用, comment: StatefulShellRoute.indexedStack 里配 initialLocation: index == currentIndex,再点当前 tab 回到该 tab 首页,各 tab 滚动位置还都保留着。
- user: 混用三方链接插件的人, category: 注意, comment: 同时用 app_links 插件的话,记得把 Info.plist 的 FlutterDeepLinkingEnabled 设为 NO,不然链接被 Flutter 默认处理器抢先,插件收不到。
