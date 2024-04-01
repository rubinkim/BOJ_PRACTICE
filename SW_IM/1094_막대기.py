#-*- coding: utf-8 -*-
"""
23

(4)
"""
x = int(input())
lst = []
while True:
    lst.append(x%2)
    x //= 2
    if x == 1:
        print(sum(lst))
        break
print(lst)