# writing-for-agents (`mattpocock/skills/writing-for-agents`)

## whitebox

- 判定文档类型与分支: 确认产出对象 (skill / AGENTS.md / 指针指向的文档); 若是 skill, 先读取同级 SKILL-MECHANICS.md 获取 frontmatter 与调用方式。
- 信息分级: 把每块内容放上三级信息层级 (in-file 步骤 → in-file 参考 → 指针后的披露参考), 用『分支是否触达』决定内联还是下沉。
- 写步骤与完成标准: 每步以可检验且高要求的 completion criterion (完成判据) 收口, 抵抗提前完成。
- 重构: 用模型预训练已有的引导词 折叠多处重复表述; 仅当拆分真能省下一种负载时才切分文档。
- 修剪: 逐句三查——duplication (重复)、no-op (对默认行为无改变的指令)、失去 relevance (相关性) 的行——收敛到单一事实来源。

- Context pointer (上下文指针) 即路由: agent 是否触达材料由指针措辞决定, 与目标本身无关——引导词前置、每个分支只留一个触发词、删去正文已含的身份描述; 指针的每个词都常驻上下文按 token 计价。
- 双负载预算: context load (常驻窗口的 token/注意力开销) 与 cognitive load (人类『何时看哪份文档』的开销) 是两本独立账; 内联、下沉、拆分的每个决定都在花其中一本——没有第三个选项可白拿。
- 校验不靠外部工具, 靠判据与自查: completion criterion 要求可检验+穷尽; pruning 用 no-op 测试 (『相对模型默认行为是否改变』) 逐句过滤, 否定句会让被禁内容更醒目, 一律改写成正向目标。无外部工具/库/模型 API 调用, 唯一外部依赖是本地文件 SKILL-MECHANICS.md, 仅当产出物是 skill 时按指针读取。
