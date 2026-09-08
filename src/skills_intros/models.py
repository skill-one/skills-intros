"""Domain taxonomy and pydantic schemas for structured LLM outputs."""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Domain(StrEnum):
    """Usage-scenario taxonomy for skill classification.

    Each member carries (value, emoji, description); the description doubles as
    the classification hint injected into the domain prompt.
    """

    def __new__(cls, value: str, emoji: str, description: str) -> "Domain":
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.emoji = emoji
        obj.description = description
        return obj

    DEV_CODING = (
        "开发编程", "💻",
        "写代码、调试、重构、数据库、API/框架集成、爬虫与浏览器自动化"
    )
    TESTING_QA = ("测试与质量", "🧪", "测试编写与测试框架、E2E/UI 自动化测试、代码审查、质量检查与 bug 排查工具")
    DATA_ANALYSIS = ("数据分析", "📊", "SQL 查询、数据清洗、统计分析、可视化、报表与数据工程(ETL)")
    OPS_SECURITY = ("运维与安全", "🛡️", "部署发布、云基础设施、监控告警、SRE、网络配置与安全防护")
    OFFICE = ("办公效率", "🗂️", "docx/pdf/xlsx/ppt 等文档处理、邮件、日历、会议纪要、任务与项目管理")
    CONTENT_CREATION = ("内容创作", "✍️", "文章写作、文案、翻译、技术文档、社媒内容、播客/脚本等, 以文字与信息为主体的创作")
    DESIGN_MEDIA = ("设计多媒体", "🎨", "UI/平面设计、图像生成与编辑、视频剪辑、3D、品牌视觉等视觉与音视频制作")
    KNOWLEDGE = ("知识管理", "🧠", "笔记与知识库(Obsidian/Notion 等)、信息检索、调研与深度研究、资料整理沉淀")
    BUSINESS = ("商业运营", "📈", "市场营销、SEO、销售、客服、电商、增长与 CRM 等面向业务增长与客户的工作")
    PAY_FINANCE = ("支付金融", "💰", "支付集成、账单与发票、金融理财、交易类技能")
    EDUCATION = ("教育学习", "🎓", "教学备课、课程制作、学习辅导、刷题与面试准备")
    LIFE = ("生活服务", "🏠", "旅行规划、饮食、健身健康、个人日常事务")
    OTHER = ("其他", "❓", "仅当以上分类确实都不贴合时使用, 不要勉强归类")

    @classmethod
    def taxonomy_text(cls) -> str:
        """One '- emoji name: description' line per member; injected into the domain prompt."""
        return "\n".join(f"- {d.emoji} {d.value}: {d.description}" for d in cls)

    @classmethod
    def display(cls, value: str) -> str:
        """'emoji name' for known domain values; the input unchanged otherwise."""
        try:
            d = cls(value)
        except ValueError:
            return value
        return f"{d.emoji} {d.value}"


class DomainClassification(BaseModel):
    """Output schema for the `domain` prompt."""

    domain: Domain = Field(description="按使用场景找到你最贴合的分类")
    reason: str = Field(description="分类理由, 一句话")


class IntroText(BaseModel):
    """Output schema for free-text intro prompts (scenario_intro, comparison)."""

    text: str = Field(description="介绍词正文, 150~250 个汉字")


class BlackBoxPair(BaseModel):
    """One 「输入 → 输出」 example for the blackbox intro."""

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


class TriggerGuide(BaseModel):
    """Output schema for the `trigger_guide` prompt."""

    use_when: list[str] = Field(description="agent 应自动触发该 skill 的时机, 3~5 条")
    avoid_when: list[str] = Field(description="不应触发该 skill 的情形, 2~3 条")


class Taglines(BaseModel):
    """Output schema for the `tagline` prompt."""

    taglines: list[str] = Field(description="3 条宣传短标语, 每条 20 个汉字以内")


class SkillRecord(BaseModel):
    """A single skill loaded from the scraper index."""
    model_config = ConfigDict(frozen=True)

    id: str
    name: str
    installs: int
    source: str
    hash: str
    skill_md: str
    description: str = ""
