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
lst = [[] for _ in range(51)]

for _ in range(n):
    word = input()
    if word not in lst[len(word)]:
        lst[len(word)].append(word)
    
for l in lst:
    if len(l) == 0:
        continue
    elif len(l) == 1:
        print(l[0])
    else:
        l.sort()
        for w in l:
            print(w)

"""
N = int(input())
lst = []

for _ in range(N):
    lst.append(input())

lst = list(set(lst))
lst.sort(key=lambda x : (len(x),x))

print("\n".join(lst))
"""
