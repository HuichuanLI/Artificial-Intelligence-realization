# -*- coding:utf-8 -*-
# @Time : 2020/12/26 9:26 下午
# @Author : huichuan LI
# @File : algorithm.py
# @Software: PyCharm

import numpy as np

import random


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


## alpha_beta_search 搜索

def alpha_beta_search(state, game):
    player = game.to_move(state)

    # Functions used by alpha_beta
    def max_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -np.inf
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = np.inf
        for a in game.actions(state):
            v = max(v, max_value(game.result(state, a), alpha, beta))
            if v >= beta:
                return v
            beta = max(beta, v)
        return v

    # Body of alpha_beta_search:
    best_score = -np.inf
    beta = np.inf
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action


def alpha_beta_player(game, state):
    return alpha_beta_search(state, game)


def minmax_player(game, state):
    return minmax_decision(state, game)


def random_player(game, state):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state)) if game.actions(state) else None
