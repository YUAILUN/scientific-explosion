# Pantheon (召唤众神) Agent Skill

[![Project](https://img.shields.io/badge/Original_Project-Pantheon_K--Dense-blue)](https://pantheon.k-dense.ai/)
[![Standard](https://img.shields.io/badge/Agent_Skills-Standard_Compliant-green)](https://github.com/anthropics/skills)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

> **提出一个科学或研究问题。从亚里士多德到卡帕西，历史上的 80 位伟大思想家现场回答，每个人都用自己的声音回答。**
> 
> 本项目将 [Pantheon](https://pantheon.k-dense.ai/)（基于 [K-Dense-AI/mimeographs](https://github.com/K-Dense-AI/mimeographs)）完整蒸馏为标准的 Agent Skill，支持无缝安装到 **OpenAI Codex**、**Google Antigravity**、**Claude Code** 以及 **Cursor** 中。

---

## 目录结构

```
pantheon/
├── SKILL.md                          # 核心技能定义与 5 阶段执行 SOP
├── README.md                         # 安装与使用全景指南
├── references/
│   ├── catalog_80_thinkers.md        # 80 位先贤全景花名册与专属安装代码
│   ├── chambers.md                   # 预设主题分院（AI、哲学、生科、产业）
│   ├── synthesis_framework.md        # 辩证共识与深层断层图谱指南
│   ├── mimeo_guide.md                # K-Dense Mimeo 单体深度 Skill 安装指南
│   └── pantheon_data.json            # 80 位思想家结构化元数据
└── scripts/
    └── pantheon_cli.py               # 命令行组阁与检索辅助脚本
```

---

## 一键安装指南 (Installation)

### 1. 安装到 Google Antigravity
Antigravity 会自动读取 `~/.gemini/config/skills/` 目录中的技能：

```bash
# 创建软链接到 Antigravity 全局技能目录
ln -sfn /Users/yuailun/.gemini/antigravity/scratch/pantheon ~/.gemini/config/skills/pantheon
```

### 2. 安装到 OpenAI Codex
Codex 会自动读取 `~/.codex/skills/` 目录中的技能：

```bash
# 创建软链接到 Codex 全局技能目录
ln -sfn /Users/yuailun/.gemini/antigravity/scratch/pantheon ~/.codex/skills/pantheon
```

### 3. 安装到通用 Agent Skills 根目录 (`~/.agents/skills`)
```bash
ln -sfn /Users/yuailun/.gemini/antigravity/scratch/pantheon ~/.agents/skills/pantheon
```

*(也可以直接运行附带的安装命令快速完成全平台链接)*。

---

## 如何使用 (Usage)

在 Codex 或 Antigravity 聊天窗口中，你可以像在原版网页上一样，提出任何深刻的科学、算法、哲学或商业问题：

### 示例 1：通用跨学科联席辩论
> **用户输入**：
> `/pantheon 人类是否应该暂停前沿超大规模 AI 模型的训练？`

**万神殿输出流程**：
1. **智能组阁**：自动召集 `stuart-russell`（AI对齐与安全）、`richard-s-sutton`（算力教训）、`elon-musk`（生存风险与加速制造）、`hannah-arendt`（技术极权与行动复多性）、`andrej-karpathy`（工程锯齿状智能）。
2. **具身发言**：每位大师以真实第一人称发声，引用各自的思维模型和代表作。
3. **现场质询**：各流派大师针锋相对，直击彼此的假设死穴。
4. **终局提炼**：输出跨学科共识、不可调和的世界观断层、以及可执行的科研验证路线。

### 示例 2：指定专场分院辩论
> **用户输入**：
> `召唤众神 --chamber ai 纯自回归语言模型（Next-token prediction）能否通向 AGI 世界模型？`

### 示例 3：指定特定人物点将
> **用户输入**：
> `召唤 卡帕西、珀尔、萨顿、亚里士多德 讨论：如何在自动驾驶中平衡端到端神经网络与因果逻辑规则？`

---

## 80 位先贤单体深度 Skill 扩展

如果你希望让某位思想家常驻在你的当前代码仓库（例如让 Karpathy 审查你写的神经网络，让 Jobs 审查前端交互）：
你可以使用标准命令安装其单体包：

```bash
npx skills add K-Dense-AI/mimeographs/andrej-karpathy
npx skills add K-Dense-AI/mimeographs/steve-jobs
npx skills add K-Dense-AI/mimeographs/judea-pearl
```
详见 `references/mimeo_guide.md`。
