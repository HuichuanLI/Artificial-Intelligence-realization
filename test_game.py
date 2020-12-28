# -*- coding:utf-8 -*-
# @Time : 2020/12/26 9:23 下午
# @Author : huichuan LI
# @File : test_game.py
# @Software: PyCharm


from Game import *

random.seed(666)

f52 = Fig52Game()
ttt = TicTacToe()


def gen_state(to_move='X', x_positions=[], o_positions=[], h=3, v=3):
    """给予一个游戏状态，X在棋盘上的状态，O在棋盘上的位置"""

    moves = set([(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]) - set(x_positions) - set(o_positions)
    moves = list(moves)
    board = {}
    for pos in x_positions:
        board[pos] = 'X'
    for pos in o_positions:
        board[pos] = 'O'
    return GameState(to_move=to_move, utility=0, board=board, moves=moves)


def test_minmax_decision():
    print(minmax_decision('A', f52) == 'a1')
    print(minmax_decision('B', f52) == 'b1')
    print(minmax_decision('C', f52) == 'c1')
    print(minmax_decision('D', f52) == 'd3')


def test_alpha_beta_search():
    assert alpha_beta_search('A', f52) == 'a1'
    assert alpha_beta_search('B', f52) == 'b1'
    assert alpha_beta_search('C', f52) == 'c1'
    assert alpha_beta_search('D', f52) == 'd3'

    state = gen_state(to_move='X', x_positions=[(1, 1), (3, 3)],
                      o_positions=[(1, 2), (3, 2)])

    # print(alpha_beta_search(state, ttt))
    # == (2, 2)

    state = gen_state(to_move='O', x_positions=[(1, 1), (3, 1), (3, 3)],
                      o_positions=[(1, 2), (3, 2)])
    assert alpha_beta_search(state, ttt) == (2, 2)

    state = gen_state(to_move='O', x_positions=[(1, 1)],
                      o_positions=[])
    assert alpha_beta_search(state, ttt) == (2, 2)

    state = gen_state(to_move='X', x_positions=[(1, 1), (3, 1)],
                      o_positions=[(2, 2), (3, 1)])
    assert alpha_beta_search(state, ttt) == (1, 3)


if __name__ == "__main__":
    test_minmax_decision()
    test_alpha_beta_search()
