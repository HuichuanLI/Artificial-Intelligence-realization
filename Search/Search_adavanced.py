# -*- coding:utf-8 -*-
# @Time : 2020/12/25 10:46 下午
# @Author : huichuan LI
# @File : Search_adavanced.py
# @Software: PyCharm
from collections import deque
from .node import Node
from .utils import PriorityQueue
from .problem import *
import sys
import numpy as np



def hill_climbing(problem):
    """
    [Figure 4.2]
    From the initial node, keep choosing the neighbor with highest value,
    stopping when no neighbor is better.
    """
    current = Node(problem.initial)
    while True:
        neighbors = current.expand(problem)
        if not neighbors:
            break
        neighbor = argmax_random_tie(neighbors, key=lambda node: problem.value(node.state))
        if problem.value(neighbor.state) <= problem.value(current.state):
            break
        current = neighbor
    return current.state
