# flutter-build-responsive-layout (`flutter/agent-plugins/flutter-build-responsive-layout`)

## comments

- user: 第一次用的新手, category: 坑, comment: 用 OrientationBuilder 判断横竖屏切布局,折叠屏上界面直接裁掉一半。换 LayoutBuilder 按 constraints.maxWidth 判断才正常,顶层别用横竖屏。
- user: 独立开发者, category: 注意, comment: 产品硬要求锁竖屏,结果折叠屏展开后 App 居中带黑边,MediaQuery 还拿不到大屏尺寸。真要锁屏,只能改用 Display API 读物理屏幕尺寸。
- user: 前端转 Flutter 的, category: 妙用, comment: 列表在大屏被拉超宽,我换 GridView.builder 配 SliverGridDelegateWithMaxCrossAxisExtent,窗口拖宽自动加列,不用手写断点。
- user: 桌面端适配老哥, category: 注意, comment: 桌面上窗口能随便拖,写死的宽度逻辑全崩。别判断手机还是平板,一切按窗口实际宽度走,600 这个断点我用着挺稳。
- user: 实习生, category: 坑, comment: 表单没限宽,平板横屏下输入框被拉得巨长没法看。套一层 Center + ConstrainedBox(maxWidth: 800) 居中,大屏立刻能看了。
- user: 测试出身, category: 启发, comment: 以前适配要攒一堆真机,现在拖窗口边缘就能看全各断点的布局切换,再跑 validator 直接报溢出位置,我改掉了等真机才测的习惯。
