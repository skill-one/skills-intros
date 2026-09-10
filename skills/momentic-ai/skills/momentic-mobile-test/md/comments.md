# momentic-mobile-test (`momentic-ai/skills/momentic-mobile-test`)

## comments

- user: 测试转岗新人, category: 坑, comment: 以前我每步后面都加 sleep 等页面加载，又慢又偶发失败。后来改成写一条「出现XX按钮」的检查步骤，它自己会重试，反而更快更稳。
- user: 安卓开发, category: 注意, comment: 测 WebView 页面报 No browser controller，不是环境坏了，是包没开 WebView 调试。换 debug 包，或 release 包显式打开调试开关。
- user: 三年经验QA, category: 妙用, comment: 某步老点错目标时，把步骤描述改准确，它就会重新定位而不是吃旧缓存；预览成功后把 CacheId 带进对应那一步再保存，重跑定位快很多。
- user: 测试组长, category: 启发, comment: 它每次开跑前都先问「用户看到什么才算通过」，我才发现老用例一半只验了「没报错」。现在先定可见的验收状态再写步骤，断言少了却真能拦住 bug。
- user: 外包接手祖传项目, category: 坑, comment: 项目里新旧测试文件混着，我手改了老文件半天不生效。看 fileType 字段分辨：v1 千万别手编，走工具改；只有 v2 能直接编辑 YAML。
- user: iOS开发, category: 注意, comment: 首页轮播图一直动，iOS 上元素定位老超时，干等没用。加个测试开关停掉动画立刻好了——持续动画会卡住无障碍快照，不是设备慢。
