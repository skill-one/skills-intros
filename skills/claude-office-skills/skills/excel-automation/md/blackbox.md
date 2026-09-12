# excel-automation (`claude-office-skills/skills/excel-automation`)

## blackbox

**function**: 帮你自动操作 Excel:填数据、做图表、合并多个文件、批量生成报表,还能直接控制你电脑上正打开着的 Excel 窗口。

- input: 一个文件夹, 里面躺着几十个格式相同的销售明细 Excel, output: 一个汇总好的 Excel: 每个文件的销售额、销量、均价各占一行, 排好版可以直接发领导
- input: 一段新数据 + 你桌上正开着的 Excel 看板, output: 看板当场刷新: 数据表更新、汇总数字重算、图表重画, 右上角标注更新时间
- input: "帮我把 1 月的数据做成月报, 要带图, 能直接打印", output: 一个排版好的月报 Excel 文件 (含数据表和图表), 顺手再导出一份 PDF 版
- input: "我想要一个 Excel 里没有的函数, 比如自动算增长率", output: 一个自定义函数, 之后你在任意单元格里输入 =GROWTH_RATE(A2:A13) 就能直接用
