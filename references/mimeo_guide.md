# K-Dense Mimeo 与独立思想家 Skill 安装指南 (Mimeo Integration Guide)

本技能（`pantheon`）是万神殿的**核心调度器与跨学科辩论引擎**。
它的底层人设数据库源自开源项目 [K-Dense-AI/mimeographs](https://github.com/K-Dense-AI/mimeographs) 与蒸馏引擎 [K-Dense-AI/mimeo](https://github.com/K-Dense-AI/mimeo)。

如果你希望将某一位具体先贤作为长期专属助手深入绑定到你的项目或日常编程中（例如让乔布斯常驻审查产品，让卡帕西常驻写模型，让巴菲特常驻做财务投资分析），你可以非常便捷地安装单体深度 Skill。

---

## 一、安装单体深度 Expert Skill (80位可选)

K-Dense 为全量 80 位先贤制作了符合 Open Agent Skills 标准的独立包。你可以使用 `npx skills add` 快速安装到 Codex、Claude Code、Cursor 或全局环境中：

### 1. 常用代表人物一键安装命令

```bash
# AI 架构与工程师常驻代表
npx skills add K-Dense-AI/mimeographs/andrej-karpathy   # 卡帕西：从零造轮子、Software 3.0、vibe coding
npx skills add K-Dense-AI/mimeographs/richard-s-sutton  # 萨顿：算力为王、苦涩的教训、通用搜索学习
npx skills add K-Dense-AI/mimeographs/judea-pearl       # 珀尔：因果阶梯、反事实推断、反盲目拟合
npx skills add K-Dense-AI/mimeographs/ilya-sutskever    # 苏茨克维：压缩即智能、安全超级智能

# 哲学与批判性思维常驻代表
npx skills add K-Dense-AI/mimeographs/aristotle         # 亚里士多德：四因说、中庸之道、目的论
npx skills add K-Dense-AI/mimeographs/david-hume        # 休谟：经验实证、归纳怀疑
npx skills add K-Dense-AI/mimeographs/ludwig-wittgenstein # 维特根斯坦：语言游戏、界定概念混淆

# 产业与极端工程常驻代表
npx skills add K-Dense-AI/mimeographs/elon-musk         # 马斯克：物理第一性、5步工程砍需求法则
npx skills add K-Dense-AI/mimeographs/steve-jobs        # 乔布斯：产品与审美十字路口、拒绝平庸
npx skills add K-Dense-AI/mimeographs/warren-buffett    # 巴菲特：能力圈、护城河、安全边际

# 科学家与生物医学常驻代表
npx skills add K-Dense-AI/mimeographs/aviv-regev        # 雷格夫：单细胞基因组、TechBio高通量闭环
npx skills add K-Dense-AI/mimeographs/robert-langer     # 兰格：生物材料与纳米药物递送、科研转化
npx skills add K-Dense-AI/mimeographs/walter-c-willett  # 威利特：超长期大样本队列流行病学
```

### 2. 批量安装多个专家

```bash
npx skills add \
  K-Dense-AI/mimeographs/andrej-karpathy \
  K-Dense-AI/mimeographs/judea-pearl \
  K-Dense-AI/mimeographs/elon-musk \
  K-Dense-AI/mimeographs/aristotle
```

安装后，单体 Skill 包含完整的：
- `SKILL.md` (按需动态激活)
- `AGENTS.md` (若拷入项目根目录则作为常驻系统性格)
- `references/principles.md` (完整核心原则)
- `references/frameworks.md` (可执行分析框架)
- `references/mental-models.md` (思维模型库)
- `references/quotes.md` (经查证的名言原话)

---

## 二、使用 Mimeo 为任何新人物制作专属 Skill

若你想召唤 80 位名单之外的思想家（例如：费曼 Richard Feynman、香农 Claude Shannon、图灵 Alan Turing、王阳明 Wang Yangming、达尔文 Charles Darwin）：

可直接使用 K-Dense 的生成工具 `mimeo`：

```bash
# 1. 克隆 mimeo 仓库
git clone https://github.com/K-Dense-AI/mimeo.git
cd mimeo

# 2. 安装环境
uv sync

# 3. 配置 .env 密钥 (OpenRouter / Parallel)
cp .env.example .env

# 4. 一键自动研读全网公开著作、访谈、论文并蒸馏生成 Skill
uv run mimeo "Richard Feynman" --mode full --format both
```

生成结果将自动保存在 `output/richard-feynman/`，可直接复制到 `~/.codex/skills/` 或 `~/.gemini/config/skills/` 中使用！
