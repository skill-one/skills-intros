# motion-doctrine (`heygen-com/hyperframes/motion-doctrine`)

## whitebox

- 先写 vector ledger: 每个剪辑缝一行 (ledger.json), 声明切点时间、出/入向量 (轴 + 带符号方向, Z 行带缩放符号)、选择器、技法
- 跑 seam-stamp.mjs --ledger ledger.json --write index.html, 从 ledger 生成接缝代码 — 盖章的缝「构造上」即合格, 手写仅限 Tier-A morph / match-cut
- 逐场景编排: 每个阶段指定一条持续动效路线, 补载体 (carrier) 与因果链; 实现细节路由到低层技法 skill (cut-the-curve / oversized-cursor / seam-craft)
- 跑 seam-gate.mjs verify --ledger ledger.json --project ., exit 0 才算完工; FAIL 则改 ledger 或场景后重跑 (场景首尾 ~1s 的任何改动会重开该缝的审计)

- 声明式账本先行: 全部接缝决策固化在 ledger.json (schema 见 references/seam-gate.md); 出/入向量不匹配 → 改方案而非改缓动; 校验前先静态检查每行自洽 (方向是否互为镜像、Z 符号等)
- 代码生成: seam-stamp.mjs 为 Node.js 脚本, 读 ledger 直接把接缝写入 index.html; 动效缓动统一用 GSAP 记法 (power4.in/out、back.out(1.4–1.7); 禁 bounce.out / elastic.out), 无模型 API 依赖
- 数值校验: seam-gate.mjs verify 逐缝检查 — 出场在切点仍在运动、入场中途接棒 (不得静止起步)、实测方向=账本方向、速度匹配 (仅 WARN)、零重叠 (切点仅一侧可见)、Z 轴 d(scale)/dt 两侧同号、carrier 矩形连续 (含祖先缩放); 另有 probe --t <cut> 定位缝上真实 carrier 选择器供写账本时使用
