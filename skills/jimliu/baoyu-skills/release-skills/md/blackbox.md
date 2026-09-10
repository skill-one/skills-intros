# release-skills (`jimliu/baoyu-skills/release-skills`)

## blackbox

**function**: 一句话: 你说「发布」, 它就把项目的新版本整套发出去 — 升版本号、写多语言更新日志、打标签、发 GitHub Release, 全程只需你确认一次。

- input: 在项目目录里说「发布新版本」, output: 版本号自动升级 (如 1.2.3 → 1.3.0), 中/英/日等更新日志写好并插入文件, 生成规范的提交和标签, 推送到远程并创建对应的 GitHub Release 页面
- input: 输入 --dry-run (预演), output: 一份不改动任何文件的预览报告: 检测到的项目类型和当前版本、建议的新版本号、将要生成的提交列表和中/英更新日志草稿
- input: 输入 --backfill-releases (回填), output: 为历史上只打了标签、却没有 GitHub Release 的旧版本, 逐个补齐创建 Release 页面, 说明文字从更新日志中对应版本段落提取
