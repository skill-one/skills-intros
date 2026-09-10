# best-practices (`addyosmani/web-quality-skills/best-practices`)

## whitebox

- 触发后, 若渲染页面可用, 先通过 Chrome DevTools MCP 跑 lighthouse_audit 实测 Best Practices (正常加载用 navigation 模式, 需保留当前状态用 snapshot 模式)
- 检查审计列出的 console / network 失败项, 仅在某项能支撑一条发现时才拉取该详情
- 用依赖 (npm audit)、HTTP 响应头、配置和源码检查补充运行时证据, 因为 Lighthouse 不等于完整安全评估
- 修复涉事代码后重跑同一审计验证, 安全问题与风格偏好分开报告

- 证据先行 + 闭环验证: 现场实测优先 (Chrome DevTools MCP 的 lighthouse_audit), 工具不可用时降级为 Lighthouse CLI + 针对性依赖与响应头检查; 明确规则: 绝不拿高 Lighthouse 分数当安全证明
- 安全检查走 references/SECURITY.md 参考: 覆盖 HTTPS/HSTS、CSP 与 Trusted Types、SRI (第三方脚本指纹锁定)、依赖补丁、HTML 净化、Cookie
- 清单驱动输出: 按 安全→兼容→代码质量→UX 四类核对项 (checklist) 逐条校验, 外部工具仅用 SKILL.md 列出的: npm audit、SecurityHeaders.com、W3C Validator、Observatory
