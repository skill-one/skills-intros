# argent-metro-debugger (`software-mansion/argent/argent-metro-debugger`)

## blackbox

**function**: 连上你正在运行的手机 App 或桌面应用, 帮你查看屏幕上的界面、读取报错日志、当场执行代码, 找到并修复运行中的问题。

- input: 一句「连上我正在跑的 App, 看看为什么一直白屏/报错」, output: 具体的错误信息清单, 每条注明出自哪个文件哪一行; 掉线、需要重新加载这类问题直接帮你当场恢复
- input: 「这个页面由哪些部分组成? 那个按钮在屏幕什么位置?」, output: 当前屏幕的组件清单: 每个元素的名字、层级关系和位置坐标
- input: 一段想验证的代码或问题, 如「帮我看看这个变量的值现在到底是多少」, output: 这段代码在正在运行的 App 里真实执行后的返回结果
