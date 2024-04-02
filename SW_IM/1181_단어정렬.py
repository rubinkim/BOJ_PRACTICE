#-*- coding: utf-8 -*-
"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""

n = int(input())
lst = [set() for _ in range(n)]

for _ in range(n):
    word = input()
    lst[len(word)-1].append(word)
    
for l in lst:
    print(l)