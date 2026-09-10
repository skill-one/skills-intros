# fingerprint-ci-gate (`liarjsdev/liarjs-skills/fingerprint-ci-gate`)

## scenario

爬虫团队某次更新了浏览器,当时没人察觉;几周后抓取流量被批量封禁,却查不出是哪次提交弄坏的指纹——排查如大海捞针。我把指纹检测装进 CI(自动化构建流程):每次提交自动扫描、与基线对比,回归当场拦在 PR,不等到线上炸雷。🚧
