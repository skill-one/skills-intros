# wrangler (`cloudflare/skills/wrangler`)

## blackbox

**function**: 帮你把网站或接口部署到 Cloudflare 上线, 并解决部署过程中的报错和配置问题。

- input: 一个项目文件夹 + 一句「帮我部署上线」, output: 一个能直接访问的线上网址 (如 https://my-app.xxx.workers.dev)
- input: 终端里 wrangler 命令报错的那段红字, output: 指出错在哪、给出改好的配置文件或正确的命令, 照做即可跑通
- input: 「我想给项目接一个云端数据库 (KV 存储)」, output: 改好的配置文件 (wrangler.jsonc) + 部署前验证通过的说明
