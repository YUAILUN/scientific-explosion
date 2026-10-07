# Scientific Explosion (科学爆发)

> **A Multi-Perspective Dialectical Inquiry & Council Review Framework for AI Agents**  
> 面向科学研究、算法设计与重大技术决策的**多流派辩证审议与思维模型矩阵** Agent Skill。

[![GitHub Repo](https://img.shields.io/badge/GitHub-YUAILUN%2Fscientific--explosion-181717?logo=github)](https://github.com/YUAILUN/scientific-explosion)
[![Standard](https://img.shields.io/badge/Agent_Skills-Open_Standard-green)](https://github.com/anthropics/skills)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## 📌 项目定位 (Overview)

在面对前沿科学假设、前沿 AI 架构选型（如 Scaling Law vs. 因果表征 vs. 世界模型）或重大系统工程决策时，常规单一 AI 生成的回答容易陷入统计学上的**中庸折中（Mode Collapse）**，给出模棱两可、看似面面俱到却缺乏判决性力度的结论。

**Scientific Explosion (科学爆发)** 提供了一套多智能体辩证审议工作流（Dialectical Council Review SOP）：
- **多流派思维矩阵**：汇聚哲学认识论、经验实证、因果推断、前沿机器学习与宏观系统工程等 80 个经过公开学术文献沉淀的经典思维透镜。
- **真实冲突展开**：从第一性原理、因果干预、算力法则到物理与商业现实约束，展开多维度思想对抗与假设压力测试。
- **反折中终局提炼**：拒绝和稀泥，提炼出不可动摇的底线共识、深层公理断层（世界观冲突根源）以及可落地的**可证伪判决性实验（Crucible Experiments）**。

兼容 **OpenAI Codex**、**Google Antigravity**、**Claude Code** 以及 **Cursor** 等支持标准 Agent Skill 的环境。

---

## ⚖️ 免责声明与学术伦理 (Disclaimer & Ethics)

1. **概念性方法论模拟**：本项目中所有学者与思想家透镜，均作为**学术概念模型与方法论代表（Epistemic Lenses）**，用于科研思辨、架构推演与思想实验；
2. **非真实个人言论**：系统生成内容基于公开学术理论、方法论框架与历史文献逻辑推演，**绝不代表任何现存学者或历史先贤本人的真实陈述、当下意志或个人背书**；
3. **科研辅助性质**：本工具产出的推论与实验设计仅供科研人员决策参考与头脑风暴，不作为最终临床医疗、法律裁决或商业投资凭证。

---

## 🏛️ 四大专题审议分院 (Chambers)

| 专题分院 | 关注领域 | 核心方法论代表透镜 |
|---|---|---|
| **计算与机器智能分院** | Scaling Law 边界、世界模型、因果推理、对齐与表征 | 因果阶梯 (Pearl)、算力教训 (Sutton)、Software 3.0 (Karpathy)、JEPA (LeCun)、信息压缩 (Sutskever) |
| **哲学与认识论分院** | 科学实在论、归纳怀疑、意识与语言界限、工程伦理 | 四因说 (Aristotle)、先验综合 (Kant)、经验归纳批判 (Hume)、语言游戏 (Wittgenstein)、行动复多性 (Arendt) |
| **自然科学与生命医学分院** | 复杂生物网络、高通量筛选、流行病学队列、科研转化 | 单细胞图谱 (Regev)、大科学协同 (Lander)、纳米药物工程 (Langer)、长期队列流行病学 (Willett) |
| **产业工程与系统落地分院** | 第一性物理极限、制造工程瓶颈、资本配置、组织护城河 | 物理第一性原理 (Musk)、人文艺术十字路口 (Jobs)、能力圈与安全边际 (Buffett)、内生有机增长 (Faulkner) |

---

## 📂 项目结构 (Repository Layout)

```
scientific-explosion/
├── SKILL.md                          # 核心技能规范与 5 阶段辩证审议 SOP
├── README.md                         # 规范说明、免责声明与安装指南
├── references/
│   ├── catalog_80_thinkers.md        # 80 个方法论模型详引与思维透镜索引
│   ├── chambers.md                   # 专题审议分院详细配置
│   ├── synthesis_framework.md        # 辩证共识与深层公理断层提炼规范
│   ├── mimeo_guide.md                # 独立单体思维技能扩展指引
│   └── pantheon_data.json            # 结构化思维模型元数据
└── scripts/
    └── pantheon_cli.py               # 本地组阁匹配、思维模型检索与审议生成 CLI
```

---

## 💻 一键安装与配置 (Installation)

### 1. 安装至 Google Antigravity
```bash
ln -sfn "$(pwd)" ~/.gemini/config/skills/pantheon
```

### 2. 安装至 OpenAI Codex
```bash
ln -sfn "$(pwd)" ~/.codex/skills/pantheon
```

### 3. 安装至通用 Agent 根目录
```bash
ln -sfn "$(pwd)" ~/.agents/skills/pantheon
```

---

## 💡 使用方法 (Usage Examples)

在对话环境中，输入以下指令或直接提出复杂科研假说：

### 示例 1：全域跨学科审议
> **输入**：
> `/pantheon 当前大语言模型的推理能力涌现，究竟是统计相关性的极致压缩，还是形成了真正的隐式世界模型？`

### 示例 2：指定专场分院
> **输入**：
> `召唤众神 --chamber ai 蛋白质结构预测领域，纯数据驱动深度学习与量子化学第一性原理计算如何结合？`

### 示例 3：指定思维透镜点将
> **输入**：
> `召唤 珀尔、萨顿、卡帕西、亚里士多德 讨论：自动驾驶多模态大模型的因果鲁棒性瓶颈。`

---

## 🙏 致谢与开源说明 (Acknowledgements)

- 理论与数据基础：本项目的 80 位思想模型矩阵结构参考并整理自学术开源项目 [K-Dense Mimeographs](https://github.com/K-Dense-AI/mimeographs)（遵循 MIT License），在此向相关研究团队致谢。
- 架构遵循：本技能遵循开放的 [Agent Skills](https://github.com/anthropics/skills) 规范标准设计与构建。

---

## 📄 许可证 (License)

本项目采用 [MIT 许可证](LICENSE)。
