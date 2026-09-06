---
name: note-skill
description: 生成或改写 HTML 学习笔记。技术主题使用 Deep Study，先组织问题驱动的知识链、关键推导和学习优先级，再排版为可复习的长文；也支持原有学霸手写笔记和手账风格。适用于“学习笔记”“学霸笔记”“HTML 笔记”、论文或代码学习笔记，以及面试复习笔记；仅问一个技术问题时不必生成整份笔记。
---

# note-skill · Deep Technical Study Notes + Visual Notes

先组织知识和教学逻辑，再将理解结构渲染成笔记。降低语言理解成本，保留决定理解的机制、数学、实现和边界。

**内容正确性与理解完整性优先于视觉紧凑。** 不得为固定页高、整齐卡片或短篇幅删除关键解释；按 [视觉检查清单](references/checklist.md) 拆页或拆节。

## 模式与输出

| 风格 | 默认选择条件 | 模板 | 布局 |
| --- | --- | --- | --- |
| A · 学霸笔记 | 轻量总结、非技术笔记，或明确要求手写风格 | [template.html](assets/template.html) | [layouts.md](references/layouts.md) |
| B · 手账 / Journal | 明确要求皮革本、手账、翻页 | [template-journal.html](assets/template-journal.html) | [layouts-journal.md](references/layouts-journal.md) |
| C · Deep Study | 系统学习技术主题、理解算法或机制、技术面试复习 | [template-deep-study.html](assets/template-deep-study.html) | [layouts-deep-study.md](references/layouts-deep-study.md) |

用户指定的风格优先。技术深度与视觉风格独立：技术学习即使选 A/B，也走内容流程；仅美化已有笔记时保留其事实与范围，流程可以轻量执行，不强加推导和面试题。

默认交付可直接打开的 HTML，CSS 与必要 JS 内联；尊重明确指定的 Markdown 输出，跳过 HTML 映射和渲染。字体等外部资源不等于离线自包含，按模板检查回退。无需构建工具或前端框架。

## 工作流

### 1. Understand

从请求与材料确认或推断主题、已有基础、学习目标、是否面向面试、时间预算、内容来源和期望深度。已有信息足够就继续，只有缺失信息会改变主题或来源范围时才询问。

默认读者：有基本编程／数学基础，但第一次系统学习本主题。默认目标：建立完整 picture、掌握核心机制、能回答面试追问。未给时间预算时按核心主线分配篇幅，不凭空设页数上限。

**完成条件：** 明确学习范围与读者起点；正文开头简短注明关键假设、目标和阅读优先级。

### 2. Research / Grounding

先读内容来源，再写笔记。读取 [grounding.md](references/grounding.md)：处理论文、PDF、博客、代码、Markdown、网页，区分来源事实、解释性推导和教学示例，记录核心结论的出处及缺口。

`笔记.md` 是本仓库的教学设计 exemplar，提炼已放入 references；它和模板示例都不是其他技术主题的事实依据。不要求使用 Skill 的人再次提供该文件。

**完成条件：** 核心机制及适用条件有可靠依据；资料缺口和冲突已处理或明确标出，未核实结论不写成事实。

### 3. Build Knowledge Chain

读取 [knowledge-chain.md](references/knowledge-chain.md)，先形成简短的内部章节蓝图：每个重要章节写明 Previous / Gap / Bridge / Mechanism / Tradeoff / Next。用真实依赖组织主线，独立路线画分支，教学顺序不冒充历史演进。

**完成条件：** 读者知道每个核心概念为什么此刻出现；前文留下的问题有后文落点或明确的范围边界。

### 4. Depth Planning

读取 [interview-priority.md](references/interview-priority.md)；涉及公式、算法、系统流程或代码时读取 [technical-depth.md](references/technical-depth.md)。为知识点分配 CORE / FOLLOW-UP / OPTIONAL，决定需要推导、核心公式、数值／符号例子、代码、流程、对比或一句扩展介绍中的哪些。

**完成条件：** 难但决定主线的内容留在 CORE；每个核心主题有可观察的掌握标准，篇幅集中于真正的逻辑断点。

### 5. Draft Content First

读取 [pedagogy.md](references/pedagogy.md)，先完成与 HTML 无关的正文草稿。通常从问题到直觉，再到精确机制、必要推导／例子，最后回收直觉和本节结论；按实际知识关系调整，不逐节机械填模块。

先讲清正文，再按目标压缩面试回答。需要校准讲解质量时读取 [exemplars.md](references/exemplars.md)，模仿其组织理由而非主题和措辞。

**完成条件：** 草稿已有完整解释、必要公式与示例，理论—流程—代码能互相定位；不是等待 HTML 阶段填充的提纲。

### 6. Content Audit

读取 [content-checklist.md](references/content-checklist.md)。逐项核对适用的 P0，在内部记录章节证据；不适用项注明原因。失败项返回草稿修正，不能用视觉组件遮盖。

**完成条件：** 所有适用 P0 通过，读者可以独立复述核心机制，面试回答能从正文推出。

### 7. Semantic Layout Mapping

只在内容通过审查后，读取所选风格的布局文件和 [components.md](references/components.md) 对应部分。原因—结果用 flow，本质差异用 compare，条件分支用 table，执行顺序用 process，知识缺口用 transition。普通解释保留连贯段落。

**完成条件：** 组件与知识关系对应；布局容纳正文，未反向删改关键内容。无需每节用齐组件。

### 8. Render HTML

复制所选模板到用户指定目录；未指定时用 `notes/<主题短名>/index.html`。读取模板 `<style>` 确认可用类名，替换标题、示例正文、目录、来源和占位符。Style B 的示例正文还在底部 `texts` 中，必须一并替换。

保留 A 的纸张／装订／write-in、B 的皮革／翻页系统；C 使用长文版式、稳定语义色、可读公式与代码。图标按需使用 Lucide / Remix Icon 或内联 SVG，不用 emoji 作装饰。C 可完全不用图标。

**完成条件：** HTML 内容与通过审查的草稿一致；标题、公式、变量、代码、来源和章节锚点正确，不残留模板主题。

### 9. Final QA

内容变动后重查 [content-checklist.md](references/content-checklist.md) 受影响项；同时执行 [checklist.md](references/checklist.md) 的通用项及所选风格项。有浏览器时实际预览桌面与窄屏，检查长公式、表格、代码、目录和交互；只有静态检查时如实说明尚未验证的项目。

**完成条件：** 内容与视觉检查均通过。存在未解决的内容 P0 时不宣称成稿通过；可说明缺口并交付明确标注的草稿。

## 最终交付

交付完整笔记和可点击文件路径，不只给提纲；默认不展示内部章节蓝图、草稿过程或审查表。笔记包含大图景、阅读优先级、连贯正文、必要来源与紧凑回顾，面试内容按需出现。多文件输出提供入口和前后链接。说明实际做过的验证和仍影响阅读的限制，未运行的代码不声称已测试。
