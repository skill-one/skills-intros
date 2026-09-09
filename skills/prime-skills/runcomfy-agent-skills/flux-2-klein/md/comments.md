# flux-2-klein (`prime-skills/runcomfy-agent-skills/flux-2-klein`)

## comments

- user: 第一次用的新手, category: 坑, comment: 没先 runcomfy login 就跑, 报退出码 77, 查了半天发现是没登录. 另外 width 写 4096 会直接 422, 分辨率上限约 2K.
- user: 电商美工, category: 妙用, comment: 把过审那版的 prompt 存成模板, 同事出图只换主体和场景词, 全店风格终于是一套的了, 以前十个人十个样.
- user: 独立游戏开发者, category: 坑, comment: 以为 steps 拉到 50 更精细, 结果和 25 步看不出差别还慢一倍. 后来固定草稿用 4B 四步, 定稿 9B 二十五步.
- user: 自媒体运营, category: 坑, comment: 图里多行文案必糊, 只留一句主标语, 再加 crisp typography、步数拉到 25 才清楚; 长文案我换 GPT Image 2.
- user: 设计系学生, category: 启发, comment: 用惯了「主体+动作+场景+风格+光+镜头」的顺序, 现在给摄影组提需求也这么列条目, 对方再没反问我「到底想要啥」.
- user: 后端老兵, category: 注意, comment: CI 里别走设备码登录, 直接设 RUNCOMFY_TOKEN. 退出码 75 是限流超时可重试, 77 是没登录, 别当服务故障误报警.
