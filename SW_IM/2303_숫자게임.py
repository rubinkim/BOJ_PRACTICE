#-*- coding: utf-8 -*-
"""
3
7 5 5 4 9
1 1 1 1 1
2 3 3 2 10

(1)
"""
from itertools import combinations
n = int(input())
lst = []

for _ in range(n):
    max_first_digit = -1
    for combi in combinations(map(int, input().split()), 3):
        temp = sum(combi) % 10
        max_first_digit = max(max_first_digit, temp)
    lst.append(max_first_digit)

#print(lst)
ans = 0
for i in range(len(lst)):
    if lst[i] == max(lst):
        ans = i + 1
print(ans)