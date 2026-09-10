# playwright-stealth-verify (`liarjsdev/liarjs-skills/playwright-stealth-verify`)

## comments

- user: 自动化测试工程师, category: 妙用, comment: CI 里我断言 checks 无 bad 项，比只卡 85 分强。升 Playwright 后 worker-consistency 变红，当场抓到插件只补了主线程、漏了 Worker。
- user: 写爬虫五年的老哥, category: 坑, comment: 以为装了隐身插件就稳了，一跑 worker-consistency 扣 20 分：插件只改主线程，Worker 里 navigator.webdriver 还是 true。别猜，扫一遍看坏项 id。
- user: 第一次用的新手, category: 坑, comment: 第一次跑出三十多分差点提 bug，后来明白无头 Chrome 本来就该低分，是正常测量不是故障。照坏项 id 改：ua、viewport 归启动参数，webdriver 归驱动。
- user: 内网安全运维, category: 注意, comment: 测试环境禁外联，直接跑会卡在 liarjs.dev 那步。加 --offline 只跑 32 项 JS 检查；要网络视图就 --endpoint 指向自部署。另注意 Node 得 22+。
- user: 自研浏览器维护者, category: 妙用, comment: 自己打补丁的 Chromium 起在 9222 端口，--cdp 直接连上去测，测试代码零改动。gpu-triad 抓到 WebGL 和 WebGPU 报的显卡对不上，肉眼根本看不出。
- user: 风控团队 Tech Lead, category: 启发, comment: 以前同事一句「加了插件应该没事」就放行。现在规矩：上线前跑 liarjs，有 bad 项不许过。指纹从玄学变成 CI 里的数字，评审终于不用吵了。
