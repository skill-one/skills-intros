# herdr (`herdrdev/herdr/herdr`)

## whitebox

- 环境门禁: 先验证 HERDR_ENV=1, 确认自己运行在 Herdr 受管 pane 内; 不通过则声明不在 Herdr 中并停止, 绝不从外部控制会话
- 学习 CLI: 运行 herdr --help 和各命令组 (如 herdr agent / herdr pane, 不带子命令) 获取本机二进制的真实语法; 绝不运行裸 herdr (会启动 TUI 界面)
- 发现状态: 用 workspace/pane/agent list 等只读命令探查现有布局和 agent, 从返回的 JSON 中解析 ID (w1:p1 这类不透明稳定句柄), 不靠猜
- 构造布局: herdr pane split --current --direction right --cwd "$PWD" --no-focus 在当前 tab 内切出兄弟 pane, 保持调用者工作目录且不抢用户焦点, 从 .result.pane.pane_id 取新 ID
- 驱动 agent: herdr agent start 启动后, 用 agent prompt ... --wait 提交任务并等待首个稳定状态 (idle/done/blocked), 再用 agent read 读取输出; 若 blocked 说明 agent 卡在审批/提问界面, 先检查再决定输入

- JSON 契约 + 二进制权威: 所有控制命令返回 JSON, 下一步参数一律取自 .result.* 字段 (如 .result.pane.pane_id); CLI 语法以本机安装的 herdr 二进制为准 (--help 自省), 不预测; 语法错误 exit 2, 服务端错误为 stderr 上的 JSON + exit 1
- 上下文注入与作用域隔离: Herdr 向每个受管 pane 注入 HERDR_WORKSPACE_ID / HERDR_TAB_ID / HERDR_PANE_ID, 命令可用 --current 精确指向调用者自身; ID 按 server 作用域隔离, 跨机器同名 ID 不通用
- 终端驱动而非 API: 不通过模型 API, 而是驱动 agent 自己的终端界面——prompt 按方括号粘贴模式 (bracketed-paste) 发送文本+编码 Enter 作为一次有序提交; 读屏支持 visible / recent-unwrapped (合并软换行, 适合日志) / detection 等快照源; Herdr 据此把 pane 内的 agent 识别并分类为 idle / working / blocked / done / unknown 生命周期状态
- 外部依赖: 本机 PATH 中的 herdr CLI 二进制 + 正在运行的 Herdr 服务端会话 (经 socket 通信); 被驱动的编码 agent (如 codex) 需已安装为可用 kind; 常规 bash + JSON 解析, 无任何外部模型 API
