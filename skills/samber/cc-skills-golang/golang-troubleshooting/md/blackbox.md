# golang-troubleshooting (`samber/cc-skills-golang/golang-troubleshooting`)

## blackbox

**function**: 排查并修复 Go 程序的各种毛病——崩溃、偶发出错、程序卡死、变慢、内存暴涨——先找到真正的病根, 再给你修好的代码。

- input: 一个会随机崩溃的 Go 项目路径 + 报错堆栈信息, output: 定位到引发崩溃的具体代码行, 说明为什么会崩, 并交付修复后的代码
- input: 「服务跑几天内存就涨满」+ Go 源码目录, output: 一份诊断结论: 指出是哪段代码在漏内存, 附上修好的代码
- input: 「这个接口有时正常有时报错」+ Go 源码, output: 找出并发的隐藏问题所在位置, 交付修复后的代码和验证方法
- input: 一段输出结果不对的 Go 函数, output: 一个能稳定复现问题的失败测试 + 修好的函数, 并解释错在哪
