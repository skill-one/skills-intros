# rust-async-patterns (`wshobson/agents/rust-async-patterns`)

## blackbox

**function**: 帮你写、查错、修好 Rust 异步程序(那种需要同时干很多事、不卡住的程序)。

- input: 一段会卡死或跑得奇慢的 Rust 异步代码 + 你的一句话描述("程序卡住不动了"), output: 指出问题出在哪一行、为什么, 并给出修好的完整代码
- input: 一句需求, 如"帮我写个并发抓取 100 个网页的工具, 同时最多 10 个请求", output: 一份可直接跑起来的完整 Rust 代码, 带并发限制和出错处理
- input: 一段编译报错(如 "future cannot be sent between threads safely")贴给你, output: 用人话解释报错原因 + 具体改哪几行才能通过编译
