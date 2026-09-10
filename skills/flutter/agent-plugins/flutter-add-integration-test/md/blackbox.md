# flutter-add-integration-test (`flutter/agent-plugins/flutter-add-integration-test`)

## blackbox

**function**: 给你的 Flutter App 加上自动化测试:它会像真人一样自动打开 App、点按钮、填表单、翻页面,并验证结果对不对,替你把整个用户操作流程变成能反复运行的测试。

- input: 一个 Flutter 项目路径 + 一句话需求,如「给登录功能加上自动化测试」, output: 项目里多出可直接运行的测试文件;运行后会自动打开 App、输入账号密码、点登录按钮、确认进入首页,最后告诉你「通过 ✅」或「失败 ❌ 及原因」
- input: 一段操作描述,如「点加号按钮 3 次,数字应该显示 3」, output: 对应的自动化测试代码;跑一遍即完成点击和验证,以后每次改完代码都能重跑,防止改坏了没发现
- input: 一个跑不过的测试(附报错信息),如「测试卡住不动 / 找不到按钮」, output: 修好的测试:该等的动画等到位、该滚动的列表滚到位,重新运行直到通过
