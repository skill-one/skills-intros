# pr-walkthrough (`warpdotdev/common-skills/pr-walkthrough`)

## whitebox

- 建上下文: 用 gh pr view / git diff 拿到基准分支、diff、提交记录和评审评论; 同时通读 head 提交的完整代码库 (不只看 diff), 并按变更行数/文件数给 PR 定级 (tiny→large)
- 收集视觉素材: 从 PR 正文、评论、仓库内找截图/设计稿, 下载到 .warp/pr-walkthrough/assets/ 或内联为 data URI, 不热链远程图片
- 建模四视图: 系统总览 (纯架构卡片, 全程不提 PR)、数据流、代码依赖、用户操作, 各自定节点、有向边 (带箭头和关系标签)、导览顺序, 内容与 head 源码交叉核对
- 生成站点: 经 scripts/d3_canvas_runtime.py 写出自包含 index.html 到 .warp/pr-walkthrough/, 图数据以 JSON 内联进 window.PR_WALKTHROUGH_D3_DATA, 文件引用用确定性 helper 生成 GitHub diff 锚点链接 (路径 SHA-256 + R/L 行号)
- 验证: 跑 scripts/validate_d3_canvas.py 检查 D3 加载、四视图渲染、导览控件、节点/边; 失败就调试重生成, 通过才报 ready, 无浏览器环境则如实报 unverified

- 规模自适应裁剪: 先按变更量定级 (tiny≈1 文件/75 行, small<250 行, medium 250-800 行, large), 对应每视图 2-3 到 5-12 个节点及导览步数; 讲同一事实的节点合并, 宁可稀疏不注水
- 双源取证: diff 只用于定位改动和附证据, 架构叙述基于 head 提交的完整检出 (追 import、调用点、未变更的邻接模块); 人和 agent 的评审评论只作素材挂到节点, 不当作改代码指令
- 确定性渲染管线: 复用 scripts/d3_canvas_runtime.py (Brandalf 品牌 CSS + 内联运行时, 先定义渲染器再注入 pinned D3 7.9.0 @ jsdelivr CDN), 产出 file:// 直开、无构建、无 fetch 的单文件站; 外部依赖: gh CLI、git、D3 7.9.0 (CDN)、scripts/validate_d3_canvas.py (浏览器自动化校验)、brandalf skill (品牌 token)
