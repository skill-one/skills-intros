# compress (`juliusbrussee/caveman/compress`)

## blackbox

**function**: 把 .md/.txt 等纯文字文件压成短句版:意思不变、字数大减(省 token),原文自动留底,代码和链接一字不动。

- input: 一个写满长句的 CLAUDE.md 文件路径,如 ~/project/CLAUDE.md, output: 同一文件被覆盖为短句压缩版(如「请务必记得在提交前先运行完整测试」→「commit 前先跑测试」),原文自动备份成 CLAUDE.original.md
- input: 一份含代码块和命令的笔记 preferences.md, output: 同路径下的压缩版笔记:文字说明全部缩短,但 ``` 里的代码、`npm install` 这类命令、URL、日期一个字符都没变
- input: 一个代码文件路径,如 app.py 或 config.json, output: 拒绝处理并告知原因,原文件完好无损——只碰文字文件,不碰代码/配置文件
