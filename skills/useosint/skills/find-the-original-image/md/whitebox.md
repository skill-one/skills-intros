# find-the-original-image (`useosint/skills/find-the-original-image`)

## whitebox

- 输入定版：拿原始最高分辨率文件（非截图），先跑文件元数据检查。
- 全帧多引擎初搜：按素材类型选引擎（人脸→Yandex、物体/地标/图中文字→Google Lens、查旧拷贝→TinEye、中文内容→Baidu），至少跑三个。
- 裁剪重搜：对脸、招牌、徽章、水印等独特细节逐一裁剪单独重搜，必要时水平镜像后再跑（应对规避自动匹配的转发）。
- 定位最早版本：TinEye 按 oldest 排序，把拿到的最早日期当搜索覆盖面的上限，而非结论。
- 读取匹配页面并固证：收割摄影师/日期/说明/文件名，用存档交叉验证日期，按四级置信度定级，再按产出转交下游技能（定位→geolocate-from-pixels、人名→find-anyone 等）。

- 引擎分派表 + 结果分歧即信号：纯依赖外部搜索引擎 API/网页（Yandex、Google Lens、Bing Visual Search 的框选区域工具、TinEye、Baidu），无本地模型；各引擎对同一张图的结果不一致本身被当作证据——如 TinEye 出现多年前的精确拷贝而 Lens 只有近期转发，即二手素材的特征指纹。
- 视频与低质输入的预处理回路：视频抽关键帧（开头/中段/结尾/含招牌或人脸的帧）按静图搜；低质图先上采样、去噪、校正色阶再重跑。核心手法是裁剪——原图指纹被背景主导，裁到独特物体才命中被重新裁切过的转发版。
- 出处验证管线：严格区分『包含此图的页面』（证据）与『相似图』（非证据），候选需像素级细节比对确认；最早日期经存档首capture（read-deleted-pages）、日期限定文本搜索（google-like-a-spy）、最大分辨率版本、水印裁剪单搜、图库检查五路交叉；输出按 confirmed / probable / match-only / unconfirmed 定级，人脸引擎（PimEyes/FaceCheck.ID/Search4Faces）仅限有授权场景，且命中一律视为未确认。
