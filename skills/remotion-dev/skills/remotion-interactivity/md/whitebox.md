# remotion-interactivity (`remotion-dev/skills/remotion-interactivity`)

## whitebox

- 用 Interactive.* 包装 (Interactive.Div/Img/Video/Sequence) 并加硬编码 name, 固定文案直接内联, 让每个元素可被 Studio 选中识别
- 所有 CSS 样式写成内联对象字面量传入 style —— 禁止常量引用、对象展开、运算
- 动画以 interpolate() 直接内联写在 style 的 scale/translate/rotate 上 (不用 transform), 输入只允许 frame, 输入/输出范围与 easing 全部硬编码
- 组合元数据 (width/height/fps/durationInFrames/defaultProps) 内联在 <Composition>, 动态部分才走 calculateMetadata(); 特效数组同样内联且形状稳定
- Remotion Studio 解析这套结构 → 元素可点击选中、拖拽/缩放/旋转、样式与关键帧可编辑; 结构太复杂则数值灰显

- 约定式结构识别: Studio 靠匹配代码模式 (Interactive.* + name + 内联 style + 内联 interpolate) 建立可视化编辑映射; 偏离约定 (useMemo 生成 style、引用常量、任意变量参与 interpolate、数学运算) 即识别失败 → 灰显
- 关键帧提取: 内联 interpolate() 的硬编码参数 (frame 输入、输入/输出 range、Easing 如 spring、extrapolate clamp、output 如 perceptual-scale) 被标准化为 Studio 中可编辑的关键帧与缓动曲线
- 编辑写回代码: <Composition>/<Still> 上的内联 defaultProps 使 Props 编辑器能把可视化修改保存回代码; 仅动态元数据经 calculateMetadata() 处理。外部依赖: 仅 Remotion v4 Studio, 自定义组件按官方 make-component-interactive API 接入, 无模型/API 依赖
