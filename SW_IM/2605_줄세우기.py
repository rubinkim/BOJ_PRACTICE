#-*- coding: utf-8 -*-

"""
5
0 1 1 3 2

4 2 5 3 1
"""
import sys
input = sys.stdin.readline

N = int(input())
dataArray = [x for x in range(1, N+1)]
memory = []
head, current, pre = None, None, None


