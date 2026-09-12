# tavily-extract (`tavily-ai/skills/tavily-extract`)

## comments

- user: 内容运营 / 天天搬资料的, category: 妙用, comment: 抓超长文档时我加 --query "定价" --chunks-per-source 3,只返回相关段落,直接喂给 AI 总结,不用再手动删无关内容。
- user: 第一次用的新手, category: 坑, comment: 我一次塞了 30 个链接,超出 20 个上限的那部分直接没结果。分成两批跑才拿全,别贪一次搞定。
- user: 前端开发, category: 坑, comment: extract 一个单页应用,内容缺一半但 exit code 是 0,我以为成功了就交差。记得翻 failed_results,失败的 URL 加 --extract-depth advanced 重跑。
- user: 运维老哥, category: 注意, comment: 免登录额度用完会要求 tvly login,要弹浏览器。服务器上的定时任务走不了这步,提前登录好,不然脚本半夜静默失败。
- user: 研究生 / 文献整理党, category: 妙用, comment: 清理收藏夹,50 篇旧文章分 3 批 extract,用 -o 存成 json 再转 markdown 进笔记库,比一篇篇复制粘贴省了一下午。
- user: 写 AI 应用的开发者, category: 启发, comment: 以前抓网页要自己写去广告、去导航的清洗规则,现在直接喂 extract 出的 markdown 给模型,清洗那步整个删掉了。若搜索结果自带原文够用,连这步都能省。
