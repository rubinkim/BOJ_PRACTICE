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
lst = [[] for _ in range(n)]

for _ in range(n):
    word = input()
    if word not in lst[len(word)-1]:
        lst[len(word)-1].append(word)
    
for l in lst:
    if l == []:
        continue
    elif l != []:
        l.sort()
        for w in l:
            print(w)
