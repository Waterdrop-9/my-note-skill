# 学霸笔记 · 组件手册

按所选风格读取对应部分。以下原有文字样式、装饰与动画以 Style A 为主；Style B 的真实类名与片段见 [layouts-journal.md](layouts-journal.md)。Style C 读取文末的语义组件，CSS 以对应模板为准，不能假设 A 的所有类在 B/C 中可用。

## 文字样式

| 类名 | 效果 | 用途 |
|------|------|------|
| `.highlight` | 黄色高亮背景 | 关键术语、重点概念 |
| `.highlight-pink` | 粉色高亮背景 | 危险操作、警告内容 |
| `.highlight-green` | 绿色高亮背景 | 正面信息、安全状态 |
| `.highlight-orange` | 橙色高亮背景 | 注意事项、待办 |
| `.red-text` | 红色加粗 | 强调、警告、关键词 |
| `.blue-text` | 蓝色 | 信息、术语、链接 |
| `.green-text` | 绿色 | 安全、正面、确认 |
| `.purple-text` | 紫色 | 技术、代码、工具 |
| `.orange-text` | 橙色加粗 | 数据、统计、注意 |
| `.code-term` | 等宽字体 + 下划线 | 代码术语、命令、变量名 |
| `.underline-wavy` | 红色波浪下划线 | 重点强调 |
| `.double-underline` | 红色双下划线 | 最高强调 |
| `.check-mark` | 绿色加粗 ✓ | 正确、通过 |
| `.cross-mark` | 红色加粗 ✗ | 错误、失败 |
| `.star-mark` | 红色星号 ★ | 重要标记 |

## 标签

```html
<span class="badge">红色标签</span>
<span class="badge blue">蓝色标签</span>
<span class="badge green">绿色标签</span>
<span class="badge purple">紫色标签</span>
<span class="badge orange">橙色标签</span>
```

## 代码块

```html
<div class="code-block">
  <span class="code-comment"># 注释</span>
  <span class="code-keyword">import</span> os
  <span class="code-string">"字符串"</span>
</div>
```

## 装饰图标（Lucide SVG）

**禁止使用 emoji 作为图标。** 需要图标时，使用 Lucide SVG 图标库。

模板已引入 Lucide CSS：`https://unpkg.com/lucide-static@latest/font/lucide.min.css`

根据笔记主题选择合适的 Lucide 图标：

| 主题 | Lucide 图标 | CSS Class |
|------|------------|-----------|
| 安全/漏洞 | Shield Alert | `lucide-shield-alert` |
| Bug | Bug | `lucide-bug` |
| AI | Bot | `lucide-bot` |
| 锁/加密 | Lock | `lucide-lock` |
| 代码 | Code | `lucide-code` |
| 盾牌/防御 | Shield | `lucide-shield` |
| 警告 | Alert Triangle | `lucide-alert-triangle` |
| 灯泡/想法 | Lightbulb | `lucide-lightbulb` |
| 火/热点 | Flame | `lucide-flame` |
| 闪电/速度 | Zap | `lucide-zap` |
| 网络 | Network | `lucide-network` |
| 数据库 | Database | `lucide-database` |
| 文件 | File | `lucide-file` |
| 搜索 | Search | `lucide-search` |
| 设置 | Settings | `lucide-settings` |
| 用户 | User | `lucide-user` |

使用方式（放在 `.notebook` 内）：

```html
<div class="doodle" style="top:80px;right:80px;font-size:2rem;transform:rotate(15deg);opacity:0.15;"><i class="lucide-bug"></i></div>
```

> 图标大小通过 `font-size` 控制，颜色继承父元素的 `color`。

## 装饰元素控制

| 元素 | 默认显示 | 隐藏方式 |
|------|---------|---------|
| 胶带 `.tape` | 显示 | 删除对应 div |
| 回形针 `.paperclip` | 显示 | 删除对应 div |
| 咖啡渍 `.coffee-stain` | 显示 | 删除对应 div |
| 折角 `.folded-corner` | 显示 | 删除对应 div |
| 螺旋孔 `.spiral-holes` | 显示 | 删除对应 div |
| 涂鸦 `.doodle` | 隐藏 | 按需添加 |

## 动画系统

Style A 的内容元素使用 `.write-in` 类实现"书写出现"效果；Style C 正文静态显示，不依赖入场动画。

**动画延迟规则**：
- 标题：0.1s
- 副标题/日期：0.3s
- 第一个 section：0.5s 开始
- 每个 section 内部元素递增 0.1s
- section 之间递增 0.2-0.3s

示例：
```html
<div class="title write-in" style="animation-delay:0.1s">标题</div>
<div class="subtitle write-in" style="animation-delay:0.3s">副标题</div>
<div class="section">
  <div class="section-title write-in" style="animation-delay:0.5s">第一节</div>
  <div class="content write-in" style="animation-delay:0.6s">内容</div>
  <div class="side-note write-in" style="animation-delay:0.7s">旁注</div>
</div>
<div class="section">
  <div class="section-title write-in" style="animation-delay:0.9s">第二节</div>
  <div class="content write-in" style="animation-delay:1.0s">内容</div>
</div>
```

## Style C · 稳定语义与复用组件

技术内容先通过 [内容审查](content-checklist.md)，再按 [Deep Study 布局](layouts-deep-study.md) 映射。组件是表达已识别语义的词汇，不是输出清单。内容中出现需要强调的洞察、误区、流程或回顾时，主动选用对应表达；不要求固定组合或每节都有卡片，也不能把“按需”执行成全文省略视觉锚点。C 的提示卡共享 `.study-card` 基础样式，不为每种语义重复实现容器。

| 语义 | 类名 | 颜色／结构 | 复用关系 |
| --- | --- | --- | --- |
| 结构说明／知识整理 | `.study-card` | 蓝色 | 基础提示卡；普通解释用段落 |
| 承上启下 | `.study-card.transition-card` | 青色 | 同一基础卡片 |
| 关键洞察 | `.study-card.key-insight` | 橙色 | 同一基础卡片 |
| 误解／重要边界 | `.study-card.misconception-card` | 红色 | 同一基础卡片 |
| 面试压缩 | `.study-card.interview-card` | 红色 | 同一基础卡片；回答回链正文 |
| 选读扩展 | `.study-card.optional-note` | 紫色 | 同一基础卡片 |
| 必要高级推导 | `.study-card.derivation-note` | 紫色 | 同一基础卡片；不因此降为选读 |
| 解法／正面结果 | `.study-card.solution-card` | 绿色 | 同一基础卡片 |
| 执行过程 | `.study-card.process-card` + `ol` | 青色／有序步骤 | 原流程语义，原生列表 |
| 原因／依赖链 | `.flow-box` / `.flow-item` / `.flow-arrow` | 青色 | 复用 A L03 的接口 |
| 本质差异 | `.compare-box.compare-card` / `.compare-row` | 蓝色 | 复用 A L04；compare-card 是语义别名 |
| 主线回顾 | `.summary-box.summary-card` | 蓝色 | 复用 A L13；summary-card 是语义别名 |
| 精确公式 | `.formula-card` / `.formula-scroll` | 中性暖灰 | 新增公式与解释容器 |
| 来源视觉证据 | `.source-figure` / `.figure-frame` / `.figure-credit` | 中性边框／原图色 | 原图、截图或忠实改绘，规则见 visual-evidence |
| 条件分支 | `.table-scroll` > `.mechanism-table` | 蓝色表头 | 原生 table，窄屏局部横滚 |
| 代码 | `pre.code-block` > `code` | 深色／等宽 | 复用原代码接口，保留缩进 |

颜色功能稳定，标题同时明确写出“关键洞察”“易错点”“成立条件”“执行流程”“面试回答”等用途。红色边界与面试、紫色推导与扩展等共色功能必须由文字区分。

强调有轻重：短提示用 `.study-label` 配语义类（如 `key-insight`），连续推导的关键条件可用 `.study-note` 配语义类保留边线与留白；需要独立停读、复习回找的解释用 `.study-card`。三者共享既有语义色，不另建主题配色。标题／粗体也可以承担强调，普通段落不用套蓝卡。

学习提示属于读者界面，和内部 brief 分开：局部显示“关键洞察／易错点／成立条件／追问／选读”；优先级用 `.priority.core`、`.priority.follow-up`、`.priority.optional`，可附“核心／追问／选读”中文。按学习价值分级，紫色必要推导仍可为 CORE；读者画像、默认目标、时间预算、资料范围、生成策略继续隐藏，正常出处和图注保留。

标题、正文、代码字体及六组语义色统一在 [Style C 模板](../assets/template-deep-study.html) 的 `:root` 中维护。不要为了视觉变化随意换颜色，或给每段添加提示卡。需要更多视觉变化时优先改变信息形状，例如来源图、流程、推导、对比或连续正文，而不是继续堆不同颜色的盒子。


### 自测问答：先作答，再揭晓

HTML 自测题与面试问答使用独立的原生 `details.qa-answer`，省略 `open`，答案默认折叠。问题完整显示在折叠区域外；`summary` 是“查看答案／收起答案”控件，每题独立开合，可同时展开多题。复用现有卡片与标签，不把答案要点泄露在题目旁。正文的必要解释、推导与边界保持可见；这里只隐藏已在正文讲过的自测答案。

```html
<aside class="study-card interview-card">
  <h3 class="card-title">自测</h3>
  <div class="qa-item">
    <p class="qa-question">缓存容量足够，为什么仍可能频繁未命中？</p>
    <details class="qa-answer">
      <summary><span class="qa-show">查看答案</span><span class="qa-hide">收起答案</span></summary>
      <div class="qa-body"><p>容量只是一个条件；还要结合访问局部性、淘汰策略与失效行为判断。回答应回到正文已解释的机制。</p></div>
    </details>
  </div>
</aside>
```

Style C 模板提供控件样式与打印处理：打印时展开答案，结束后恢复原状态。保留原生键盘交互、展开标记和焦点样式，无需框架。折叠中的公式仍随正文进行初始化；检查展开后的公式、代码和表格。其他 HTML 风格生成自测时复用这一结构，配色沿用所选风格。
