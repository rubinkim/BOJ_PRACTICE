#-*- coding: utf-8 -*-

"""
2
0 0 10 10
2 2 6 6

64 36


3
0 2 10 10
7 9 8 4
8 4 10 6

81 25 60


4
0 2 10 10
7 9 8 4
8 4 10 6
6 0 12 10

62 24 0 120

# method 1 : looping arr for every color paper : takes a very long time!
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n

for n in range(1, N+1):
    cnt = 0
    for lst in arr:
        cnt += lst.count(n)
    print(cnt)

# method 2 : Using frequenct list and then loop the arr just once by every row of the arr! : can save a lot of time!!!            
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n
            
cnts = [0] * (N+1)
for lst in arr:
    for n in lst:
        cnts[n] += 1
print(*cnts[1:], sep='\n')
"""

# method 3 : Using frequenct list and then loop the arr just once by every cell of the arr : can save a lot of time!!!            
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n
            
cnts = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        cnts[arr[i][j]] += 1
print(*cnts[1:], sep='\n')
            

# method 4 : Using frequent list and populate the arr more efficient way!!!
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):    
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        arr[i][sj : sj+w] = [n] * w
        
