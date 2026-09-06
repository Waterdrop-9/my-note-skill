# note-skill

Deep Technical Study Notes + Visual Note Generator

一个供 AI Agent 使用的学习笔记 Skill。保留原来的学霸手写笔记与皮革手账，新增 **Style C · Deep Study**：先组织知识和教学逻辑，再生成适合长文阅读的 HTML。

输入技术主题时，它会先弄清楚：已有方法解决了什么、还缺什么、新概念为何现在出现、具体改变哪个环节、代价是什么。正文讲通之后，才压缩面试回答和选择视觉组件。

## 三种风格

| 风格 | 适用场景 | 保留／新增的呈现能力 | 预览模板 |
| --- | --- | --- | --- |
| A · 学霸笔记 | 手写笔记、轻量知识总结、课堂与科普 | 米黄横线纸、螺旋装订、胶带／咖啡渍、write-in 入场 | [template.html](assets/template.html) |
| B · 手账 / Journal | 明确偏好皮革本、分册记录、翻页阅读 | 皮革封面、金属环、键盘／点击／按钮翻页 | [template-journal.html](assets/template-journal.html) |
| C · Deep Study | AI、LLM、RL、Transformer、操作系统、编译、数据库、算法、数学等技术学习 | 暖白长文、公式与代码、来源图表、按内容动态编排 | [template-deep-study.html](assets/template-deep-study.html) |

技术系统学习默认 C，轻量或非技术视觉笔记默认 A，手账／翻页请求选择 B。用户指定优先；技术深度与风格独立，深度内容也可以用 A/B。仅要求美化原文时，保留内容范围，不强加推导和面试题。

**完整示例：** [缓存为什么还需要淘汰策略？](examples/deep-study-cache.html)。下载后用浏览器打开，可检查实际知识链、条件展开、公式、最小实现、边界与口述压缩；不只是组件展示页。

## Deep Study 多做了什么

| 能力 | 对生成行为的具体约束 |
| --- | --- |
| Problem-driven | 先建立任务、朴素办法和真实缺口，核心概念先回答为什么存在 |
| Knowledge Chain | 规划 Previous / Gap / Bridge / Mechanism / Tradeoff / Next；前文提出的问题，后文主动收回 |
| Why before How | 定义、公式、实现之前先解释问题与直觉 |
| Mechanism-aligned analogy | 比喻映射具体操作，改变条件后仍能预测行为；不能替代数学解释 |
| Technical depth | 保留关键推导，区分定义／估计／近似，对齐公式—流程—变量—代码 |
| Interview-aware | CORE / FOLLOW-UP / OPTIONAL 分层；面试回答是正文的压缩，有理由和边界 |
| Content QA | 正文在排版前通过内容 P0 审查，失败先改正文 |
| Visual evidence | 关键架构图、曲线、表格或界面可直接复用／截取并本地保存，图注说明来源和读法 |
| Semantic layout | 先选问题演进、执行路径、数学推导、方法对比、论文证据或代码调用链，再按局部语义选择组件 |

“提高稳定性”“提升效率”不算解释完成：要继续说明哪个量或步骤改变了，为什么有效，以及不这样做会怎样。难但决定理解的内容不能因为难而放进选读；独立路线也不会被硬写成一条历史进化链。

## 安装与使用

将整个仓库放入所用 Agent 支持的 skills 目录，确保 `SKILL.md`、`assets/` 与 `references/` 的相对路径保持一致。沿用原项目的 WorkBuddy 安装方式：

```bash
git clone https://github.com/Unclecheng-li/note-skill.git ~/.workbuddy/skills/note-skill
```

也可下载后复制仓库目录，再按宿主要求重新加载 skills。本项目仍是静态 Skill 资源，不需要安装前端框架。技能标识规范化为 `note-skill`，描述保留“学霸笔记”“手写笔记”等自然语言入口。

直接描述需求即可，无需自己写完整大纲：

```text
帮我生成一份 PPO 学习笔记。我懂基础 Policy Gradient，
但没真正理解 importance sampling、GAE 和 PPO clip。
目标是算法面试。请用 Deep Study HTML。
```

预期先从已有 Policy Gradient 的能力和缺口组织主线：优势估计解决什么、旧数据复用为何需要校正、ratio 有什么问题、clip 改变什么。GAE 与数据校正可以是配合工作的分支，不会把所有名词编成必然的历史继承。核心公式、分支条件、冻结量与梯度路径应出现在正文，面试区回链正文解释。

```text
我懂字典和基本复杂度，第一次系统学缓存淘汰。
给我约 20 分钟能读完的笔记，重点理解 LRU 为什么命中也要改次序。
```

```text
把下面的旅行记录做成 Style B 皮革手账，保留原文。
```

默认读者有基础编程／数学知识，第一次系统学习当前主题；默认目标是建立完整 picture、掌握机制、接住面试追问。这些信息只指导生成，不会作为“已有基础／目标／资料范围”显示在页面头部。默认输出单 HTML，也尊重明确指定的 Markdown。指定来源时遵守来源范围，缺失或冲突的信息会注明。

## 工作流与资源

**Understand → Research / Grounding → Build Knowledge Chain → Depth Planning → Draft → Content Audit → Semantic Layout Mapping → Render HTML → Final QA**

[SKILL.md](SKILL.md) 负责触发、默认值、流程、加载时机和交付要求；详细规则按阶段加载，不把整套手册一次塞进上下文。

| Reference | 何时使用 |
| --- | --- |
| [grounding.md](references/grounding.md) | 阅读资料，分清事实、教学示例和风格参考 |
| [visual-evidence.md](references/visual-evidence.md) | 选择、提取、截图、改绘和引用来源关键图表 |
| [knowledge-chain.md](references/knowledge-chain.md) | 组织章节、桥接、分支与问题回收 |
| [interview-priority.md](references/interview-priority.md) | 分配深度、学习 ROI、停止标准与面试压缩 |
| [technical-depth.md](references/technical-depth.md) | 公式、关键推导、估计量、阶段／变量／代码映射 |
| [pedagogy.md](references/pedagogy.md) | 补初学者断点、具体例子、机制比喻与分支归纳 |
| [exemplars.md](references/exemplars.md) | 理解参考写法为何有效；跨主题验收场景 |
| [content-checklist.md](references/content-checklist.md) | 草稿 P0 内容审查；失败返回正文 |
| [layouts.md](references/layouts.md) / [layouts-journal.md](references/layouts-journal.md) | 保留 A 的 18 种布局与 B 的 10 种布局 |
| [layouts-deep-study.md](references/layouts-deep-study.md) | C 的语义布局、公式、长文与打印规则 |
| [components.md](references/components.md) | 原组件及 C 语义组件，区分各风格可用类 |
| [checklist.md](references/checklist.md) | 通用视觉检查及 A/B/C 专项 QA |

`笔记.md` 是本次改造的教学设计 exemplar，其方法已提炼入 references。使用 Skill 不依赖它的再次提供，也不能用它支持其他主题的技术事实。仓库中用户提供的原始参考资料保持原样，`assets/` 才是生成入口。

## Style C 的视觉结构

正文约 800px 宽，暖白背景，Noto Serif SC 标题、Noto Sans SC 中文正文、JetBrains Mono 代码，均有系统字体回退。没有固定页高或入场隐藏。

| 颜色 | 稳定语义 | 组件例子 |
| --- | --- | --- |
| 蓝 | 解释与结构 | compare-card、summary-card、表头 |
| 青 | 承上启下与流程 | transition-card、process-card、flow-box |
| 橙 | 核心洞察 | key-insight |
| 红 | 误解、警告与面试 | misconception-card、interview-card |
| 绿 | 解法与正面结果 | solution-card |
| 紫 | 高级推导与扩展 | derivation-note、optional-note |

所有提示卡共用基础样式；流程、对比、代码、总结沿用原接口，并新增带图注和来源的 figure。模板只提供视觉原语，不规定文章大纲：目录、编号、导读、总结和面试卡都按内容与目标选用。颜色配合文字标题，不用颜色代替优先级判断。公式采用固定版本 KaTeX，宽表、公式、代码和来源大图在窄屏局部滚动或打开原尺寸。

默认 HTML 的样式与应用脚本内联，字体、图标与 KaTeX 来自 CDN；**单文件不等于完全离线**。C 在资源缺失／禁用 JS 时保留静态正文和 TeX，但降级不算公式精排通过。严格离线需求可预渲染 MathML 或按需打包资源，不为普通输出新增构建系统。KaTeX 接入方式见其 [官方文档](https://katex.org/docs/autorender.html)。

## QA 与本地预览

两道独立门槛：内容审查先检查为什么、桥接、机制、推导、边界和来源；视觉审查再检查阅读、渲染和交互。适用的内容 P0 必须通过；不适用项写清原因，不能用排版或关键词计数冒充理解验证。

内容太长时，依次考虑增加页面、拆 section、拆多个 HTML、迁移低优先级扩展。**不为统一页高删除关键推导、原因解释、初学者断点、必要示例或边界。** B 当前页会撑开皮革容器，C 自然长文阅读。

浏览器直接打开模板／示例，或在仓库运行：

```bash
python3 -m http.server 8000
```

打开 `http://localhost:8000/examples/deep-study-cache.html`。检查桌面、窄屏、目录跳转、公式、代码与打印；B 还需检查翻页及长页。

仓库提供不需要第三方 Python 包的维护检查：

```bash
python3 scripts/check.py
python3 scripts/check_example.py
```

前者检查维护文件的本地引用、HTML 标签／锚点、Markdown 围栏，并在 Node 可用时检查内联 JS 语法；后者从实际示例 HTML 提取代码，验证淘汰次序、命中行为、零容量、失败保留及循环扫描反例。它们不替代浏览器预览或教学质量审查，也不修改用户原始参考文件。

本轮不引入通用渲染引擎、自动打分器或大规模评测框架。后续最值得做的是用多个领域的真实请求独立试生成，依据暴露的教学问题迭代规则。

## 许可

保留原项目的 [MIT License](LICENSE)。
