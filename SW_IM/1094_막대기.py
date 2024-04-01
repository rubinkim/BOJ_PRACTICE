#-*- coding: utf-8 -*-
"""
3
2 2
1 5
13 29

(1 5 67863915)
"""
x = int(input())
lst = []
while True:
    if x == 1:
        print(sum(lst))
        break
    lst.append(x%2)
    x //= 2
print(lst)