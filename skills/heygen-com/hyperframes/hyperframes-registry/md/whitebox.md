# hyperframes-registry (`heygen-com/hyperframes/hyperframes-registry`)

## whitebox

- 检索: 用英文描述'想要的动效'跑 hyperframes catalog --query 对整个目录排序, 或 catalog --type/--tag 浏览过滤
- 安装: hyperframes add <name> 联网拉取 item 文件, 默认写入 compositions/<name>.html (block) 或 compositions/components/<name>.html (component), CLI 打印文件清单和待粘贴 snippet
- 接 Block: 在宿主 index.html 写一个 data-composition-src div 引入 block 文件, 补齐 data-composition-id (须与 block 内部 composition ID 一致)、data-start、data-duration、data-track-index、data-width/height
- 接 Component: 把已安装 snippet 文件的 HTML 粘进宿主 composition 标记、CSS 粘进 style 块、JS 粘进 script (时间线代码之前), 若 snippet 暴露 GSAP 时间线集成则把调用加进时间线
- 兜底: 检索结果无一项可用时, 先用 hyperframes feedback --search-miss 上报缺口, 再手写该动效

- 名称解析与依赖序: add 的位置参数先按精确 item 名匹配, 未命中且值是 tag 则安装该 tag 下所有 block; 依赖项先于目标 item 安装; 仅 manifest 有缓存 (24h 刷新窗口, 失联时旧副本仍可服务检索), item 文件每次安装都重新联网拉取——离线可搜索不可安装
- 双层级检索: 默认层按与 item name/title/description 共享词汇本地排序 (不发送任何数据); --on-device 层经一次性 33MB 模型下载后按语义排序; 目录和模型均按英文索引, 非英文 query 无可搜索词直接返回空 (须换英文重写 query 而非报缺口); --json 信封标注哪一层应答, 不可安装项从排名中剔除并计入 dropped
- 接线与配置: block 以子合成方式由宿主时间线调度, data-composition-id 必须匹配 block 内部 ID, data-start/data-track-index 决定出现时机与图层 (值越大越靠前); component 无自身尺寸, 按文件内注释块并入宿主 HTML/style/script; 安装路径与 registry 地址可由 hyperframes.json 配置, CLI 够不到 registry 时可 curl 原始 registry.json 兜底
