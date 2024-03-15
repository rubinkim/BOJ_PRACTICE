#-*- coding: utf-8 -*-
"""
5
1 4
4 3 3 2 1
5 2 4 3 2 1
4 4 3 3 1
4 3 2 1 1
4 2 3 2 1
4 4 3 2 1
3 4 3 2
5 4 4 2 3 1
5 4 2 4 1 3

A B B A D


4
4 4 3 2 1
4 1 4 3 2
4 3 3 2 1
4 4 3 3 3
4 4 3 3 3
4 3 4 3 2
4 3 2 1 1
3 3 2 1

D B A A
"""

N = int(input())
for _ in range(N):
    card_dict = {1 : [0, 0], 2 : [0, 0], 3 : [0, 0], 4 : [0, 0]}
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))
    
    for x in A_lst:
        card_dict[x][0] += 1
    