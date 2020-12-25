# -*- coding:utf-8 -*-
# @Time : 2020/12/25 10:50 下午
# @Author : huichuan LI
# @File : test_search2.py
# @Software: PyCharm

from Search.Search_adavanced import *
from Search.problem import PeakFindingProblem


def test_hill_climbing():
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]])
    assert hill_climbing(prob) == (0, 3)
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    assert hill_climbing(prob) == (0, 2)
    prob = PeakFindingProblem((2, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    assert hill_climbing(prob) == (1, 3)


def test_simulated_annealing():
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]], directions4)
    sols = {prob.value(simulated_annealing(prob)) for _ in range(100)}
    assert max(sols) == 20
    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]], directions8)
    sols = {prob.value(simulated_annealing(prob)) for i in range(100)}
    assert max(sols) == 999


test_hill_climbing()
test_simulated_annealing()
