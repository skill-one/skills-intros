# multi-account-isolation (`antibrow/anti-detect-browser-skills/multi-account-isolation`)

## whitebox

- 用 anti-detect-browser SDK 逐个启动身份: 一个身份一个 profile + 一个专属代理 + 一份冻结 persona, 开 geoip 让时区跟随代理出口。
- 在各自代理通道内跑机械断言: browser.timezone 对 public_ip 国别、WebRTC 只暴露代理 (browserleaks)、canvas 哈希跨重启重读一致, 再横向 diff 整个车队的 persona / public_ip / profile_dir。
- 跑跨层一致性套件: CreepJS (Worker 与主线程、GPU 三接口)、whoer / pixelscan 全栈速览、`npx liarjs` 跑约 40 条开源规则做无人值守 CI 校验。
- 有失败时按成本从低到高排查: profile 目录是否复用 → 出口 IP 是否撞车 → 时区与 IP 是否矛盾 → persona 是否被重新生成 → 最后才怀疑指纹本身。
- 全绿则收窄结论为 '浏览器技术层自洽', 并明示不覆盖浏览器之外的因素 (同付款方式、同联系方式、行为模式)。

- 断言而非肉眼, 核心是配置不变量: 1 身份 = 1 profile = 1 persona = 1 代理 = 1 时区, 任何一格被两个身份共享即判缺陷; 具体做法: 时区对出口 IP 国别、按 profile.json (而非目录名) 比对 profile_dir 和 user-data/ 是否串号。
- 冻结回放做稳定性判据: persona (persona.json) 只生成一次并冻结, 每次启动回放同一套指纹; 若 canvas/WebGL 哈希在两次 launch 间变化, 这个 '每次都不一样' 本身就是异常信号, 说明 persona 没被冻结。
- 依赖 anti-detect-browser SDK (内核为闭源 Chromium 构建, 欺骗逻辑在 C++ 而非注入脚本), 外部检测站 browserleaks.com/webrtc、CreepJS、whoer.net、pixelscan.net, CI 用 liarjs; 内核不盲信, 经 redacted_args() (脱敏后的内核命令行)、本地 MITM 代理、固定 SDK 版本 + dist.integrity 哈希核验; 全程不涉及模型 API。
