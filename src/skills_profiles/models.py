"""Domain taxonomy and pydantic schemas for structured LLM outputs."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Domain(StrEnum):
    """Usage-scenario taxonomy for skill classification.

    Each member carries (value, emoji, description, cover_style); the description
    doubles as the classification hint injected into the domain prompt, and the
    cover_style is the fixed look of the category — medium, palette and light,
    never objects: what is drawn comes from the `cover` prompt and from the one
    character framing images.py appends, so the 13 categories stay visually
    distinct without any of them competing with the subject for the picture.
    """

    def __new__(cls, value: str, emoji: str, description: str,
                cover_style: str) -> "Domain":
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.emoji = emoji
        obj.description = description
        obj.cover_style = cover_style
        return obj

    # set by __new__ from each member's tuple; declared for the type checker
    emoji: str
    description: str
    cover_style: str

    DEV_CODING = (
        "开发编程", "💻",
        "写代码、调试、重构、数据库、API/框架集成、爬虫与浏览器自动化",
        "flat vector illustration, deep indigo background, cyan and lime terminal glow",
    )
    TESTING_QA = (
        "测试与质量", "🧪",
        "测试编写与测试框架、E2E/UI 自动化测试、代码审查、质量检查与 bug 排查工具",
        "flat vector illustration, teal background, amber highlights",
    )
    DATA_ANALYSIS = (
        "数据分析", "📊",
        "SQL 查询、数据清洗、统计分析、可视化、报表与数据工程(ETL)",
        "flat vector illustration, navy background, coral and mint accents",
    )
    OPS_SECURITY = (
        "运维与安全", "🛡️",
        "部署发布、云基础设施、监控告警、SRE、网络配置与安全防护",
        "flat vector illustration, slate blue background, warm orange glow",
    )
    OFFICE = (
        "办公效率", "🗂️",
        "docx/pdf/xlsx/ppt 等文档处理、邮件、日历、会议纪要、任务与项目管理",
        "flat vector illustration, warm beige background, muted blue and terracotta",
    )
    CONTENT_CREATION = (
        "内容创作", "✍️",
        "文章写作、文案、翻译、技术文档、社媒内容、播客/脚本等, 以文字与信息为主体的创作",
        "flat vector illustration, cream background, ink blue and ochre",
    )
    DESIGN_MEDIA = (
        "设计多媒体", "🎨",
        "UI/平面设计、图像生成与编辑、视频剪辑、3D、品牌视觉等视觉与音视频制作",
        "flat vector illustration, off-white background, vivid magenta, cyan and yellow",
    )
    KNOWLEDGE = (
        "知识管理", "🧠",
        "笔记与知识库(Obsidian/Notion 等)、信息检索、调研与深度研究、资料整理沉淀",
        "flat vector illustration, dusty violet background, mint accents",
    )
    BUSINESS = (
        "商业运营", "📈",
        "市场营销、SEO、销售、客服、电商、增长与 CRM 等面向业务增长与客户的工作",
        "flat vector illustration, light grey background, navy and gold",
    )
    PAY_FINANCE = (
        "支付金融", "💰",
        "支付集成、账单与发票、金融理财、交易类技能",
        "flat vector illustration, dark green background, gold accents",
    )
    EDUCATION = (
        "教育学习", "🎓",
        "教学备课、课程制作、学习辅导、刷题与面试准备",
        "flat vector illustration, sky blue background, warm yellow accents",
    )
    LIFE = (
        "生活服务", "🏠",
        "旅行规划、饮食、健身健康、个人日常事务",
        "flat vector illustration, soft peach background, sage and coral accents",
    )
    OTHER = (
        "其他", "❓",
        "仅当以上分类确实都不贴合时使用, 不要勉强归类",
        "flat vector illustration, neutral grey background, one blue and one orange accent",
    )

    @classmethod
    def taxonomy_text(cls) -> str:
        """One '- emoji name: description' line per member; injected into the domain prompt."""
        return "\n".join(f"- {d.emoji} {d.value}: {d.description}" for d in cls)

    @classmethod
    def _lookup(cls, value: str) -> "Domain | None":
        """The member whose value is `value`, or None.

        `Domain(value)` is how a plain string maps back to a member (pydantic uses
        it too); wrapped once because the enum's own constructor takes the 4-tuple.
        """
        try:
            return cls(value)  # type: ignore[call-arg]
        except ValueError:
            return None

    @classmethod
    def display(cls, value: str) -> str:
        """'emoji name' for known domain values; the input unchanged otherwise."""
        d = cls._lookup(value)
        return value if d is None else f"{d.emoji} {d.value}"

    @classmethod
    def style_for(cls, value: str) -> str:
        """The category's cover style; an unknown or missing value gets OTHER's."""
        d = cls._lookup(value)
        return (d if d is not None else cls.OTHER).cover_style


class DomainClassification(BaseModel):
    """Output schema for the `domain` prompt."""

    domain: Domain = Field(description="按使用场景找到你最贴合的分类")
    reason: str = Field(description="分类理由, 极简一句话")


class IntroText(BaseModel):
    """Output schema for free-text profile prompts (scenario)."""

    text: str = Field(description="介绍词正文, 100 个字以内")


class ImagePrompt(BaseModel):
    """Output schema for the `cover` prompt: one English line describing the picture.

    Not just an `IntroText`, because this text feeds a text-to-image model rather
    than a human. Measured against real endpoints: a recipe that came back as
    Chinese marketing prose still validated as a string, and became a garbage
    picture. Every rule below is therefore a rejection instructor hands back to
    the model, so the recipe is corrected before it is stored.
    """

    text: str = Field(description="英文画面主体: 逗号分隔的短语, 40 词以内, 写那个人在做什么")

    @field_validator("text")
    @classmethod
    def _english_phrase(cls, value: str) -> str:
        value = " ".join(value.split()).strip().rstrip(".,;: ")
        if not value:
            raise ValueError("不能为空")
        if not value.isascii():
            raise ValueError("必须是纯英文 (ASCII), 不要出现中文")
        if len(value.split()) > 40:
            raise ValueError("超过 40 个英文单词, 请精简成逗号短语")
        if any(mark in value for mark in "!?\"'()"):
            raise ValueError("只要逗号分隔的短语, 不要问句/引号/括号")
        return value


class BlackBoxPair(BaseModel):
    """One 「输入 → 输出」 example for the blackbox profile."""

    input: str = Field(description="用户实际会给出的输入, 如文件路径、URL、一段文本")
    output: str = Field(description="用户实际会拿到的输出, 如生成的文件、报告、代码")


class BlackBoxIntro(BaseModel):
    """Output schema for the `blackbox` prompt: outside view, no internals."""

    function: str = Field(description="这个 skill 是做什么的, 一句话")
    input_output: list[BlackBoxPair] = Field(
        description="典型「输入 → 输出」对照, 3~5 条"
    )


class WhiteBoxIntro(BaseModel):
    """Output schema for the `whitebox` prompt: inside view of how it works."""

    execution_flow: list[str] = Field(description="主路径 (happy path) 执行流程, 按顺序 3~5 步")
    mechanisms: list[str] = Field(description="关键实现机制, 2~3 条; 依赖的外部工具/库/模型写在此处")


class Persona(BaseModel):
    """Output schema for the `persona` prompt: the skill's occupational portrait."""

    tool: str = Field(description="最具标志性的趁手工具, 写实际操作的那个真实工具/对象, 如 git, figma")
    role: str = Field(description="最合适的职业角色, 像真实职业一样命名自己, 如 提交把关人、文档排版师")
    scene: str = Field(description="最高频、最常见的工作场景, 用户最需要你的那一刻, 如 改完代码准备提交时")


class Taglines(BaseModel):
    """Output schema for the `tagline` prompt."""

    taglines: list[str] = Field(description="3 条宣传短标语, 每条 20 个字以内")


class SkillComment(BaseModel):
    """One first-person user comment on a skill."""

    user: str = Field(description="评论者身份, 简短具体, 如 后端老兵、第一次用的新手")
    category: str = Field(description="评论类型, 通常为 妙用 / 坑 / 注意 / 启发 之一, 也可自拟")
    comment: str = Field(description="评论正文, 第一人称, 有实质性帮助, 60 字以内")


class SkillComments(BaseModel):
    """Output schema for the `comments` prompt: users commenting on the skill."""

    comments: list[SkillComment] = Field(description="4~6 条来自不同背景用户的评论")


class SkillRecord(BaseModel):
    """A single skill loaded from the scraper index."""
    model_config = ConfigDict(frozen=True)

    id: str
    name: str
    installs: int
    source: str
    hash: str
    skill_md: str = ""  # filled in by data.read_skill_md when a run needs it
    description: str = ""
