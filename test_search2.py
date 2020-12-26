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


def test_genetic_problem():
    # Queens Problem
    # 基因序列
    gene_pool = range(8)
    population = init_population(100, gene_pool, 8)

    def fitness(q):
        # 适应度函数
        non_attacking = 0
        for row1 in range(len(q)):
            for row2 in range(row1 + 1, len(q)):
                col1 = int(q[row1])
                col2 = int(q[row2])
                row_diff = row1 - row2
                col_diff = col1 - col2

                # 不是斜着的 45度和-135度
                if col1 != col2 and row_diff != col_diff and row_diff != -col_diff:
                    non_attacking += 1

        return non_attacking

    solution = genetic_algorithm(population, fitness, gene_pool=gene_pool, f_thres=25)
    assert fitness(solution) >= 25
    return solution


test_hill_climbing()

test_simulated_annealing()

print("result:" + " ".join(map(str, test_genetic_problem())))
