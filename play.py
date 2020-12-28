# -*- coding:utf-8 -*-
# @Time : 2020/12/28 10:16 上午
# @Author : huichuan LI
# @File : play.py
# @Software: PyCharm
from Game import minmax_decision, alpha_beta_player, random_player, TicTacToe, Gomoku

from test_game import gen_state

import subprocess as sp

ttt = TicTacToe()

x_pos = []
o_pos = []

print("TicTacToe gamer vs computer")
print("1 random 2 pro 3 expert")

choose = input("input:")

while choose not in ['1', '2', '3']:
    print("error")
    choose = input("input:")

choose = int(choose)
print("输入你的位置 比如：1,2:")

while True:
    state = gen_state(to_move='O', x_positions=x_pos,
                      o_positions=o_pos, h=ttt.h, v=ttt.v)
    ttt.display(state)
    position = input("位置:")
    while "," not in position:
        print("重新输入")
        position = input("位置:")
    a, b = map(int, position.split(","))
    # clear_the_screen = sp.call('clear', shell=True)  # Linux
    board = ttt.result(state, (a, b))
    while board == state:
        print("重新输入")
        position = input("位置:")
        a, b = map(int, position.split(","))
        board = ttt.result(state, (a, b))

    o_pos.append((a, b))
    state = gen_state(to_move='X', x_positions=x_pos,
                      o_positions=o_pos, h=ttt.h, v=ttt.v)

    if ttt.compute_utility(board.board, (a, b), 'O'):
        ttt.display(state)
        print("you win")
        exit()

    if choose == 1:
        a, b = random_player(ttt, state)
    elif choose == 2:
        a, b = minmax_decision(state, ttt)
    else:
        a, b = alpha_beta_player(ttt, state)
    x_pos.append((a, b))
    state = gen_state(to_move='O', x_positions=x_pos,
                      o_positions=o_pos, h=ttt.h, v=ttt.v)
    board = ttt.result(state, (a, b))

    if ttt.compute_utility(board.board, (a, b), 'X'):
        ttt.display(state)
        print("you lose")
        exit()
