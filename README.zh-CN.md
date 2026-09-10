# skills-profiles

为 [skill-one/skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror) 收录的
[agent skills](https://www.skills.sh) 生成的多角度中文档案：一个可查询的索引
（`skills.jsonl`，带每个 skill 的分类与职业画像），加上每个 skill 完整的八份文字档案
（`skills/`），以及为已经渲染出配图的那些 skill 准备的封面配图。档案由 LLM 基于每个 skill 的
`SKILL.md` 生成，并按整体快照发布——快照自包含，读到什么就是什么，不需要别的东西。

English: [README.md](README.md) · 开发指南（生产 / 扩展这份数据）：[DEVELOPING.zh-CN.md](DEVELOPING.zh-CN.md)

## 数据是什么

```
├── skills.jsonl   每个已生成档案的 skill 一行，按 id 排序——筛选 / 关联 / 排行都从这里开始
├── stats.json     生成进度：每个 prompt 的覆盖数、已完成/剩余/过期
└── skills/        每个 skill 一个目录，目录名就是它的 id
    └── vercel-labs/skills/find-skills/   ({owner}/{repo}/{slug})
        ├── domain.json  scenario.json  blackbox.json  whitebox.json
        ├── tagline.json persona.json   comments.json  cover.json
        ├── cover.png    渲染出的配图（只有已经画过的 skill 才有）
        └── md/          同样八份内容的 markdown 版，方便阅读
```

`skills.jsonl` 的一行（真实数据）：

```json
{
  "id": "vercel-labs/skills/find-skills",
  "hash": "b146008599c31057cef1c145774cea5d5afb30e8f43fa802e47a4b461419aaaf",
  "domain": {
    "domain": "开发编程",
    "reason": "面向开发者的技能包检索与安装工具, 属于 agent 开发工具链生态"
  },
  "persona": {
    "tool": "npx skills",
    "role": "技能猎头",
    "scene": "你说「这活你不会吧」时,我出门找一个现成的技能装上"
  }
}
```

| 字段      | 含义                                                                 |
| --------- | -------------------------------------------------------------------- |
| `id`      | skills.sh 的 skill id，`{owner}/{repo}/{slug}`——与镜像的 id 完全一致 |
| `hash`    | 上游记录的技能文件 SHA-256：档案描述的就是这一份内容                 |
| `domain`  | `domain`：13 个固定使用场景分类之一；`reason`：一句话理由            |
| `persona` | 把 skill 当一个职业——`tool` 趁手工具、`role` 角色、`scene` 高频场景  |

`domain.domain` 是闭合枚举，可以直接筛：开发编程 · 测试与质量 · 数据分析 · 运维与安全 · 办公效率 ·
内容创作 · 设计多媒体 · 知识管理 · 商业运营 · 支付金融 · 教育学习 · 生活服务 · 其他。

索引只折入你真正会拿去筛选的两个角度，其余六个都是每个 skill 目录下的文件，各有各的结构——八个角度合计：

| Prompt     | 结构                                     | 内容                                                        |
| ---------- | ---------------------------------------- | ----------------------------------------------------------- |
| `domain`   | `{domain, reason}`                       | 分类 + 理由——同时进索引                                     |
| `persona`  | `{tool, role, scene}`                    | 职业画像——同时进索引                                        |
| `scenario` | `{text}`                                 | 一段 100 字以内的场景化介绍，从用户痛点切入                 |
| `tagline`  | `{taglines[3]}`                          | 3 条宣传短标语，每条 20 字以内                              |
| `blackbox` | `{function, input_output[3–5]}`          | 黑盒视角：你给什么 → 你得到什么，不谈内部实现               |
| `whitebox` | `{execution_flow[3–5], mechanisms[2–3]}` | 白盒视角：主路径流程、关键机制、真实依赖                    |
| `comments` | `{comments[4–6]}`                        | 用户第一人称评论；`category` 通常为 妙用 / 坑 / 注意 / 启发 |
| `cover`    | `{text}`                                 | 配图配方：一段英文文生图提示词，只描述画面主体               |

`{...[n–m]}` 表示长度为 n~m 的数组；`input_output` 的元素是 `{input, output}`，`comments` 的元素是
`{user, category, comment}`。一份 `comments.json` 的节选：

```json
{
  "comments": [
    {
      "user": "后端老兵",
      "category": "妙用",
      "comment": "用 --owner 锁定官方源: npx skills find react --owner vercel-labs, 结果只剩 Vercel 家的, 不会被野包污染。"
    },
    {
      "user": "团队技术负责人",
      "category": "坑",
      "comment": "只看搜索第一页就装, 换来个 80 安装量的弃坑包, 出问题没人管。现在先看安装量和 GitHub stars, 低于 100 的直接 pass。"
    }
  ]
}
```

每个已发布的 skill 八个角度都是齐的；`stats.json` 再告诉你有多少个 skill、以及这些档案是基于哪一版
数据生成的：

```json
{
  "covers": { "rendered": 0 },
  "prompts": {
    "blackbox": 334,
    "comments": 334,
    "cover": 334,
    "domain": 334,
    "persona": 334,
    "scenario": 334,
    "tagline": 334,
    "whitebox": 334
  },
  "skills": { "complete": 334, "remaining": 8625, "stale": 0, "total": 8959 },
  "snapshot": { "ref": "dist-2026-09-09", "fetched_at": "2026-09-09T02:01:24Z" }
}
```

`prompts.cover` 数的是档案生成器写下的配图*配方*数；`covers.rendered` 数的是据这些配方真正画出来的配图数。
两者分开计数，是因为配图是一个独立的产物、实测一张约 1.7 MB（1024x1024），且只为已经渲染过的 skill 存在
——把 `cover.png` 当作每个
skill 上「有则有、无则无」的东西来对待，缺失时不做任何兜底。

`skills.total` 是上游快照的规模，`skills.complete` 是已经生成档案的部分，剩下的都在队列里。
`snapshot.ref` 指出这些 hash 属于镜像的哪个 tag（见[与镜像数据关联](#与镜像数据关联)）。这些计数在每轮
`generate` 发布结束时重写，因此只做丢弃的 `sync` 发布之后，它可能略高于树上的实际数量；要精确计数时，
以 `skills.jsonl` 的行数为准。

两条由结构本身保证的性质：

- 索引是每个 skill 目录的投影，每次重写都从磁盘重新推导：行存在当且仅当目录存在，
  行里的 `domain` / `persona` 不可能与磁盘上的 json 不一致。
- `hash` 就是生成档案时依据的那份内容。上游改写某个 skill 后，它的档案会被丢弃而不是继续描述
  另一个版本——已发布的每一行都说得清自己讲的是哪一版。

`*.json` 是给程序读的形式，也是缓存标记；`md/*.md` 是同一份内容的排版版。除 id、路径和字段名外，
全部是中文。

### 配图

`cover.json` 只装一样东西：一段英文文生图提示词，说清**画什么**，由 skill 的职业画像推导而来——
谁在干活、拿着什么、在用户需要他的那个场景里。这段配方会被校验（纯英文、逗号分隔短语），所以写成中文文案的回答会被重试，而不是被照着画出来。**画风**并不在其中：配图渲染时用的是该 skill `domain`
分类所对应的风格，13 个分类各有一套固定风格，于是同一分类的配图像一个家族，画风也不会随措辞漂移。
每张配图都是**一个正在干活的人**：这个取景规则是渲染器里的常量，不是对模型的请求，所以哪怕配方写得很单薄，
出来的也是人物肖像，而不是一堆道具的静物画。配方与配图分开存放（`md/cover.md` 展示配方，`cover.png` 是成品），
而重画一张配图不花任何 LLM 调用。

## 如何获取数据

发布在 [`dist` 分支](../../tree/dist)上——分支根目录**就是**档案快照，因此每个 commit 都是一个完整
状态，同一棵树也可以在网页上直接浏览。覆盖率随每次发布增长（要精确数字就数 `skills.jsonl` 的行数），
文字档案本身压缩后不到 1 MB；渲染出的配图不计入这个数字，因为单张约 1.7 MB、且只有已经渲染过的
skill 才有。可以按需拉单个文件，也能整包克隆。注意 `dist` 还附带一个内部
`cache/skills-sh/` 数据集镜像（上游的 `SKILL.md`），供 CI 恢复、让 `generate` 不必再回上游拉取——
它不属于档案 API，但整包克隆/下载 tarball 会把它一起带上（约 120 MB 文本）。按路径取单个文件不受影响。

### 拉取单个文件

不用克隆、不用鉴权。先从索引挑 id，再按路径取任意一个角度：

```bash
curl -sO https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills.jsonl

# dist/skills/<id>/<prompt>.json —— 想在终端里读就用 md/<prompt>.md
curl -s https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills/vercel-labs/skills/find-skills/md/persona.md
```

索引很小（按当前覆盖率约 130 KB），整份拉下来很便宜。GitHub 对这些地址有约 5 分钟缓存，
所以 `dist` 的 URL 始终跟着最新发布。

筛选只要 jq 就够——取出所有「设计多媒体」类的 skill 及其职业角色：

```bash
curl -s https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills.jsonl |
  jq -r 'select(.domain.domain == "设计多媒体") | [.id, .persona.role] | @tsv'
```

### 克隆整个快照

```bash
git clone --depth 1 -b dist https://github.com/skill-one/skills-profiles.git

# 或者一个请求拿完，不带 git 历史：
curl -sL https://codeload.github.com/skill-one/skills-profiles/tar.gz/refs/heads/dist |
  tar -xz --strip-components=1
```

### 钉住某个快照

每次发布都会打 tag，而 tag 是不可变的——钉住一个，你看到的内容就不会在脚下变化：
`dist-YYYY-MM-DD` 是某一天的数据集基准（`sync` 写入，同日内的发布 force 覆盖），
`dist-YYYY-MM-DD-N` 是这个基准之上的第 N 批档案（`generate` 写入）。历史按滚动时间窗剪枝
（默认一个月）。

```bash
# 最新的已发布 tag
latest=$(git ls-remote --tags --refs https://github.com/skill-one/skills-profiles.git 'refs/tags/dist-*' \
         | awk -F/ '{print $NF}' | sort -Vr | head -1)
curl -sO "https://raw.githubusercontent.com/skill-one/skills-profiles/$latest/skills.jsonl"
git clone --depth 1 -b "$latest" https://github.com/skill-one/skills-profiles.git
```

按 tag 缓存、只在出现更新的 tag 时才重新拉取——tag 的内容永不变，这是既贴近最新、又不必每轮
重下的省钱取法。

### 与镜像数据关联

安装量、stars、简介以及 `SKILL.md` 原文都刻意没有在这里重复——它们在
[skills-sh-mirror](https://github.com/skill-one/skills-sh-mirror) 里，而这份数据正是基于它的
数据集生成的。两边的键相同：用 `id` 关联行，用 `hash` 确认内容一致。如果也要按 hash 对齐，
就把上游钉到 `stats.json` 里的 `snapshot.ref`——对着随时在变的 `dist` 分支，总会有几个 hash 已经漂走：

```bash
curl -sO https://raw.githubusercontent.com/skill-one/skills-profiles/dist/stats.json
up=$(jq -r .snapshot.ref stats.json)   # 例如 dist-2026-09-09
curl -s "https://raw.githubusercontent.com/skill-one/skills-sh-mirror/$up/skills.jsonl" -o up.jsonl
curl -s https://raw.githubusercontent.com/skill-one/skills-profiles/dist/skills.jsonl -o mine.jsonl

# id  installs  category  role
jq -r --slurpfile up up.jsonl '($up | map({(.id): .installs}) | add) as $i
  | [.id, $i[.id], .domain.domain, .persona.role] | @tsv' mine.jsonl
```

同一个 `id` 还能定位到它的 skills.sh 页面（`https://www.skills.sh/<id>`），
以及镜像里对应的上游文件。

档案由本仓库的 `sync` 与 `generate` 两条工作流生成（GitHub Actions 手动触发：
`gh workflow run generate.yml -f limit=50`）。想自己跑通整条流水线、新增一个角度或重算某个 skill：
[DEVELOPING.zh-CN.md](DEVELOPING.zh-CN.md)。
