#-*- coding: utf-8 -*-

"""
10
3
2 4
7 8
6 9

10
3
1 3
5 7
8 9

10
5
1 1
1 2
1 3
1 4
7 8


3   1   4
1   1   5
"""
L = int(input())
N = int(input())
for p, k in map(int, input().split()):
    print(p, k)