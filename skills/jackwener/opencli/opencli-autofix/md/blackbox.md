# opencli-autofix (`jackwener/opencli/opencli-autofix`)

## blackbox

**function**: 当你的 opencli 命令 (一条命令直接读取网站数据的工具) 报错跑不通、或返回结果不对时, 我把问题修好, 让命令重新跑出正确数据。

- input: 一条跑不通的命令和报错, 如「opencli zhihu hot 报错: Could not find element」, output: 同一条命令重新跑通, 直接拿到知乎热榜数据, 附一句「哪里坏了、改了什么」的简短说明
- input: 「命令不报错但结果为空」, 如 opencli xiaohongshu search "咖啡" 返回 0 条, 而你自己浏览器里明明看得到内容, output: 要么换个查法重新拿到数据; 要么明确告诉你: 命令没坏, 是登录过期或被网站限流, 建议你先去网站重新登录, 不乱改
- input: 修不动的情况, 如网站弹验证码、要求登录、连接不上浏览器, output: 直接停手, 告诉你卡在哪、需要你做什么 (如先登录网站、运行检查命令), 不会瞎改一通白折腾
