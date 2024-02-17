#-*- coding: utf-8 -*-

"""
1
1
1 1

3
3 4 5
2 2

5
1000000 1000000 1000000 1000000 1000000
5 7

5
10 9 10 9 10
7 20

5
10 9 10 9 10
7 2


1 7 714290 10 13
"""

import sys
input = sys.stdin.readline
N = int(input())                                    # 5
classes = list(map(int, input().split()))           # 1000000 1000000 1000000 1000000 1000000
B, C = map(int, input().split())                    # 5 7
ans = 0

for cls in classes:
    ans += 1
    if cls <= B:
        continue
    else:
        cls -= B
        if cls % C == 0:
            ans += (cls // C)
        else:
            ans += (cls // C)
            ans += 1
print(ans)