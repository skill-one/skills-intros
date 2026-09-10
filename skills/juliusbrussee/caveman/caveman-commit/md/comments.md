# caveman-commit (`juliusbrussee/caveman/caveman-commit`)

## comments

- user: 第一次用的新手, category: 坑, comment: 以为它会替我执行 git commit,干等了半天。其实它只输出消息文本,复制粘贴到提交框这步得自己做。
- user: 开源仓库维护者, category: 妙用, comment: revert 和安全修复它会自动带上 body 写清原因,不用我提醒。别嫌它啰嗦,这是给半年后排障的人留的。
- user: 外包公司前端, category: 注意, comment: 它默认不加 AI 署名。我们公司要求标注,得在指令里明说加 Assisted-by trailer,否则交上去过不了审查。
- user: 后端老兵, category: 妙用, comment: 把 diff 和一句"为什么改"丢给它,它自己判断该用 fix 还是 feat!,还自动接上 Closes #128,我只做最后把关。
- user: 大三实习生, category: 注意, comment: subject 是英文祈使句还限 50 字符,自己憋很费劲。直接把中文意图和 diff 一起给它压缩,一次就过。
- user: 单人全栈开发, category: 启发, comment: 用了一个月发现:subject 写不进 50 字符,往往说明这次改动本身太大,该拆了。消息反过来逼我改了提交习惯。
