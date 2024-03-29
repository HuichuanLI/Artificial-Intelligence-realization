# Artificial-Intelligence-realization

Python code for the book Artificial Intelligence: A Modern Approach. You can use this in conjunction with a course on
AI, or for study on your own.

# 搜索算法

## 无信息搜索

- DFS
- BFS
- Uniform
- DFS limited
- DFS iterative
- Bidirection Searching(to do)

![八皇后问题](./photo/2.png)

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

目前实现了

- 罗马尼亚问题
- n皇后问题

![八皇后问题](./photo/1.png)

## 超越经典搜索

经典搜索：系统地探索问题的空间

    该系统性是由以下方法得到：在内存中保持一条或多条路径，并且在沿着该路径的每个点上记录哪些已被探索过；目标找到时，该路径也就构成问题的一个解
    然而在许多问题中到达目标的路径是无关紧要的

局部搜索是一种不同于经典搜索的算法，它不介意什么路径

    局部搜索算法使用一个当前节点（而不是多条路径），并且通常仅移动到该节点相邻的节点，通常，搜索后不保留该路径
    局部搜索有2个优点：使用很少内存；在大的或者无限（连续）状态空间中，能发现合理的解

- 爬山法
- 模拟退火
- 局部束搜索[未完成]
- 遗传算法
- ACO 蚁群算法

遗传算法的一些要素是1960年代提出

    它是一种模仿自然选择过程的搜索启发式算法
    
    该算法是随机束搜索的一个变型，其中后继节点是由两个父辈状态的组合而不是修改单一状态生成的
    
    其处理过程是有性繁殖而不是无性繁殖
    
    属于进化算法的大分类
    
    该算法采用自然进化所派生的技法来生成优化问题的解，例如：遗传、突变、选择以及杂交
    
    该算法开始时具有一组k个随机生成的状态，称为种群，每个单个状态称为个体，每个个体通常由一组字符一般为01字符串，如八皇后的个体

![八皇后问题](./photo/3.png)

## 对抗搜索(游戏问题) adversarial search

零和博弈

    经典例子：囚徒困境   相关困境理论
    
    博弈有趣但很难解决
    
    博弈，像现实世界，当无法算计出最优决策时，需要决策理论
    
    超过人类的是完备性信息，未超过人类的往往是随机游戏

![八皇后问题](./photo/5.png)

- minmax算法
- alpha-beta 算法

实现了：TicTacToe,connect4,komodu

![八皇后问题](./photo/6.png)


    Minimax algorithm can select optimal moves by a depth-first enumeration of game tree.
    
    Minimax算法可以通过博弈树的深度优先计算选择最佳移动。
    
    
    
    Alpha–beta algorithm achieves much greater efficiency by pruning irrelevant subtrees.
    
    Alpha–beta算法通过剪掉不相关子树来得到更高的效率。
    
    
    
    Heuristic evaluation function is useful for imperfect real-time decisions of games.
    
    启发式评价函数对于博弈的不完全实时决策很有效。
    
    
    
    Stochastic game is a dynamic game with probabilistic transitions.
    
    随机博弈是具有概率转换的动态博弈。


