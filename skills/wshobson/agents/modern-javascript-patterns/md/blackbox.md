# modern-javascript-patterns (`wshobson/agents/modern-javascript-patterns`)

## blackbox

**function**: 把老旧、难懂或报错的 JavaScript 代码改写成简洁、易维护的现代写法，并顺手修掉常见错误。

- input: 一段用回调函数层层嵌套写的旧 JS 代码（改起来就头痛的那种）, output: 同一功能、用 async/await 改写后的清晰代码，逻辑一目了然
- input: 一段重复啰嗦、变量名混乱的 JS 代码, output: 用现代简洁写法（如解构、箭头函数）重写的精简版本，每处改动附一句说明
- input: 一段运行时报 "Cannot read property of undefined" 的代码, output: 修复后的可运行代码，并指出哪一行会取不到值
