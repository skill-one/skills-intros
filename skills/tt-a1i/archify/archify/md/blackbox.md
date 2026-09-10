# archify (`tt-a1i/archify/archify`)

## blackbox

**function**: 把一段文字需求或 Mermaid 图变成一张精美、可交互的架构/流程/时序图 HTML 文件,浏览器打开即可查看、缩放、搜索关系,还能导出成 PNG/SVG 图片。

- input: 一段白话描述, 如「用户请求先到网关, 经过认证服务校验, 再由订单服务写入数据库, 通知走消息队列」, output: 一个双击就能在浏览器打开的交互式架构图 HTML: 节点分色、箭头带语义标注, 支持明暗主题切换、点击高亮某条链路, 可一键导出 PNG/SVG
- input: 一段现成的 Mermaid 代码 (flowchart / sequenceDiagram / stateDiagram), output: 同含义但排版和视觉更专业的交互图 HTML, 替代 Mermaid 默认的朴素样式
- input: 一个本地代码仓库路径 + 一句话, 如「画出这个项目里一次下单请求的真实调用链」, output: 基于仓库真实代码核对后的时序图 HTML, 而不是凭空猜测的示意版本
