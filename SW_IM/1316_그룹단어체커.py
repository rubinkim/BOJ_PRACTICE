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
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            pure_word.append(word[i])
    if len(pure_word) == len(set(pure_word)):
        ans += 1
print(ans)