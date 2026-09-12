# chrome-devtools (`github/awesome-copilot/chrome-devtools`)

## blackbox

**function**: 替你操作和检查一个真实的 Chrome 浏览器: 打开网页、点按钮、填表单、截图, 并告诉你页面为什么报错、为什么慢。

- input: 一个网址 (如 https://example.com), output: 该页面的截图 + 页面上有什么内容的简要说明
- input: 一个网址 + 一组账号信息, 指令「帮我登录/填表/下单」, output: 完成后的页面状态 (截图确认), 遇到弹窗或验证会停下来问你
- input: 「这个网页一打开就报错, 帮我看看」+ 网址, output: 具体报错原因: 哪段脚本挂了、哪个请求失败 (如 404/500), 附出错证据
- input: 「这个网站打开要 10 秒, 慢在哪」+ 网址, output: 性能体检报告: 拖慢加载的元凶 (大图片/慢接口等) 及改进建议
- input: 「看看我的网页在手机上长什么样」+ 网址, output: 模拟手机屏幕尺寸后的页面截图
