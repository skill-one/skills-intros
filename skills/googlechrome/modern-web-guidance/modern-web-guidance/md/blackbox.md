# modern-web-guidance (`googlechrome/modern-web-guidance/modern-web-guidance`)

## blackbox

**function**: 给你「现在最该怎么做」的网页前端开发最佳实践: 当你要做某个网页功能 (弹窗、动画、图片加载优化等) 时, 帮你查到对应的标准做法指南, 避免写出过时代码。

- input: 「我想做一个弹窗对话框」这类需求描述, output: 几条匹配的最佳实践指南清单: 每条含指南名称、解决什么问题、用到哪些现代浏览器功能
- input: 一个指南 ID, 如 optimize-image-priority, output: 该指南的完整内容: 具体实现步骤和兼容性注意事项
- input: 「页面首屏加载太慢, 图片怎么优化?」这类性能问题, output: 对应场景的优化指南, 如图片加载优先级、延迟渲染非首屏内容等做法
- input: 「列出所有指南」(不确定关键词时), output: 全部可用指南的总目录, 供逐条浏览挑选
