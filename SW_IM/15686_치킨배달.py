"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

(5)


5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

(10)


5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

(11)


5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1

(32)
"""
from itertools import combinations

N, M = map(int, input().split())     # N : one-side length of the city,  M : maximum number of chicken houses
houses, chickens = [], []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):