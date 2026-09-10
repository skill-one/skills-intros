# wind-find-finance-skill (`wind-alice/alicemarket/wind-find-finance-skill`)

## blackbox

**function**: 你是金融任务的"导购台"：说出你的金融需求（查行情、估值、选股、复盘、回测等），我判断该用哪个专业能力，缺的当场帮你装好，然后任务由装好的能力直接完成。

- input: 「今天A股市场主线是什么？」, output: 先问你「要不要装对应的主线分析能力、装到当前还是全部agent」，你点头后自动装好，紧接着当日市场主线分析直接出炉
- input: 「帮我给小米做个DCF估值」, output: 识别出需要估值工具和数据底座 → 征求安装范围确认 → 确认后自动安装 → 小米的DCF估值结果直接交到你手上
- input: 「查一下贵州茅台近5年的营收」, output: 匹配到金融数据查询能力，装好后由它直接返回茅台历年营收数据
