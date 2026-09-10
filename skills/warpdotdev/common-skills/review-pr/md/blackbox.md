# review-pr (`warpdotdev/common-skills/review-pr`)

## blackbox

**function**: 审查一个代码变更 (PR) 的 diff,输出一份机器可读的评审报告 review.json:包含总体结论 (APPROVE/REJECT) 和逐行问题批注 (bug、安全、错误处理、注释与测试质量)。

- input: 一份 PR 的差异文件 pr_diff.txt + 描述文件 pr_description.txt, output: review.json:含总体结论 (APPROVE 或 REJECT)、一段评审总览,以及若干条精确到「文件+行号」的行内批注
- input: 一个包含真实 bug 的 diff (如某行漏了空值判断,会崩溃), output: review.json 中对应行出现一条 🚨 [CRITICAL] 批注,说明问题并附可直接采纳的修复代码建议块
- input: 一个干净无问题的 PR diff, output: review.json:verdict 为 APPROVE,comments 为空数组 [],总览里写明 Found: 0 critical, 0 important, 0 suggestions
