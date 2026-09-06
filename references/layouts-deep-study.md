# Style C · Deep Study 语义布局

内容审查通过后读取。使用 [template-deep-study.html](../assets/template-deep-study.html) 的 CSS；它复用 A 的 `.section`、`.flow-box`、`.compare-box`、`.code-block`、`.summary-box` 接口，取消手写装饰。组件语义见 [components.md](components.md)。模板提供视觉原语，不提供固定文章大纲。

## 先选整篇的叙事形状

不要先数卡片或套章节名。根据主题的主要理解任务选择一种主导结构，必要时局部混合：

| 主导结构 | 适合内容 | 常见推进方式 |
| --- | --- | --- |
| 问题演进 | 算法、机制为何逐步出现 | 已有办法 → 具体缺口 → 新机制 → 新代价 |
| 执行路径 | 系统、协议、训练流水线 | 输入 → 状态变化 → 输出 → 故障与恢复 |
| 数学推导 | 概率、优化、理论算法 | 要求什么 → 关键变形 → 条件 → estimator／实现 |
| 方法对比 | 选型、家族方法、设计空间 | 共同任务 → 决策维度 → 分歧 → 适用边界 |
| 论文证据 | 论文精读、实验复现 | claim → 方法 → 图表证据 → 限制 → 可复现实验 |
| 代码调用链 | 框架、源码、工程实现 | 入口 → 数据结构 → 核心调用 → 生命周期 → 边界 |

同一主题可以先用一张总图建立整体，再沿推导或执行流深入。章节数、是否编号、是否有目录、总结卡和面试卡都由内容决定。big picture 必须出现，但可以是一段自然开篇、一张来源架构图或一个最小例子，不必单独做“全局”板块。

## 内容与布局同构

| 内容关系 | 布局选择 | 使用理由 |
| --- | --- | --- |
| 连贯解释 | section + p | 保持论证可连续阅读 |
| 原因 → 结果／依赖链 | flow-box（沿用 A L03） | 箭头表达真实关系，多分支分别列出 |
| 两种方案本质差异 | compare-box / compare-card（沿用 A L04） | 用共同维度说明选择依据 |
| 核心洞察 | study-card key-insight | 点出决定理解的量与变化 |
| 典型误解／错误边界 | study-card misconception-card | 写误解、正确机制和出错条件 |
| 条件分支 | mechanism-table | 展开条件、操作、结果、人话，再归纳 |
| 算法执行／阶段流转 | study-card process-card + ol | 输入、动作、输出及后续用途按执行顺序出现 |
| 关键公式 | formula-card | 公式和含义、符号、假设一起阅读 |
| 来源中的架构图、曲线、表格或界面 | source-figure | 保留结构或证据，带读图提示与出处 |
| 面试压缩 | study-card interview-card | 简短口述 + 追问，回链正文依据 |
| 承上启下 | study-card transition-card | 前文产物、具体缺口、本节补法 |
| 主线回收 | summary-box summary-card（沿用 A L13） | 归纳已解释的机制，不重复正文 |
| 选读扩展 | study-card optional-note | 指明额外用途和停止标准 |

普通段落不必加卡片。重要过渡可以直接写入正文；内容复杂时拆 section，不能为对齐卡片高度删解释。相邻板块若反复出现“标题 + 一段话 + 同色卡片 + 掌握标准”，应重新组织节奏，而不是换颜色伪装变化。

## C01 · 页面与章节

复制模板后替换 `STUDY CONTENT START` 到 `STUDY CONTENT END` 之间的画布示例，并更新 `<title>`。这些标记只帮助定位，不需要额外生成器。保留尾部公式状态提示及渲染脚本。

使用一个 h1、各节 h2、小节 h3。章节 ID 用稳定且唯一的短名；只有内容较长、读者会跨节跳转时才生成目录，并同步链接。默认头部只保留标题与可选领域标签。读者起点、学习目标、时间预算、资料范围和优先级计划是内部 brief，不显示为副标题、meta 行或顶部说明卡；用户明确要求导读时例外。多文件时在开头和文末放入口／前后篇链接，确保依赖方向可追踪。

```html
<section class="section" id="capacity">
  <h2 class="section-title"><span class="section-number">02</span>容量有限，先删谁？</h2>
  <p>在这里用具体问题推进解释。</p>
  <p class="mastery">掌握到这里：能手推一次淘汰，并解释选择依据。</p>
</section>
```

## C02 · 桥接、洞察与误解

同一基础卡片只换语义类名；标题也写明功能，不能只靠颜色辨别。

```html
<aside class="study-card transition-card">
  <h3 class="card-title">复用解决了重复计算，容量问题还在</h3>
  <p>缓存已经保存了结果，但内存有限。现在需要决定满了以后优先保留谁。</p>
</aside>
<aside class="study-card misconception-card">
  <h3 class="card-title">容易误解：最近插入不等于最近使用</h3>
  <p>解释具体反例和真实机制，不能只写“这是错的”。</p>
</aside>
```

`key-insight`、`optional-note`、`interview-card`、`solution-card` 使用同样结构。必要推导可以用 `derivation-note`，紫色不自动意味着 OPTIONAL，优先级由文字标识。

## C03 · 条件表与比较

```html
<div class="table-scroll" role="region" aria-label="条件与行为，可横向滚动" tabindex="0">
  <table class="mechanism-table">
    <caption>先展开条件，再判断行为</caption>
    <thead><tr><th scope="col">条件</th><th scope="col">实际操作</th><th scope="col">结果</th><th scope="col">一句人话</th></tr></thead>
    <tbody><tr><th scope="row">命中</th><td>移到最近使用端</td><td>访问次序更新</td><td>用过就重新排队</td></tr></tbody>
  </table>
</div>
<div class="compare-box compare-card">
  <h3 class="card-title">使用相同维度比较</h3>
  <div class="compare-row"><span class="compare-label">方案 A</span><p>它依据什么、改变什么、付出什么。</p></div>
  <div class="compare-row"><span class="compare-label">方案 B</span><p>在同样条件下为什么行为不同。</p></div>
</div>
```

较多维度用原生 table；只比较两个机制用 compare-row。窄屏允许表格局部横滚，页面本身不得横向溢出。表格后补模式归纳与准确的记忆句。

## C04 · 流程与代码

```html
<div class="study-card process-card">
  <h3 class="card-title">一次请求中的数据流</h3>
  <ol>
    <li><strong>查找。</strong>输入 key，得到是否命中及已保存的值。</li>
    <li><strong>处理。</strong>命中时更新次序；未命中时计算并保存结果。</li>
    <li><strong>返回。</strong>结果交给调用者，状态供下一次访问使用。</li>
  </ol>
</div>
<pre class="code-block"><code># 教学片段：命中也改变次序，否则会误删刚访问的条目。
cache.move_to_end(key)</code></pre>
```

代码使用真实缩进与 HTML 转义。不要将长代码拆到读者无法辨认上下文的卡片；正文给最小闭环，附录承接冗长实现。

## C05 · 来源图表

来源含关键视觉证据时读取 [visual-evidence.md](visual-evidence.md)。图片保存到成品旁的 `media/`，通过相对路径引用；图片本身可点击打开原尺寸。

```html
<figure class="source-figure">
  <a class="figure-frame" href="media/architecture.png" target="_blank" rel="noopener">
    <img src="media/architecture.png" alt="请求经过缓存、数据库并返回结果的数据流" loading="lazy" decoding="async">
  </a>
  <figcaption>
    <strong>读图：</strong>缓存未命中时才进入数据库路径。
    <span class="figure-credit">据 <a href="https://example.com/source">来源图 3</a> 截取</span>
  </figcaption>
</figure>
```

原始数据曲线优先保留原图；简单关系优先用 HTML/CSS 或内联 SVG 表达。不要引入图表库只为画一张静态关系图，也不要凭视觉估算重建实验数据。

## C06 · 公式

默认使用模板中的固定版本 KaTeX（CSS、主脚本、auto-render 三者一致），正文写 `\(...\)`，独立公式写 `\[...\]` 或 `$$...$$`。不启用单 `$` 分隔符，避免误识别金额和代码。外部脚本和字体是可选的视觉增强，正文静态存在。

```html
<p>先问：怎样从有限观测估计总体均值？</p>
<figure class="formula-card">
  <div class="formula-scroll" role="region" aria-label="样本均值公式，可横向滚动" tabindex="0">
    <div class="formula-body">\[\widehat{\mu}_n = \frac{1}{n}\sum_{i=1}^{n}x_i\]</div>
  </div>
  <figcaption>估计量：将 n 次观测平均。观测来自什么分布、是否独立，需要由当前主题说明。</figcaption>
</figure>
```

先解释问题，再给公式及身份，随后说明符号、整体含义与关键步骤。长式先用 `aligned` 等按逻辑换行，再允许局部横滚，不缩小到难以辨认。HTML 文本中的 `&`、`<`、`>` 仍需转义；KaTeX 里的对齐符在 HTML 源码写成 `&amp;`。不要把公式放在 pre/code 中让自动渲染器忽略。

模板在资源缺失、语法失败时保留可读 TeX 并显示提示；这属于降级，不能声称“公式排版 QA 通过”。无公式笔记可删掉 KaTeX 的 link/script、状态提示和尾部渲染脚本。严格离线且要求精排时，可在生成阶段预渲染 MathML，或按用户允许的打包方式内嵌必要资源；不能把“单 HTML”宣称为天然无外部依赖。

[KaTeX 浏览器接入](https://katex.org/docs/browser.html)与 [auto-render 文档](https://katex.org/docs/autorender.html)是渲染行为的维护依据。

## C07 · 阅读与打印

正文宽度约 800px，中文 sans-serif、标题 serif、代码 monospace；依赖字体不可达时使用系统回退。颜色由模板变量固定，参见组件手册。C 不使用固定页高、绝对定位正文、入场隐藏或翻页。

支持 320px 起的窄屏，代码／表格／公式可键盘聚焦后横滚；长公式和宽表打印前按内容换行或拆分，不能指望屏幕横滚在纸上可用。打印自然分页，不给整节设置不可拆分；最终仍需实际预览。
