#-*- coding: utf-8 -*-
"""
ababababa
aba

(2)

a a a a a
a a

(2)

ababababa
ababa

(1)

aaaaaaa
aa

(3)
"""

lst = list(input())
word = input()

cnt = 0
i = 0
while len(lst) >= len(word):
    if lst[:len(word)] == list(word):
        cnt += 1
        i += len(word)
        lst = lst[len(word):]
    elif lst[:len(word)] != list(word):
        i += 1
        lst = lst[i:]
    if len(lst) == len(word) and lst != list(word):
        break
    
print(cnt)