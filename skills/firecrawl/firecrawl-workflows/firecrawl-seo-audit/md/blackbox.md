# firecrawl-seo-audit (`firecrawl/firecrawl-workflows/firecrawl-seo-audit`)

## blackbox

**function**: 给你的网站做一次「搜索排名体检」: 找出影响它在搜索引擎 (如 Google/百度) 中排名的问题, 并给出按轻重缓急排好序的改进清单。

- input: 一个网站网址, 如 https://example.com, output: 一份完整的 SEO 体检报告: 每个页面标题和描述写得好不好、结构是否清晰、有哪些死链和缺漏, 以及先修哪个、后修哪个
- input: 网站网址 + 几个你想被搜到的词, 如「SEO工具、网站抓取」, output: 关键词机会分析: 哪些词值得去做、你的网站缺哪些对应页面、内容差在哪
- input: 你的网址 + 竞争对手的网址, output: 对比报告: 对手的页面为什么排在前面, 你需要补什么才能追上
