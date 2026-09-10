# gpt-image-2 (`pilioai/skills/gpt-image-2`)

## comments

- user: 电商运营, category: 妙用, comment: 两张图各传一个 --input, prompt 写"把产品放进第二张图的场景里", 合成的场景图直接能上详情页
- user: 前端新手, category: 坑, comment: 加了 resolution 参数想定像素, 结果 HTTP 400; 这模型没有分辨率参数, 只能 --aspect-ratio 控形状
- user: 自媒体博主, category: 注意, comment: 命令先返回任务号, 不直接给图, 要再跑 pnpm dlx @pilio/cli task wait 任务号; 我以为卡死强退白等一场
- user: 后端老兵, category: 注意, comment: key 用 export PILIO_API_KEY 写进环境变量, 别直接拼在命令行里, 会留在 shell 历史, 有泄露风险
- user: 兼职接横幅单的设计生, category: 妙用, comment: --aspect-ratio 是把比例追加进 prompt 引导构图, 不是硬裁; 我做 21:9 横幅时四周多留了安全区
- user: 爱省钱的独立开发者, category: 妙用, comment: pilio.ai 网页版是同一套流程, 我先在网页试 prompt 效果, 满意再回命令行批量生成, 少烧额度
