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

a_tuple = []
for i in range(len(a)):
    a_tuple.append((a[i], i))
    
print(a_tuple)
a_sort = sorted(a_tuple)
print(a_sort)

lst = []
chk = [False] * n

for i in range(len(a)):
    for j in range(len(a_sort)):
        if a[i] == a_sort[j][0] and i == a_sort[j][1]:
            lst.append(j)
print(lst)
