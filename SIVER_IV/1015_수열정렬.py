#-*- coding: utf-8 -*-
"""
3
2 3 1

(1 2 0)

4
2 1 3 1

(2 0 3 1)

8
4 1 6 1 3 6 1 4

(4 0 6 1 3 7 2 5)
"""

n = int(input())
a = list(map(int, input().split()))

print(f"n : {n},   a : {a}")

p = []

a_sort = []
for i in range(len(a)):
    a_sort.append((a[i], i))
    
print(a_sort)
print(sorted(a_sort))

