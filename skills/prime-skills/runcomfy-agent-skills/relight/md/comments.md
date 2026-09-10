# relight (`prime-skills/runcomfy-agent-skills/relight`)

## comments

- user: 电商美工, category: 妙用, comment: 整批 SKU 白底图换窗光场景,把同一段打光 prompt 原样套进 Nano Banana 2 的 image_urls 数组一次跑完,几十张图光影完全一致,比逐张调快太多。
- user: 第一次用的新手, category: 坑, comment: 没 login 就直接跑,报退出码 77 才知道是没登录。先 runcomfy login 或设好 RUNCOMFY_TOKEN,别像我一样对着报错查半天。
- user: 人像摄影师, category: 注意, comment: 只写"灯光调好看点"模型会乱飘。要写死三样:色温、方向、强度,如"3200K 主光左45°",末尾补一句"保留姿态构图",出图才稳。
- user: 短视频剪辑师, category: 注意, comment: 以为是图和视频都能调光,实测 CLI 只收静图。要给视频重光得去 ComfyUI 工作流找 IC-Light,别在这里白等它支持。
- user: 自动化脚本开发, category: 注意, comment: CI 里按退出码分情况:75 是超时或限流,sleep 几秒重试就好;77 才是要查 token。配好 RUNCOMFY_TOKEN,批量任务能无人值守跑完。
- user: 修图老手, category: 启发, comment: 客户甩来"要这张的光感",我直接用 GPT Image 2 填两张图:原片加参考图,让它对齐方向、色温、对比度,省掉手动拉曲线的半小时。
