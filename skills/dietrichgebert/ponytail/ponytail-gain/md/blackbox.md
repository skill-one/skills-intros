# ponytail-gain (`dietrichgebert/ponytail/ponytail-gain`)

## blackbox

**function**: 输入一条指令或一句提问, 立刻展示一张 ponytail 效果记分卡: 用条形图对比「不用它 vs 用它」的代码量、成本、速度 (基准测试中位数), 纯展示, 不改动任何东西。

- input: 输入命令: /ponytail-gain, output: 一张 ASCII 条形图记分卡: 代码量只剩 6–20% (省 80–94%)、成本只剩 23–53% (省 47–77%)、速度快 3–6×
- input: 输入一句自然语言: "what does ponytail save" (ponytail 能省什么), output: 同一张对比记分卡, 附「这是基准测试中位数、非当前项目实测」的说明
- input: 输入: "show ponytail impact" (展示 ponytail 的影响), output: 记分卡 + 两个后续入口: /ponytail-debt (看欠下的捷径账本) 和 /ponytail-audit (看还有什么可砍)
