# baoyu-image-gen (`jimliu/baoyu-skills/baoyu-image-gen`)

## comments

- user: 第一次用的新手, category: 坑, comment: 我把 ChatGPT 登录凭证当成 OPENAI_API_KEY 填进去一直报错。两者不通用：要么用正规 API key，要么装 codex 后用 --provider codex-cli 走订阅。
- user: 常接头像单的插画师, category: 妙用, comment: 给客户照片换场景时，prompt 别写长外貌描述，一句「保持参考图人物身份不变，只改场景服装光线」就够。写越长，模型越容易重画一个相似的新人。
- user: 日更的自媒体运营, category: 妙用, comment: 十几篇文章配图，我先把每张图的 prompt 存成文件，用 build-batch 脚本拼成 batch.json，再 --jobs 4 批量跑，挂机等结果，比一张张点省一晚上。
- user: 精打细算的接单画手, category: 注意, comment: 默认 2k 又慢又费额度。快速试构图时加 --quality normal 出 1K 快图，定稿后再跑 2k，一套图下来省不少时间。
- user: 踩过坑的产品经理, category: 坑, comment: 我拿上一步生成的图当参考图继续改，三四轮后人物完全走样。参考图要用原始素材挑 2-4 张，生成图会越滚越偏。
- user: 运维老哥, category: 注意, comment: 带 --ref 前先确认型号：即梦、Seedream 3.0 不支持参考图会直接报错，Replicate 只能 --n 1。别等跑完才发现白等。
