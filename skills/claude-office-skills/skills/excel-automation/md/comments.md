# excel-automation (`claude-office-skills/skills/excel-automation`)

## comments

- user: 维护十年老 VBA 宏的会计, category: 妙用, comment: 旧宏一行没重写：Python 里 wb.macro('月结宏')(参数) 直接调用，还能拿返回值继续算。老宏当零件，新逻辑用 Python 拼。
- user: 第一次接自动化需求的新手, category: 坑, comment: 我在没装 Office 的云服务器上跑，直接报错起不来——它控制的是真实 Excel，没装就用不了。服务器场景得换纯读写文件的库。
- user: 常爬两万行数据的分析师, category: 坑, comment: 逐格写 A1、A2……跑二十分钟像死机。改成把整个二维数组一次赋给区域，十秒完。大数据量千万别逐格写。
- user: 帮同事装环境的 IT 支持, category: 注意, comment: 部署后总有人电脑挂着十几个隐形 EXCEL.EXE，文件被锁删不掉。脚本要用 try/finally 包住，结尾必做 wb.close() 和 app.quit()。
- user: 每月批量出报表的财务专员, category: 注意, comment: 我忘了关弹窗，脚本半夜卡在「文件已存在，是否覆盖？」等确认。先设 display_alerts=False 再跑批，才不会停在一个对话框上。
- user: 团队里唯一会 Python 的, category: 妙用, comment: 把增长率算法写成 @xw.func 函数装进加载项，同事在单元格直接 =GROWTH_RATE(A2:A12)。没人要懂 Python，我成了全组的插件供应商。
