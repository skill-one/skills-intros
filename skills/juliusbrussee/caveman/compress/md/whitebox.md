# compress (`juliusbrussee/caveman/compress`)

## whitebox

- 用户触发: /caveman:compress <filepath> 或说 "compress memory file"
- 定位 SKILL.md 所在目录 (scripts/ 与其同级)
- 执行 cd <目录> && python3 -m scripts <绝对路径>
- CLI 零 token 检测文件类型 → 调 Claude 压缩 → 零 token 校验输出
- 压缩版覆写原文件, 原文备份为 <filename>.original.md, 返回结果

- 压缩规则: 删冠词/填充词/寒暄/hedge/冗余连接词, 允许碎片句; 但代码块、行内代码、URL、文件路径、命令、术语、日期数字、环境变量逐字保留; markdown 标题/列表层级/表格/frontmatter 结构不动
- 校验-修复循环: CLI 校验失败时只做 cherry-pick 定向修复 (非整篇重压), 最多重试 2 次; 仍失败则报错且原文件保持不动
- 依赖与边界: python3 (scripts CLI, 负责检测/校验/备份) + Claude (模型 API, 负责压缩); 只压自然语言文件 (.md/.txt/.typ/.tex/无扩展名), 拒绝 .py/.js/.json/.yaml 等代码文件; 混合内容只压散文部分
