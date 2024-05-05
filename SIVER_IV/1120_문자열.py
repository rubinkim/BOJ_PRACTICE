#-*- coding: utf-8 -*-
"""
adaabc aababbc
(2)

hello xello
(1)

koder topcoder
(1)

abc topabcoder
(0)

giorgi igroig
(6)
"""

a, b = input().split()
print(f"a : {a},  b : {b}")

diff = len(b) - len(a)
print(f"diff : {diff}")

cnt = 0
if diff == 0:
    for i in range(len(b)):
        if a[i] != b[i]:
            cnt += 1
            
else:
    for i in range(diff+1):
        new_a = b[:i] + a + b[-i:]
        print(f"i : {i},  new_a : {new_a},  b : {b}")
    
    