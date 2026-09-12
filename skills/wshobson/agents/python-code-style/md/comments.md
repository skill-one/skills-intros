# python-code-style (`wshobson/agents/python-code-style`)

## comments

- user: 后端老兵, category: 妙用, comment: 配好 pyproject.toml 后, 我把 pre-commit 里 flake8、isort、black 三个钩子删成一个 ruff, CI 时间直接砍半, 再也没为工具链吵架。
- user: 接手祖传代码的人, category: 坑, comment: 老项目直接开 mypy strict → 报错上千条没法下手。后来按指南先给 tests 目录加 override 放宽, 业务代码再逐步收紧, 一周就清完了。
- user: 第一次配工具的新手, category: 注意, comment: target-version 别照抄 py312, 要改成项目实际跑的版本。我抄了默认值, 服务器是 3.9, 自动修复引入新语法, 上线就报错。
- user: 写脚本的数据分析, category: 妙用, comment: 写完脚本跑一次 ruff format, 长链条调用自动折行、超长报错文案自动拆好, 我再也不手动对齐换行了。
- user: 团队 Tech Lead, category: 启发, comment: ruff 进 CI 后, 评审再没吵过格式, 大家只聊逻辑。风格规则交给工具, 是我今年做过的最划算的团队约定。
- user: 开源维护者, category: 注意, comment: docstring 里 >>> 示例别写理想化代码, 用户真会照着跑。我改函数签名忘了同步示例, 连收三个 issue 才长记性。
