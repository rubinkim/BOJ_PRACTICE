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

N1, M1 = map(int, input().split())
arr1 = [[""] * M1 for _ in range(N1)]
for i in range(N1):
    for j, x in enumerate(input()):
        arr1[i][j] = x
        
N2, M2 = map(int, input().split())
arr2 = [[""] * M2 for _ in range(N2)]
for i in range(N2):
    for j, x in enumerate(input()):
        arr2[i][j] = x
        
print(TC)
print(N1, M1)
for row in arr1:
    print(row)
print(N2, M2)
for row in arr2:
    print(row)
    
x = sum([sum([arr1[i][j] != 'W' for j in range(M1)]) for i in range(2)])
print(x)

def count_color(w, b, n, m):
    cnt = 0
    cnt += sum([sum([arr1[i][j] != 'W' for j in range(m)]) for i in range(w+1)])
    cnt += sum([sum([arr1[i][j] != 'B' for j in range(m)]) for i in range(w+1, b+1)])
    cnt += sum([sum([arr1[i][j] != 'R' for j in range(m)]) for i in range(b+1, n)])
    return cnt

print(count_color(1, 2, N1, M1))

cnt_lst = []
for a in range(1, N1-2):
    for b in range(1, N1-3):
        #print(f"i : {i},  j : {j},  cnt : {count_color(i, j, N1, M1)}")
        print(count_color(a, b, N1, M1))