# playwright-stealth-verify (`liarjsdev/liarjs-skills/playwright-stealth-verify`)

## whitebox

- 接入被测浏览器: 调用 checkPage(用户已有的 Playwright/Puppeteer Page), 或 npx liarjs --cdp 接一个已在运行的浏览器; 默认则在临时目录自建一次性 profile, 用完即删
- 在页面内 evaluate 执行 32 项 JS 层探针 (默认跑在 about:blank), 采集 navigator.webdriver、补丁 API 完整性、Worker 一致性、WebGL/WebGPU 等 client 指纹
- 非 --offline 时, 让浏览器请求 liarjs.dev/api/net.json, 拿到网络边缘视角: IP、ASN、HTTP 版本、TLS 版本、ClientHello 形状、请求头
- 汇总 client + server 两侧数据为 ScanResult {score, label, checks[], client, server, meta}, 按各检查项的扣分上限累计出总分
- 用户在测试套件里对结果断言: 例如 expect(result.score).toBeGreaterThanOrEqual(85), 或只过滤 status === 'bad' 的关键检查项

- 鸭子类型接入: checkPage 只要求对象暴露 evaluate(expression: string), Playwright 与 Puppeteer 的 Page 都符合 —— 量测用的就是被测 harness 本身, 带着它真实的启动 flags、插件和代理
- 跨上下文一致性校验: 探针对比主线程与 Web Worker 是否讲同一个故事 (worker-consistency, 部分覆写只打了主线程的典型破绽); 检查被注入的覆写是否仍返回 [native code] (native-integrity); 对比 WebGL 与 WebGPU 报告的 GPU 是否同一张卡 (gpu-triad); 另有 HeadlessChrome UA token、window.chrome 缺失、H.264 codec 与 Chrome 声明不符等启动态检查
- 双视角印证 + 出网可控: JS 层 32 项检查与网络边缘观测 (IP/ASN/TLS 指纹/请求头) 相互对照; --offline 只跑 JS 层、零出网, --endpoint 可指向自部署的 Worker 把流量留在自家基础设施内; Node ≥22, 零运行时依赖
