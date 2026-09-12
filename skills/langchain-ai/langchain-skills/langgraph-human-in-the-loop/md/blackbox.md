# langgraph-human-in-the-loop (`langchain-ai/langchain-skills/langgraph-human-in-the-loop`)

## blackbox

**function**: 帮你把全自动运行的 AI 工作流 (LangGraph) 改造成「关键步骤会停下来等人确认, 确认后接着跑完」的流程, 并修好停不下来、恢复不了、恢复后重复执行这类问题。

- input: 一段 LangGraph agent 代码 (现在从开始一路自动执行到结束), output: 改好的代码: 运行到关键节点会暂停, 把问题或草稿抛给你; 你回复后, 流程从暂停处接着走完
- input: 一句需求, 如「AI 起草的回复邮件要先给运营审, 通过才发」, output: 审批工作流代码: 展示草稿 → 等待批准或修改 → 通过则继续发送, 驳回则终止
- input: 一句症状描述, 如「等人回复后流程卡住不动」或「每次恢复都把前面的步骤重复跑了一遍」, output: 修正后的代码, 附一句原因说明 (如恢复时用错了指令、副作用放在了暂停点之前导致重复)
