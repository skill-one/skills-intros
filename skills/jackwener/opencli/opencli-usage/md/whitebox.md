# opencli-usage (`jackwener/opencli/opencli-usage`)

## whitebox

- 先跑 opencli list -f json 拉取当前适配器注册表 — 它是唯一事实来源，不硬编码命令清单。
- 按任务匹配 opencli <site> <command>，看 strategy 标签定前置条件：PUBLIC/LOCAL 免浏览器，COOKIE/INTERCEPT/UI 需已登录的 Chrome + OpenCLI 扩展（Electron 应用需先运行）。
- 没有现成适配器就路由到专项技能：opencli-browser 即时驱动浏览器、opencli-autofix 修适配器、smart-search 路由查询。
- 执行命令，统一用 -f json 输出给上层消费。
- 若失败源于站点改版，带 --trace retain-on-failure 重跑，按错误里的 trace 定位适配器源码修补后重试，最多 3 轮。

- 统一命令面：网站 / Electron 桌面应用 / 外部 CLI 全部包装成 opencli <site> <command>；适配器存于 clis/（内置）与 ~/.opencli/clis/（用户私有，免构建热加载），外部工具经 opencli external install/register 包装为透传（如 opencli gh pr list，继承 stdio、透传退出码）。
- 策略分层决定浏览器依赖：PUBLIC 纯 HTTP 免浏览器；COOKIE 靠扩展直接复用你已登录的 Chrome 会话凭证（免重新登录）；INTERCEPT 额外开自动化窗口捕获签名请求；UI 做全 DOM 交互；LOCAL 走本地端点；Electron 应用走 CDP（Chrome 调试协议）。opencli doctor 只诊断浏览器桥（daemon + 扩展 + Chrome 连通性），PUBLIC/LOCAL 不依赖它。
- 自修复协议：适配器命令失败（选择器漂移、API 轮换）时，--trace retain-on-failure 在错误信封里附 trace 块指向 summary.md，只修补其中的 adapterSourcePath 再重试，上限 3 轮；禁止静默降级为手写 fetch。外部依赖：Node ≥ 21、Chrome + OpenCLI 扩展，无模型 API。
