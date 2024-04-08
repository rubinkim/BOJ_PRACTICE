#-*- coding: utf-8 -*-
"""
9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz

(2)
"""
n = int(input())
ans = 0
for _ in range(n):
    word = list(input())
    pure_word = [word[0]]