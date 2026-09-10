# extension-camera (`caffeinelabs/skills/extension-camera`)

## whitebox

- 识别任务需求: Web 应用需要摄像头能力 (预览/拍照/前后摄切换)
- 安装 npm 包 @caffeineai/camera (~0.1.1), 引入预制 React Hook useCamera
- 调用 useCamera(config) 并解构状态与方法 (isActive, error, startCamera, capturePhoto, switchCamera, videoRef, canvasRef 等)
- 将 videoRef 挂到 <video> 做预览, canvasRef 挂到隐藏 <canvas>, 按钮绑定 start/stop/switch/capture 并在未就绪时禁用
- capturePhoto 返回 File 对象供后续使用; error 出现时按类型展示错误信息

- 核心逻辑全部封装在不可修改的预制 Hook (useCamera) 中: 自带 isSupported/error/isLoading 状态与 start/stop/capture/switch/retry 方法, 页面代码只做接线, 不写底层摄像头逻辑
- 配置驱动 + 类型化校验: CameraConfig 声明 facingMode ('user'|'environment')、宽高、quality (0~1)、format (jpeg/png/webp); 错误按 CameraError 枚举 (permission/not-supported/not-found/unknown/timeout) 归类返回, 页面据此展示
- 技能指南强约束保证体验: 拍照按钮必须放在预览上、预览必须有显式非零且响应式的尺寸、桌面端禁用切换 (仅 environment 可用)、按钮未初始化完成不可点击
- 外部依赖: npm 包 @caffeineai/camera ~0.1.1 (React Hook, 基于 React RefObject)
