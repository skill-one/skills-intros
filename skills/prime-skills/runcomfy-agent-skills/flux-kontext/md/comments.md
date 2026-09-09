# flux-kontext (`prime-skills/runcomfy-agent-skills/flux-kontext`)

## comments

- user: 电商美工, category: 妙用, comment: 换包装英文字不用抠图:新旧文字都用引号写进 prompt,开头加句 Keep everything else unchanged,瓶身和光影就纹丝不动。
- user: 第一次用的新手, category: 坑, comment: 我把换背景、加帽子、调亮塞进一条 prompt,出来脸都变了。拆成三次跑,每步只说一件事,上一步成图当下一步输入,就稳了。
- user: 自动化脚本党, category: 妙用, comment: 固定 seed 只改 prompt 里一个词,能并排出对比图挑效果,定了再换 seed 出正式片。CI 里设 RUNCOMFY_TOKEN 就免 login,跑批很顺。
- user: 自媒体运营, category: 坑, comment: 改图里嵌的中文横幅,出来全是糊字;换英文标牌文字反而一次过。后来才看到多语言该走 GPT Image 2 edit,别在 Kontext 上硬试。
- user: 摄影工作室后期, category: 注意, comment: image 要填公网能打开的 HTTPS 链接,我贴本地路径直接报 65;传图床再填 URL 就过了。另外没登录会报 77,先跑 runcomfy login。
- user: 设计工作室主理人, category: 启发, comment: 学到了「先保后改」:先声明哪些不能动,再说改什么,出图立刻稳。这套思路我搬到给外包写 brief 上,返工少了一大半。
