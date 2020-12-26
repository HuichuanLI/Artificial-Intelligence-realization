# -*- coding:utf-8 -*-
# @Time : 2020/12/26 9:26 下午
# @Author : huichuan LI
# @File : algorithm.py
# @Software: PyCharm

import numpy as np


# minmax 搜索
def minmax_decision(state, game):
    """通过给定game的当前的state"""

    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -np.inf
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = np.inf
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        return v

    print([min_value(game.result(state, a)) for a in game.actions(state)])
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))
