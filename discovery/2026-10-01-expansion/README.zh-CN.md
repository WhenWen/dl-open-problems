# 第二轮：扩大深度学习开放问题候选集

本轮执行 **61 次查询、46 个查询批次，筛选 94 篇原始论文，提出 40 个新候选**，覆盖 24 个细分领域。两轮合计 111 次查询、151 篇筛选论文、66 条线索（63 条拟新增候选、3 条已有问题补充）。这些是可审查的研究提议，**不是 66 个已证实无人解决的问题**。

[英文证据与具体检验](README.md) · [逐条结构化记录](candidates.json) · [覆盖与遗漏](coverage.md) · [检索原文](search-manifest.json) · [被否定或收窄的表述](triage.json)

每条记录区分作者报告的结果、我们提出的问题、需要核对的边界和可区分解释的实验。当前阅读深度为摘要筛选；尚未逐篇核对证明、完整实验协议和后续引用。新论文的 claim 也不等于公认结论。

| ID | 问题 | 已有理解 | 下一步要核对的边界 |
| --- | --- | --- | --- |
| [027](README.md#disc-20261001-027) | 非对比学习为什么发生部分维度坍缩 | 已有线性平衡点、归一化动力学分析 | 有限非线性模型中，哪些方向会保留有用语义？ |
| [028](README.md#disc-20261001-028) | 数据增强何时保留、何时破坏语义 | 已有 augmentation overlap 与下游误差理论 | 类间碰撞、类别不均衡时能否提前选增强强度？ |
| [029](README.md#disc-20261001-029) | MAE 的 masking rate 如何随数据改变 | 已有层次潜变量恢复理论 | 能否从可观测冗余预测新领域的最佳 mask？ |
| [030](README.md#disc-20261001-030) | 鲁棒性与准确率的 tradeoff 从哪里来 | 有误差分解，也有无内在冲突的例子 | 区分 Bayes 冲突、有限样本成本和优化成本。 |
| [031](README.md#disc-20261001-031) | 有限训练环境是否足以识别不变性 | 已有 IRM 成功条件与失败反例 | 能否判断新 shift 属于可识别范围？ |
| [032](README.md#disc-20261001-032) | 何时应该做 test-time adaptation | 已有先验偏移校正与相关性对齐方法 | 条件分布也变化时，何时更新、何时放弃更新？ |
| [033](README.md#disc-20261001-033) | GNN rewiring 如何兼顾传递与可区分性 | 已有信息收缩、局部几何与特定优化难度分析 | 全局图指标改善是否真的改善任务 loss？ |
| [034](README.md#disc-20261001-034) | heterophily 何时反而有帮助 | 已有邻域分布、度数、噪声的可分性分析 | 复杂真实图上能否提前选择聚合方式？ |
| [035](README.md#disc-20261001-035) | 截断图位置编码如何影响泛化 | 已有稳定性与截断表达力结果 | 有限计算预算下，如何预测跨图大小迁移？ |
| [036](README.md#disc-20261001-036) | 如何预报 loss of plasticity | 已有 spectral collapse 与动力系统陷阱解释 | 区分机制，并预测恢复新任务学习能力的干预。 |
| [037](README.md#disc-20261001-037) | offline RL 的 ensemble uncertainty 是否可靠 | 线性/表格和部分泛化保证已存在 | 神经表示错误时，悲观估计能否校准实际控制风险？ |
| [038](README.md#disc-20261001-038) | world model 哪些误差真正影响规划 | 已有累计误差方法与 loss 反例 | 能否由局部误差预测安全 rollout horizon？ |
| [039](README.md#disc-20261001-039) | 稀疏网络存在为何不等于容易找到 | 有彩票子网络实验、rewinding 与存在定理 | 能否在早期预测可发现性，并计入搜索总成本？ |
| [040](README.md#disc-20261001-040) | distillation 为什么模仿更好却未必泛化更好 | 已有梯度/几何解释和 fidelity 反例 | 哪些 teacher/student/data 特征预测实际收益？ |
| [041](README.md#disc-20261001-041) | LoRA 需要多大的有效 rank | 已有表达力界和共享 rank 方法 | 如何提前预测任务所需的逐层 rank 与可优化性？ |
| [042](README.md#disc-20261001-042) | modality gap 的多个解释如何统一 | 初始化、温度、错配数据、目标函数均有研究 | 能否在独立干预下预测 gap 和下游性能？ |
| [043](README.md#disc-20261001-043) | 多一个模态何时反而学不好 | 已有信息收益与 modality competition 理论 | 能否提前预测哪些模态会被忽略？ |
| [044](README.md#disc-20261001-044) | PINN 何时因为优化而失败 | 已有梯度失衡、数值刚性与病态 penalty 分析 | 能否跨 PDE 预测需要哪种训练干预？ |
| [045](README.md#disc-20261001-045) | neural operator 为什么跨分辨率失效 | 已有 aliasing 界、表示等价与离散化限制 | 能否分解并预测新网格和长 rollout 误差？ |
| [046](README.md#disc-20261001-046) | 有限预算下合成数据反馈是否稳定 | 替换、累积、固定子集已有不同结论 | 保留、过滤、fresh data 如何共同控制长期退化？ |
| [047](README.md#disc-20261001-047) | DP clipping/noise 如何影响 utility | 隐私 accounting 与高效 clipping 已成熟部分 | 能否从小实验预测不同规模和隐私预算的 utility？ |
| [048](README.md#disc-20261001-048) | ensemble diversity 何时改善 uncertainty | 已有 shift benchmark 与 uncertainty-aware tuning | 能否跨训练设置预测校准收益而非事后相关？ |
| [049](README.md#disc-20261001-049) | 少量目标标签能支持什么条件覆盖 | 已有条件保证和不可能性/样本复杂度结果 | 指定 shift 与稀有群组后，最小标签预算是多少？ |
| [050](README.md#disc-20261001-050) | sharpness 如何成为可迁移的泛化指标 | 已有重参数化反例和现代 benchmark | 能否尊重对称性并预测干预后的风险变化？ |
| [051](README.md#disc-20261001-051) | 非可分、大步长下 implicit bias 是什么 | 可分线性极限与受限大步长结果已知 | 有限时间、Adam、特征学习如何改变 margin 与风险？ |
| [052](README.md#disc-20261001-052) | MoE balance 与 specialization 如何共同演化 | 已有 routing 动态模型和 balancing 改进 | 能否提前预测 balancing schedule 的 loss 效果？ |
| [053](README.md#disc-20261001-053) | 初始 dynamical isometry 能维持多久 | 已有极限理论和有限网络构造 | 训练后的谱演化是否决定稳定性和学习速度？ |
| [054](README.md#disc-20261001-054) | client drift 如何决定通信与本地步数 | SCAFFOLD 等已有收敛分析 | 能否用可测统计量预测非 IID 深度训练曲线？ |
| [055](README.md#disc-20261001-055) | SAE 特征是否可识别且有因果意义 | 特定 sparse-mixture 模型已有恢复保证 | 相关概念、字典大小和训练漂移下是否稳定？ |
| [056](README.md#disc-20261001-056) | GAN 局部稳定为何仍可能漏掉 mode | 已有局部稳定性和极限环分析 | 哪些动态指标能提前预测整体 mode coverage？ |
| [057](README.md#disc-20261001-057) | consistency model 的质量/计算曲线 | 已有少步生成与分布误差保证 | 能否用可测训练误差预测现实模型的性能损失？ |
| [058](README.md#disc-20261001-058) | data attribution 能否预测真正 retraining | 已有 influence 失败与几何稳定性工作 | 稳定排名是否能预测有限数据删除的实际效应？ |
| [059](README.md#disc-20261001-059) | 如何低成本验证 unlearning 接近重训 | 已有多维评测和 uncertainty 指标 | 连续删除时，如何验证分布等价而非只压制回答？ |
| [060](README.md#disc-20261001-060) | 什么决定 compositional generalization | 已有架构方法及 entropy-based 预测 | 哪些结论能跨组合深度、primitive coverage 与领域？ |
| [061](README.md#disc-20261001-061) | likelihood/typicality 能否检测语义 OOD | 已有典型集与 score test 方法 | 低层统计量匹配时，检测 power 如何变化？ |
| [062](README.md#disc-20261001-062) | 哪些模型经过 alignment 后可以 merge | 已有 permutation 与奇异向量分析 | 能否提前预测多任务保留和 interpolation barrier？ |
| [063](README.md#disc-20261001-063) | 哪些最弱假设支持有用的 disentanglement | 无约束不可能性与稀疏混合正面结果已知 | 近似而非精确假设下，识别与下游收益是否稳定？ |
| [064](README.md#disc-20261001-064) | 不完美对称性应该施加多少 equivariance | 已有近似与 relaxed equivariance 方法 | 如何由数据预测归纳偏置强度，而不是逐项试？ |
| [065](README.md#disc-20261001-065) | 长尾问题何时只需修 classifier | 已有 logit adjustment 与 feature geometry 理论 | 何时信息已在 feature 中丢失，必须重新学表示？ |
| [066](README.md#disc-20261001-066) | 什么数据适合树、普通 NN 或 tabular foundation model | TabPFN 已改变部分旧 benchmark 结论 | 如何把先验失配、数据结构与摊销计算放进预测？ |

这轮最值得精读的一组是：部分 collapse、modality gap、plasticity、图 rewiring、neural operator 跨分辨率、合成数据反馈和 SAE identifiability。它们都有明确的既有解释，也有容易混淆的适用条件，适合把“理论—实验—新 setting 的缺口”写成可检验的问题。这个排序是审计建议，不是已经确认的研究价值排名。

“不重不漏”在这里落实为可追溯流程：永久 ID、相邻问题的区别、跨批次碰撞检查、逐领域缺口与下一条检索路线。自动检查只能保证记录一致；语义去重和文献是否已有答案仍需人工与全文审查。语音、机器人、多智能体、SSM、检索增强、主动学习等方向仍需专门检索，不能从此轮未出现推断它们没有合适问题。
