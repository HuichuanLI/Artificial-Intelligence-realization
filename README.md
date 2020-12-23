# -Artificial-Intelligence-realization
Python code for the book Artificial Intelligence: A Modern Approach. You can use this in conjunction with a course on AI, or for study on your own. 

# 搜索

## 无信息搜索

- DFS
- BFS
- Uniform 
- DFS limited
- DFS iterative
- Bidirection Searching(to do)


## 有信息搜索


也被称为启发式搜索

这类策略采用超出问题本身定义的、问题特有的知识，因此能够找到比无信息搜索更有效的解

一般使用如下函数中的一个或者两个：评价函数，记f(n),用于选择一个节点进行扩展；启发函数，记h(n),作为f的一个组成部分

评估函数看做是代价估计，因此评估值最低的节点被优先扩展，最佳优先图搜索的实现与一致性搜索类似

对f的选择决定了搜索策略

一般采用最佳优先搜索

实现方式：与一致代价搜索相同，然而最佳优先算法用f(n)替代g(n)来整理队列

搜索策略：一个节点被选择扩展是基于评价函数f(n)

大多数最佳优先算法还包含一个启发函数h(n)

h(n) = 从节点n到目标的最低径路代价估计

- 贪婪搜索
- A*搜索