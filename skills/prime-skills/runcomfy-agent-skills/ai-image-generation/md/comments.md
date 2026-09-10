# ai-image-generation (`prime-skills/runcomfy-agent-skills/ai-image-generation`)

## comments

- user: 第一次用的新手, category: 坑, comment: 装完就 run，报未登录才知道要先 runcomfy login。我在服务器上没浏览器卡了半天，后来去 runcomfy.com/profile 拿 token 设成环境变量才跑通。
- user: 独立设计师, category: 坑, comment: 海报文字老被模型改词：要把文案用引号原样嵌进 prompt，如写着 "SALE 50%"。日文还得注明 Japanese kana，否则出罗马音。
- user: 电商美工, category: 妙用, comment: 先用 0.5K 一次出 4 张选方向，定了就固定 seed 提到 2K 复跑，构图基本不飘，重抽全省。4K 是 0.5K 十几倍价钱，草稿期别开。
- user: 全栈开发, category: 妙用, comment: 批量改图写成脚本：Nano Banana 2 Edit 默认保人脸，'去掉左上角水印'这类空间描述直接听懂，几十张一晚跑完，不用逐张手抠。
- user: 修图老炮儿, category: 注意, comment: 别学我把 steps 拉到 50，25 步以后看不出差别，纯慢纯费。草稿用 4-8 步，定稿 25；带文字的图 Klein 必崩，直接换 GPT Image 2。
- user: 独立开发者产品经理, category: 启发, comment: prompt 主语先行才管用：主体+场景+修饰，例如'紫猫坐石头上，黄金时刻，浅景深'。删掉华丽形容词之后，我的废图率明显降了。
