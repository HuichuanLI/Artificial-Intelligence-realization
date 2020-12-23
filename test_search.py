# -*- coding:utf-8 -*-
# @Time : 2020/12/23 2:56 下午
# @Author : huichuan LI
# @File : test_search.py
# @Software: PyCharm


from Search.problem import GraphProblem
from Search.graph import UndirectedGraph

from Search.Search import *


def test_breadth_first_tree_search():
    assert breadth_first_tree_search(
        romania_problem).solution() == ['Sibiu', 'Fagaras', 'Bucharest']


if __name__ == "__main__":
    romania_map = UndirectedGraph(dict(
        Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
        Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
        Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
        Drobeta=dict(Mehadia=75),
        Eforie=dict(Hirsova=86),
        Fagaras=dict(Sibiu=99),
        Hirsova=dict(Urziceni=98),
        Iasi=dict(Vaslui=92, Neamt=87),
        Lugoj=dict(Timisoara=111, Mehadia=70),
        Oradea=dict(Zerind=71, Sibiu=151),
        Pitesti=dict(Rimnicu=97),
        Rimnicu=dict(Sibiu=80),
        Urziceni=dict(Vaslui=142)))

    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)

    print(breadth_first_tree_search(romania_problem).solution())
    print(depth_first_graph_search(romania_problem).solution())
    print(uniform_cost_search(romania_problem).solution())
