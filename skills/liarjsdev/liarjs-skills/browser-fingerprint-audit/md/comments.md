# browser-fingerprint-audit (`liarjsdev/liarjs-skills/browser-fingerprint-audit`)

## comments

- user: 在 Docker 里跑爬虫的运维, category: 坑, comment: 直接用 root 起容器跑,Chrome 沙箱初始化直接失败。切到非 root 用户并加 --shm-size=1g 才跑通,沙箱也别去关。
- user: 做指纹浏览器的独立开发者, category: 妙用, comment: 每次调完伪装参数前后各跑一次 --json 存档,diff 两份报告,哪个检查项被我改红了一目了然,不用逐项猜。
- user: 被无头模式吓到的爬虫新手, category: 坑, comment: 无头浏览器跑出低分,我以为是工具坏了折腾半天。后来才懂:无头本来就留痕迹,低分是正确结果,别去追这个分。
- user: 风控工程师, category: 注意, comment: 分数只量浏览器自身前后一致。真网站还会看 IP 信誉、账号年龄和行为,我这边 90 分照样被挑战,别当通关凭证。
- user: 公司内网的前端, category: 注意, comment: 默认会向 liarjs.dev 发一次真实请求,我们内网拦截直接报错。受限环境加 --offline 只跑 JS 层,或者 --endpoint 指向自己的部署。
- user: 第一次用的新手, category: 注意, comment: 默认只打印挂掉的检查项,一度以为没跑起来。想看全量加 --all;about:blank 上部分检查不可用,报告会标注,别当 bug。
