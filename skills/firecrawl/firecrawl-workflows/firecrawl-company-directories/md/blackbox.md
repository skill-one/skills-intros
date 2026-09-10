# firecrawl-company-directories (`firecrawl/firecrawl-workflows/firecrawl-company-directories`)

## blackbox

**function**: 把各种公司名录网站上的企业列表, 整理成一份干净、可直接使用的名单 (表格或文件)。

- input: 一个 YC 孵化器公司目录的网址 (如 YC W24 批次页面), output: 一份 JSON/CSV 文件, 含每家公司的名称、简介、行业、地点、官网链接等字段
- input: G2 上某个软件分类页面的链接 + 条件「只要美国公司, 前 50 家」, output: 一个表格: 50 家公司, 列出去重后的名称、描述、类别和官网, 按条件筛选好
- input: 一个自定义的公司目录网址 + 要求「导出成 CSV, 方便导入 CRM」, output: 一份 CRM 可直接导入的 CSV 文件, 外加一段简短说明: 抓了哪家网站、共多少家、有哪些字段拿不到
