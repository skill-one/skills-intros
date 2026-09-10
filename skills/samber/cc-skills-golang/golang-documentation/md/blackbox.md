# golang-documentation (`samber/cc-skills-golang/golang-documentation`)

## blackbox

**function**: 给 Go 项目补齐或审查文档：代码注释、README、CHANGELOG 等，你给项目路径或源码文件，我直接产出写好的文档或审查报告。

- input: 一个 Go 项目的文件夹路径，外加一句「文档缺失，帮我补全」, output: 项目里多出的文档文件：README.md、CONTRIBUTING.md、CHANGELOG.md、llms.txt，以及补好注释的源码
- input: 一个 .go 源码文件, output: 同一个文件：每个导出函数和包都加上了规范注释（说明用途、参数、报错情况、可直接复制的用法示例）
- input: 一个已有文档的 Go 项目 + 「帮我看看文档合格吗」, output: 一份审查报告：哪些包没写注释、哪些必备文档缺失、已有文档哪里写错了或不合规范、逐条怎么改
