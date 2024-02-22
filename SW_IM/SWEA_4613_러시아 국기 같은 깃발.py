#-*- coding: utf-8 -*-

"""
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
"""

TC = int(input())
for _ in range(TC):

    N, M = map(int, input().split())
    arr = [[""] * M for _ in range(N)]
    for i in range(N):
        for j, x in enumerate(input()):
            arr[i][j] = x
        


def count_color(w, b, arr, n, m):
    cnt = 0
    cnt += sum([sum([arr[i][j] != 'W' for j in range(m)]) for i in range(w+1)])
    cnt += sum([sum([arr[i][j] != 'B' for j in range(m)]) for i in range(w+1, b+1)])
    cnt += sum([sum([arr[i][j] != 'R' for j in range(m)]) for i in range(b+1, n)])
    return cnt

#print(count_color(0, 1, arr2, N2, M2))

cnt_lst = []
for x in range(N1-2):
    for y in range(x+1, N1-1):
        #print(f"x : {x},  y : {y},  cnt : {count_color(x, y, arr1, N1, M1)}")
        cnt_lst.append(count_color(x, y, arr1, N1, M1))
print(f"#1 {min(cnt_lst)}")        

cnt_lst = []
for x in range(N2-2):
    for y in range(x+1, N2-1):
        #print(f"x : {x},  y : {y},  cnt : {count_color(x, y, arr2, N2, M2)}")
        cnt_lst.append(count_color(x, y, arr2, N2, M2))
print(f"#1 {min(cnt_lst)}")  