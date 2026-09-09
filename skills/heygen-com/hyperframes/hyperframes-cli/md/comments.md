# hyperframes-cli (`heygen-com/hyperframes/hyperframes-cli`)

## comments

- user: 第一次用的新手, category: 坑, comment: 用中文搜目录「标题一行行出现」返回空，差点以为没这功能。索引是英文的，报错 No searchable words in query 就是这意思，换英文描述立刻命中。
- user: 前端独立开发者, category: 妙用, comment: 普通搜索只认字面，换个说法就搜不到。加 --on-device 按语义排，首次下 33MB 后全程离线。搜不到就回填它打印的 feedback 行，填 --wanted 提交，别硬猜组件名。
- user: 运维老哥, category: 坑, comment: 把 doctor --json 直接当 CI 门禁会假绿——它无论什么都退出 0，必须接 `| jq -e '.ok'` 看返回体。另外 validate/inspect 是废弃别名，新脚本一律写 check。
- user: 自由职业剪辑师, category: 妙用, comment: 给 30 家门店出同款片、只换店名电话：变量写进 rows.json，`render --batch rows.json --output "renders/{name}.mp4"` 一条命令挂机跑完，省一个通宵。
- user: 广告公司项目负责人, category: 启发, comment: storyboard 草稿板通过不算批准，check 全绿也要停在最终预览等人点头。起初嫌这步烦，后来每次暂停都能挑出要改的镜头，强制审批反而最省返工。
- user: 动效外包接单的, category: 坑, comment: 挂了子场景的项目 check 全绿，渲出来一幕空白小块——静态检查抓不到挂载失败。现在每个挂载点都 `snapshot --at t1,t2,t3` 截中点帧，没样式的小块就是挂坏了。
