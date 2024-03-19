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

di = [1, 1, -1, -1]     #down_right, down_left, up_right, up_left
dj = [1, -1, 1, -1]
dr = 2                  # up_right
cnt = 0
while cnt < t:
    ni, nj = i + di[dr],  j + dj[dr]
    if 0 <= ni <= h and 0 <= nj <= w:
        cnt += 1
        i, j = ni, nj
    if i == 0 and dr == 2:     # 천장에 부딪혔을때 화살표 방향이 up_right이라면,  화살표 방향을 down_right으로 변경해라.
        dr = 0
    if i == 0 and dr == 3:     # 천장에 부딪혔을때 화살표 방향이 up_left라면,  화살표 방향을 down_left로 변경해라.
        dr = 1
    if i == h and dr == 0:     # 바닥에 부딪혔을때 화살표 방향이 down_right라면,  화살표 방향을 up_right로 변경해라.
        dr = 2
    if i == h and dr == 1:     # 바닥에 부딪혔을때 화살표 방향이 down_left라면,  화살표 방향을 up_left로 변경해라.
        dr = 3
    if j == 0 and dr == 1:     # 왼쪽옆면에 부딪혔을때 화살표 방향이 down_left라면,  화살표 방향을 down_right로 변경해라.
        dr = 0
    if j == 0 and dr == 3:     # 왼쪽옆면에 부딪혔을때 화살표 방향이 up_left라면,  화살표 방향을 up_right로 변경해라.
        dr = 2
    if j == w and dr == 0:     # 오른쪽옆면에 부딪혔을때 화살표 방향이 down_right라면,  화살표 방향을 down_left로 변경해라.
        dr = 1
    if j == w and dr == 2:     # 왼쪽옆면에 부딪혔을때 화살표 방향이 down_left라면,  화살표 방향을 down_right로 변경해라.
        dr = 3
    if i == 0 and j == w:      # 천장 오른쪽 모서리에 부딪혔을때
        dr = 1
    if i == h and j == 0:      # 바닥 왼쪽 모서리에 부딪혔을때
        dr = 2
        
    new_p, new_q = reverse_convert_coord(w, h, i, j)
    print(f"cnt : {cnt}, new_p : {new_p},  new_q : {new_q}")  

print(new_p, new_q)
"""
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
