# typescript-advanced-types (`wshobson/agents/typescript-advanced-types`)

## blackbox

**function**: 编写和修复 TypeScript 的高级类型定义——相当于给代码里的数据做一份更精确的"规格说明书",让数据用错时编辑器立刻报警,而不是等到程序跑崩才发现。

- input: 一句类型需求,如「把 User 对象的每个属性都变成只读,并剔除 password 字段」, output: 可直接粘贴使用的类型代码,如 Readonly<Omit<User, 'password'>>,并附一行效果说明
- input: 一段已有接口代码,如 User 对象的定义, output: 派生出的新类型,如自动为每个属性生成 getName():string、getAge():number 这类 getter 的类型定义
- input: 一段报错的类型代码 + 编辑器里的红色报错信息, output: 修正后能通过编译的代码,附简短说明错误原因和更稳妥的写法
