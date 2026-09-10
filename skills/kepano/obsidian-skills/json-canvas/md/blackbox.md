# json-canvas (`kepano/obsidian-skills/json-canvas`)

## blackbox

**function**: 我能把你的想法变成 Obsidian 里可拖拽、可连线、可分组的可视化画布文件(.canvas):思维导图、流程图、项目看板、关系图,说清楚就行。

- input: 一句话需求,如「帮我做一张《三体》人物关系图,按地球/三体/其他分三组」, output: 一个 .canvas 文件,在 Obsidian 里打开就是分好组、连好线的可视化关系图,可自由拖拽缩放
- input: 一段流程描述,如「需求 → 设计 → 开发 → 测试 → 上线,测试不过要打回开发」, output: 一个 .canvas 文件,内含带箭头和标注的横向流程图,回路箭头也画好
- input: 一个已有的 .canvas 文件,加一句改动要求,如「加一个『复盘』节点连到『上线』后面」, output: 改好的 .canvas 文件:新节点放在不遮挡原有内容的位置,并已与指定节点连线
