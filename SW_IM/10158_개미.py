#-*- coding: utf-8 -*-
"""
6 4
4 1
8

(0 1)


6 4
5 3
4

(3 1)
"""
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

def convert_coord(w, h, p, q):   # 문제에서 주어진 좌표를 원래대로 변경
    return (h-q, p)

def reverse_convert_coord(w, h, i, j):   # 원래 좌표를 문제에서 주어진 좌표로 변경
    return (j, h - i)

i, j = convert_coord(w, h, p, q)
print(f"i : {i},  j : {j}")

new_p, new_q = reverse_convert_coord(w, h, i, j)
print(f"new_p : {new_p},  new_q : {new_q}")  

di = [1, 1, -1, -1]     #down_right, down_left, up_right, up_left
cnt = 0
while cnt <= t:
    