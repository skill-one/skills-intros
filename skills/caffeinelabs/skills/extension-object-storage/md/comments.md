# extension-object-storage (`caffeinelabs/skills/extension-object-storage`)

## comments

- user: 第一次用的新手, category: 坑, comment: 只装了前端 npm 包、没装 mops 包,上传全部 403,我以为是自己代码写错查了一下午。两个包必须同时装,重新部署才生效。
- user: 前端开发者, category: 坑, comment: 拿 getDirectURL() 返回的网址判断是不是图片,结果那是无后缀的代理地址,全部判断失败走了 fallback。要用记录里的 filename 正则判断。
- user: 后端老兵, category: 注意, comment: _immutableObjectStorage 开头的方法是平台保留名,我手写了一份想自己控制,返回类型不对照样 403。删掉,用官方 Mixin 就通了。
- user: 从 S3 迁来的老程序员, category: 妙用, comment: 原以为要像 S3 那样折腾预签名 URL 和 CORS,结果 fromBytes 一步到位,一个下午就把相册上传跑通,上传进度条还白送。
- user: 做相册 side project 的学生, category: 注意, comment: 文件字段一开始用 Text 存 id,上传代理直接不干活。凡代表文件的字段和参数都得是 Storage.ExternalBlob,别用 Text,这是硬要求。
- user: 独立开发者, category: 启发, comment: 文件实际在链下、链上只存引用,列表页只查元数据,几百条记录秒开。以后设计数据表我也会把大对象和索引记录分开存。
