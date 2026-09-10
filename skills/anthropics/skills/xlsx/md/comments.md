# xlsx (`anthropics/skills/xlsx`)

## comments

- user: 财务建模老手, category: 启发, comment: 看它把每个假设都放进独立单元格、公式只引用不写死,才意识到我手工表里藏了多少硬编码数字。现在换场景改一个格子,全表跟着重算。
- user: 第一次用的新手, category: 坑, comment: 公式刚写完打开显示空值,吓我一跳——写完必须先重算一次才有缓存值。现在没看到它跑重算并报 0 错误,我不收货。
- user: 运维老哥, category: 坑, comment: 让它改带宏的 .xlsm 没说保留,宏全丢了,按钮失灵。第二次开口先讲一句"保留宏",再没翻车。
- user: 接手部门模板的会计, category: 注意, comment: 改部门现成模板要明确说"照原格式,只改指定格子"。没说的那次它重新排版还加了说明,好看但同事不认账。
- user: 数据分析师, category: 妙用, comment: 接手陌生 xlsx 先让它转 markdown 预览,按 sheet 列出内容,不开 Excel 就知道每张表是干嘛的,再精准指派它在哪张动手。
- user: 被百分比坑过的运营, category: 注意, comment: 百分比要用小数存:说 15% 它存 0.15 显示正常;我随口让它填 15,交付出去全表 1500%,被截图吐槽。
