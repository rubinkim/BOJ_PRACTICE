#-*- coding: utf-8 -*-
"""
3
5
6
7

(2)


6
5
7
9
8492
8493
192398

(2)


4
1000
2000
3000
4000

(4)


7
6
1
9
5
7
15
8

(0)
"""

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
print(f"arr : {arr}")

ans = 51
for i in range(n):
    for j in range(5):
        temp = list(range(arr[i]-j, arr[i]-j+5))
        
