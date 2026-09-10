# contribute-catalog (`heygen-com/hyperframes/contribute-catalog`)

## comments

- user: 第一次投稿开源的新手, category: 坑, comment: 我把字幕用 tl.from(opacity:0) 配 tl.set(opacity:1) 放同一时刻，from 会盖掉 set，字幕整段不显示。换成 tl.to 就正常了。
- user: 前端工程师, category: 坑, comment: 手滑用了 Math.random()，每次渲染粒子位置都不一样，回看也对不上帧。按模板换 mulberry32 固定随机种子，渲染才可复现。
- user: 短视频工作室剪辑师, category: 妙用, comment: 调字幕节奏我从不整片渲染，用 snapshot --at "1.0,3.0,5.0" 抽关键帧看，几秒一轮，时机定稿才 render 出片，返工少一半。
- user: 海外远程的自由开发者, category: 注意, comment: 外部贡献者不用碰 AWS 传图脚本，那是 HeyGen 内部流程。把 preview.mp4 附进 PR 描述即可，目录图维护者合并前会补。
- user: 后端老兵被拉来做视频, category: 注意, comment: 我跳过了 generate-catalog-pages.ts，PR 能开但文档页缺失，被打回重补。Ship 八步一条别省，且 lint、validate 都要跑到 0 错误。
- user: 会改 HTML 的自媒体博主, category: 启发, comment: 原以为投稿得从零写项目，其实按 scaffold 复制模板改文案和参数，一下午就提了第一个字幕样式。改现成的比从零写顺得多。
