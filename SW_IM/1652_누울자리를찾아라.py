#-*- coding: utf-8 -*-
"""
5
....X
..XX.
.....
.XX..
X....
"""

n = int(input())
arr = [list(input().split()) for _ in range(n)]
for row in arr:
    print(row)
    
for i in range(n):