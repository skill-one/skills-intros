# baseline-ui (`ibelick/ui-skills/baseline-ui`)

## blackbox

**function**: 给你的界面代码做一次快速「去 AI 味」体检和修复:修掉间距、层级、排版、布局小毛病,让页面看起来是专业设计师过手的,而不是 AI 生成的。

- input: 「/baseline-ui src/components/Modal.tsx」—— 给我一个组件文件路径, output: 一份问题清单:每条都引用文件里的原始代码片段,说明为什么有问题,并给出可直接粘贴的修改后代码
- input: 一个 AI 生成的 React 页面(满屏紫色渐变、加载时页面空白跳动、按钮没有文字提示), output: 修好的同一份代码:去掉了渐变和多余特效,加载时有占位骨架,图标按钮加上了无障碍标签,排版和间距归位
- input: 「/baseline-ui」—— 什么都不带,只说一句"接下来帮我写个登录页", output: 之后写出的所有界面代码自动符合一套干净的 UI 基线:动画克制、层级清晰、排版规整,没有典型 AI 味
