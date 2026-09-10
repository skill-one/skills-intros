# baoyu-compress-image (`jimliu/baoyu-skills/baoyu-compress-image`)

## blackbox

**function**: 把图片文件压得更小（体积变小、画质基本不变），默认转成更省空间的 WebP 格式。

- input: 一张图片的路径，如 photo.png, output: 同位置的 photo.webp，并告知压了多少，如「245KB → 89KB，减少 64%」
- input: 一个装满图片的文件夹路径，如 ./images/, output: 文件夹里（包括子文件夹）的每张图片都被替换成压缩后的小文件，逐张报告瘦身效果
- input: 图片路径 + 要求「保持 PNG 格式、保留原图」, output: 得到一个更小的 PNG 文件，原图也原封不动保留
