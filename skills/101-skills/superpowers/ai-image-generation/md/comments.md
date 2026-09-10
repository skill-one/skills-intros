# ai-image-generation (`101-skills/superpowers/ai-image-generation`)

## comments

- user: 电商美工, category: 妙用, comment: 商品换背景别重画,用 GPT-Image-2 编辑模式:原图链接放 images,prompt 只写「换成沙滩日落背景」,主体能保住,省了抠图。
- user: 第一次用的新手, category: 坑, comment: 上来就跑生成命令,报 belt 不是命令才想起要先装 CLI 再 belt login。先装再登录,一分钟的事,别像我瞎折腾半天。
- user: 新媒体运营, category: 注意, comment: 图里要带文字的别默认用 FLUX,小字会糊成乱码。要海报选 Reve,只要标题大字选 Seedream 3.0,基本一次过。
- user: 独立开发者, category: 妙用, comment: 我先用 Klein 4B(约 $0.0001/张)快速试构图和 prompt,定稿再换 Seedream 4.5 出 4K,试错成本几乎为零。
- user: 老设计师, category: 启发, comment: 以前一把梭一个大 prompt 赌运气,现在拆成生成 → GPT-Image-2 局部改 → Topaz 放大三步,每步可控,废片少多了。
- user: 运维老哥, category: 注意, comment: Topaz 放大吃的是 image_url,要公网链接,我丢本地路径直接失败。先传图床再调用,别踩我这坑。
