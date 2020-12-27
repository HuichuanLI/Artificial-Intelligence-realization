# -*- coding:utf-8 -*-
# @Time : 2020/12/26 9:23 下午
# @Author : huichuan LI
# @File : test_game.py
# @Software: PyCharm


from Game import *

random.seed(666)

f52 = Fig52Game()


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


if __name__ == "__main__":
    test_minmax_decision()
    test_alpha_beta_search()