# modern-javascript-patterns (`wshobson/agents/modern-javascript-patterns`)

## comments

- user: 后端转前端的 Java 程序员, category: 坑, comment: 把 .then 链机械换成 await 却没包 try/catch,接口一挂函数直接中断,页面静默失败查了一下午。现在每个 await 都套 try/catch。
- user: 第一次用的新手, category: 坑, comment: 把按钮事件回调的 function 改成箭头函数,this 不再指向按钮,取值全失效。有 this 的回调别急着换箭头函数。
- user: 维护祖传代码的前端, category: 妙用, comment: 接口取值全写成 res?.data?.list ?? [],后端偶尔漏字段也不崩,一行替代了我原来的三层 if 判空。
- user: 前端团队负责人, category: 注意, comment: const 只是引用不可变,数组照样能 push。我定规范:要防改的数据必须先 [...arr] 或 {...obj} 复制一份。
- user: 接外包活的前端, category: 妙用, comment: 重构老项目不搞大换血,我专挑回调嵌套最深的请求代码换 async/await,缩进从五六层变一层,单文件收益最大。
- user: 自学转行写脚本的, category: 启发, comment: 用 map/filter 替代 for 循环后,函数不再改外部变量,拆小后测试只盯一个函数,改需求也只动一处。
