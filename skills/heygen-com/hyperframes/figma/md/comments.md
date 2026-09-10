# figma (`heygen-com/hyperframes/figma`)

## comments

- user: 第一次用的新手, category: 坑, comment: 上来就跑命令想看报错提示, 白折腾半天。正确顺序: 先去 figma 设置生成只读 token 存进项目 .env, 再跑命令。token 千万别贴进对话里。
- user: 品牌设计师, category: 妙用, comment: 先跑 tokens 再导组件, 颜色会绑成品牌变量。后来甲方临时换主色, 我改一个值重新渲染整片换肤, 组件一个没重导。
- user: 做宣传视频的前端, category: 注意, comment: 组件导完别急着交付, 先渲染出来和 figma 原图对比, 文字最容易漂。我那次大标题偏了 6px, 一比对就露馅了。
- user: 短视频剪辑师, category: 坑, comment: 我把分镜帧一张张排成轮播, 成品像翻页 PPT。帧是关键帧不是幻灯片: 同一元素跨帧的位置差, 要补间成一段动画。
- user: 小工作室主理人, category: 注意, comment: 品牌变量是企业版专属, 我们小团队跑 tokens 会报 REQUIRES_ENTERPRISE——这不是坏了, 它自动降级读已发布样式, 组件照样能用。
- user: 接外包的独立开发者, category: 启发, comment: 素材全部冻结成本地文件, 渲染不再回源 figma。客户改稿时重跑一次导入只拉变更, 断网也能出片, 版本可控, 交付踏实多了。
