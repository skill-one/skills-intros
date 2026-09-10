# error-handling-patterns (`wshobson/agents/error-handling-patterns`)

## comments

- user: 后端老兵, category: 妙用, comment: 把"在能处理的层级捕获"抄进团队代码评审清单, 重复日志肉眼可见地少了, 改动就一行。
- user: 第一次用的新手, category: 坑, comment: 我照感觉写了 except Exception 兜底, 把空指针 bug 吞了排查一整天; 要按指南只捕具体异常。
- user: 运维老哥, category: 注意, comment: 预期内的失败(限流、超时重试)别打 ERROR, 我吃过亏: 告警天天误报, 值班全是日志噪音。
- user: 测试工程师, category: 妙用, comment: 让它给外部服务的报错都包上订单号、金额再重抛, 排障不用翻库, 报错原文自带现场。
- user: 前端转全栈, category: 启发, comment: 以前 try-catch 包一切图安心, 现在明白异常该交给能兜底的层处理, 中间层只透传不吞。
- user: 支付系统开发, category: 注意, comment: 先分清可恢复错误(超时、限流)和代码 bug 再设计, 混成一类的话重试逻辑会把 bug 也重试三遍。
