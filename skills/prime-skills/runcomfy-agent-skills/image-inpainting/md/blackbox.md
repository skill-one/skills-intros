# image-inpainting (`prime-skills/runcomfy-agent-skills/image-inpainting`)

## blackbox

**function**: 帮我修图：把照片里指定的东西去掉、或把指定区域换成新内容，其余部分保持原样。

- input: 一张带水印的图片 + 一句话「去掉右下角的水印」, output: 处理好的新图片文件，水印消失，画面其他部分和原图一样
- input: 一张照片 + 一张标出目标区域的黑白蒙版图（白色=要改的地方）+ 一句描述（如「这里换成蓝天」）, output: 指定区域被替换/填充好的成品图，边缘自然过渡
- input: 一张街景照片 + 一句话「把画面上方的电线去掉」, output: 干净的图片文件：电线消失，天空和屋顶线条保持原样
