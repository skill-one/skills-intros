# codex-pet (`prime-skills/runcomfy-agent-skills/codex-pet`)

## whitebox

- 对用户参考图发起唯一一次 `runcomfy run openai/gpt-image-2/edit` 调用，生成 1024x1024 洋红底 (#FF00FF) 色键的 Q 版标准姿态图。
- ImageMagick 把洋红抠成透明（-fuzz 18%）、trim 裁边并等比缩放居中进 192x208 透明格子，得到标准 cell。
- 对这一个 cell 施加 ImageMagick 微变换（-roll 平移、眨眼遮罩、SRT 旋转、-flop 镜像），按 Codex 契约的每行帧数生成 9 行动画条，行尾补全透明帧；running-left 行直接由 running-right 行水平翻转得到。
- 9 行纵向拼接成 1536x1872（8 列 x 9 行 x 192x208）图集，转 WebP，并写出 pet.json 清单。
- pet.json + spritesheet.webp 复制进 ${CODEX_HOME:-$HOME/.codex}/pets/<name>/，Codex 重载后与 8 个内置宠物并排出现。

- 透明度 workaround（转换）：GPT Image 2 只输出 RGB 无 alpha，故提示词强制纯色洋红底并禁止宠物自带近品红高光，后期 `-fuzz 18% -transparent #FF00FF` 色键抠出 alpha；fuzz 可按边缘光晕调到 25% 或宠物含近品红色时降到 8-10%。
- 一帧源 + 确定性微动画（生成策略）：不烧 72 次模型调用——单个标准 cell 经 1-2px 平移、y=82 处 6px 高眨眼色带、±1-2° 旋转、镜像复制成 72 格，复刻 Codex 内置宠物'微妙动画'的手感；每行帧数契约严格对齐（idle=6, 跑右/跑左=8, waving=4, jumping=5, failed=8, waiting/running/review=6），多余格用全透明 192x208 填充。
- 风格与身份锁在唯一的模型调用里（校验靠 prompt）：'头占 60% 高度的夸张 Q 版 + 像素感描边 + 有限色板 + 平涂'全在 prompt 中锁死，同时显式排除插画/3D/渐变/阴影等漂移项；身份漂移时重跑 step 1 收紧特征描述即可，步骤 2-6 确定性不变。外部依赖：RunComfy CLI（RUNCOMFY_TOKEN 认证，sysexits 退出码）+ OpenAI GPT Image 2（经 RunComfy）+ ImageMagick（magick）。
