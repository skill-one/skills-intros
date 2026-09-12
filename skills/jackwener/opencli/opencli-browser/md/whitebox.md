# opencli-browser (`jackwener/opencli/opencli-browser`)

## whitebox

- opencli doctor 自检: 确认 Chrome 在跑、Browser Bridge 扩展已装、调试端口未被拦截, 不绿则后续全不工作
- browser state 拍页面快照: 输出带 [N] 数字引用的结构树, 从中选定目标元素 (复杂控件看 compounds 侧栏)
- browser click / type / select <target>: 用数字引用或 CSS 选择器执行操作, 表单写入用 fill / select, 返回操作结果 envelope
- 校验与跟进: 重要写入后 get value 复核 (React 受控输入可能静默吞字); 页面跳转或 SPA 路由变化后必须重新 state 取新引用
- 收尾: browser close 释放会话占用的标签页租约 (或等空闲超时自动释放)

- 选择器优先目标契约 + 元素指纹: 操作目标只能是 state/find 发的数字引用或 CSS 选择器; 每个 envelope 返回 matches_n 和 match_level (exact/stable/reidentified), DOM 轻度漂移时 CLI 按元素指纹重新定位并重新打标签
- 机器可读结构化返回: 所有子命令输出 JSON envelope; 失败时给 error.code (not_found/stale_ref/selector_ambiguous/option_not_found 等) 供程序分支, 并附候选选择器或真实下拉选项; 日期/下拉/文件控件走 compound 字段 (格式模板、最多 50 条选项表、accept/multiple)
- 网络捕获优先于屏幕抓取: browser network 截获页面 JSON API 响应, 缓存于 ~/.opencli/cache/browser-network/, --detail <key> 单独取完整 body, 不必重新触发请求; 文件上传经 CDP 附加到 input[type=file]; 外部依赖: 本机 Chrome + Browser Bridge 扩展 + opencli CLI/守护进程
