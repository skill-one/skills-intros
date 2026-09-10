# firecrawl-website-design-clone (`firecrawl/firecrawl-workflows/firecrawl-website-design-clone`)

## whitebox

- 从上下文推断源 URL、目标技术栈和是否要实现；用户给了 URL 且要设计系统就直接开工，只有被阻塞时才问 1~3 个问题。
- 对同一 URL 并行发起两次 Firecrawl 抓取：一次 `branding,images` 合并格式出结构化 JSON，一次全页截图，产物统一落到 `.firecrawl/`。
- 从 branding 块提取颜色/字体/间距/组件/品牌资产等设计 token，以 images 列表为页面内容图（hero、产品图、插图）的唯一事实来源，以截图为布局与视觉层级的参照。
- 按固定模板把证据合成为 DESIGN.md：截图嵌入文件顶部，后接 Design Tokens、Components、Page Patterns、Content Style、Agent Build Instructions；无法实测的值标注为 inferred 并给近似值。
- 若用户要求实现，先产出/更新 DESIGN.md，再以它为唯一事实来源驱动编码构建。

- 并行双抓取：`firecrawl scrape --format branding,images` 与 `--full-page-screenshot` 用 `&`+`wait` 同时执行；branding+images 必须合并在一次调用（只花一个 credit），用于弥补 branding 块只含 logo/favicon/ogImage/logoHref、缺少内容图的盲区。外部依赖：Firecrawl 托管 API（经 CLI 调用），需 FIRECRAWL_API_KEY。
- 截图落地校验：若截图抓取返回远程签名 URL 而非本地文件，则下载到同一 `.firecrawl/` 路径，保证 DESIGN.md 引用的是稳定本地资源。
- 证据分层 + 按需补抓：markdown/metadata/links 仅在需要推断标题层级、CTA、导航、页面用途时使用，HTML 只在 branding+images+截图不足以推断类名、字体名、CSS 变量时才追加；默认单页出第一版防过度抓取，多页站点可拆给并行子代理（按页或按颜色/字体/间距/组件分工）。
